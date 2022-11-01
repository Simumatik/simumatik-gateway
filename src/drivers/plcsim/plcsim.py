# Simumatik Gateway - Simumatik 3rd party integration tool
# Copyright (C) 2021 Simumatik AB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import struct
from multiprocessing import Pipe
from typing import Optional
import ctypes
import time

from ..s7protocol.iso_on_tcp import(
    PDU, getAreaFromString, getPDU, formatPDU, 
    PDU_from_ReadAreas, ReadAreas_from_PDU, 
    PDU_from_WriteAreas, WriteAreas_from_PDU)
from .s7onlinx import UserDataConnectionConfig, UserDataConnectionConfigTia, S7OexchangeBlock
from ..driver import driver


class plcsim(driver):
    '''
    Driver to communicate with Siemens PLCSim using S7Onlinx.dll.
    Compatible with PLCSim Tia Portal. Pending testing it against older PLCSim.

    Parameters:
    ip: str
        IP address of the controller that want to connect to. Default = '192.168.0.1'
    
    rack: int
        Rack number of the CPU. Default = 0
    
    slot: int
        Slot number of the CPU. Default = 1

    mode: str
        PLCSim version to be used: S7comm or S7commPlus (1200/1500). Default = 'S7comm'

    '''

    # CONSTANTS
    MaxPDULength    = 1920
    PDU_COUNTER     = 0
    MAX_ITEMS       = 10 # Number of elements that can be read or write at the time

    def __init__(self, name: str, pipe: Optional[Pipe] = None, params:dict = None):
        """
        :param name: (optional) Name for the driver
        :param pipe: (optional) Pipe used to communicate with the driver thread. See gateway.py
        """
        # Inherit
        driver.__init__(self, name, pipe, params)

        # Parameters
        self.ip = '192.168.0.1'
        self.rack = 0
        self.slot = 1
        self.mode = 'S7comm'


    def connect(self) -> bool:
        """ Connect driver.
        
        : returns: True if connection established False if not
        """
        try:
            self._connection = ctypes.WinDLL('s7onlinx.dll')
            self.connectionHandle = 0
            self.app_opcode = 0
            self.app_subs = 0
            self.extra_ack = False
            self.opt = (self.mode == 'S7commPlus')

        except Exception as e:
            self.sendDebugInfo(f"s7onlinx.dll cannot be loaded!")
            return False

        if self.connectPLCSim(ip=self.ip, rack=self.rack, slot=self.slot):
            # PDU length request
            self.PDU_COUNTER += 1
            PARAMS = b'\xf0\x00\x00\x01\x00\x01\x03\xc0'
            request_PDU = PDU(Command = 0x32,
                            Type = 0x01,
                            DestRef = 0x0000,
                            SourceRef = self.PDU_COUNTER,
                            ParamLength = len(PARAMS),
                            DataLength = 0x00,                  
                            Params = PARAMS,
                            Data = b'')
            reply_PDU = self.exchangePDU(request_PDU)
            if reply_PDU:
                _, _, PDULength = struct.unpack('!HIH',reply_PDU.Params)
            if (self.MaxPDULength > PDULength): self.MaxPDULength = PDULength
            self.sendDebugInfo("New PDU Max length set to: "+str(self.MaxPDULength))
            return True

        self.sendDebugInfo(f"Connection with PLCSim cannot be established.")
        return False


    def disconnect(self):
        """ Disconnect driver.
        """
        if self._connection:
            self._areas = {}
            if self.opt:
                fdr = S7OexchangeBlock(opcode=12, application_block_opcode=self.app_opcode, application_block_subsystem=self.app_subs)
                self.send_block(fdr)
            self._connection.SCP_close(self.connectionHandle)
            print("Disconnected")


    def addVariables(self, variables: dict):
        """ Add variables to the driver. Correctly added variables will be added to internal dictionary 'variables'.
        Any error adding a variable should be communicated to the server using sendDebugInfo() method.

        : param variables: Variables to add in a dict following the setup format. (See documentation) 
        
        """
        # TODO: Size is not considered
        for var_id in list(variables.keys()):
            var_data = dict(variables[var_id])
            area = getAreaFromString(var_id, var_data['datatype'])
            if area is not None:
                var_data['area'] = area
                var_data['value'] = None
                self.variables[var_id] = var_data
            else:
                self.sendDebugVarInfo(('SETUP: Bad variable definition: {}'.format(var_id), var_id))


    def readVariables(self, variables: list) -> list:
        """ Read given variable values. In case that the read is not possible or generates an error BAD quality should be returned.
        : param variables: List of variable ids to be read. 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        varray = []
        for var_id in variables:
            varray.append((var_id, self.variables[var_id]['area']))

        res = []
        if len(varray)>0:
            
            while len(varray):
                if len(varray) >= self.MAX_ITEMS:
                    rarray = varray[:self.MAX_ITEMS]
                    del varray[:self.MAX_ITEMS]
                else:
                    rarray = varray[:]
                    varray = []

                self.PDU_COUNTER += 1
                request_PDU = PDU_from_ReadAreas(self.PDU_COUNTER, rarray)
                reply_PDU = self.exchangePDU(request_PDU)

                for (vname, vvalue, quality) in ReadAreas_from_PDU(reply_PDU, rarray):
                    res.append((vname, vvalue, quality))
        return res


    def writeVariables(self, variables: list) -> list:
        """ Write given variable values. In case that the write is not possible or generates an error BAD quality should be returned.
        : param variables: List of tupples with variable ids and the values to be written (var_id, var_value). 

        : returns: list of tupples including (var_id, var_value, VariableQuality)
        """
        varray = []
        for (var_id, new_value) in variables:
            if new_value != None:
                varray.append((var_id, self.variables[var_id]['area'], new_value))

        res = []
        if len(varray)>0:
            while len(varray):
                if len(varray) >= self.MAX_ITEMS:
                    warray = varray[:self.MAX_ITEMS]
                    del varray[:self.MAX_ITEMS]
                else:
                    warray = varray[:]
                    varray = []
                
                self.PDU_COUNTER += 1
                request_PDU = PDU_from_WriteAreas(self.PDU_COUNTER, warray)
                reply_PDU = self.exchangePDU(request_PDU)

                for (vname, vvalue, quality) in WriteAreas_from_PDU(reply_PDU, warray):
                    res.append((vname, vvalue, quality))

        return res    


    def receive_block(self, timeout:int=1)->S7OexchangeBlock:
        rec_len = (ctypes.c_int16)()
        length = ctypes.c_int16(80+1024)
        buffer = ctypes.create_string_buffer(length.value)
        t = time.perf_counter()
        while (time.perf_counter()-t)<timeout:
            try:
                self._connection.SCP_receive(self.connectionHandle, 0, ctypes.byref(rec_len), length, buffer)
                assert (rec_len.value>=80), "Block receive exception"
                return S7OexchangeBlock.from_buffer(buffer)
            except:
                pass
        return None


    def send_block(self, block:S7OexchangeBlock)->bool:
        try:
            # TODO: Check if send_len can be get from buffer
            (send_len, buffer) = block.to_buffer()
            ret = self._connection.SCP_send(self.connectionHandle, send_len, buffer)
            assert ret==0, "Block send exception"
            return True
        except:
            return False


    def connectPLCSim(self, ip:str='192.168.0.1', rack:int=0, slot:int=1)->bool:
        try:
            self.connectionHandle = self._connection.SCP_open('S7ONLINE'.encode('utf-8')) # Encoding is very important
            e = self._connection.SCP_get_errno()
            if self.connectionHandle>0 and e == 0:                
                # Get Reachable Partners
                self.PDU_COUNTER = 1
                user = self.PDU_COUNTER if not self.opt else 0
                fdr = S7OexchangeBlock(user=user, rb_type=2, subsystem=0x7a, opcode=128, response=0xff, application_block_opcode=0x00, application_block_subsystem=0x00)
                fdr.priority = 1
                fdr.fill_length_1 = 13
                fdr.set_user_data(fdr.fill_length_1, b'\x00'*fdr.fill_length_1)
                fdr.seg_length_1 = 0
                fdr.offset_1 = 80
                self.send_block(fdr)
                rec = self.receive_block()
                assert (rec.opcode == 128 and rec.user == user and rec.fill_length_1 >= 64), "TODO"

                # First telegram
                self.PDU_COUNTER += 1
                user = self.PDU_COUNTER if not self.opt else 0
                if not self.opt:
                    fdr = S7OexchangeBlock(user=user, application_block_opcode=0x00, application_block_subsystem=0x00)
                    fdr.offset_1 = 0
                else:
                    fdr = S7OexchangeBlock(user=user, application_block_opcode=0xff, application_block_subsystem=0xff)
                    fdr.offset_1 = 80
                    fdr.response = 0xffff               
                self.send_block(fdr)
                rec = self.receive_block()
                assert (rec.opcode == 0x00 and rec.response == 0x01), "TODO"
                self.app_opcode = rec.application_block_opcode
                self.app_subs = rec.application_block_subsystem

                # Set IP, rack and Slot
                if not self.opt:
                    self.PDU_COUNTER += 1
                    fdr = S7OexchangeBlock(user=self.PDU_COUNTER, opcode=1, application_block_opcode=self.app_opcode, application_block_subsystem=self.app_subs)
                    fdr.application_block_ssap = 2
                    fdr.application_block_remote_address_station = 114

                    ud_cfg = UserDataConnectionConfig(ip=ip, rack=rack, slot=slot)
                    (length, buffer) = ud_cfg.to_buffer()
                    fdr.set_user_data(126, buffer+ b'\x00'*(126-length))
                else:
                    fdr = S7OexchangeBlock(user=0, opcode=1, application_block_opcode=self.app_opcode, application_block_subsystem=self.app_subs)
                    fdr.fill_length_1 = 34
                    fdr.seg_length_1 = 34
                    fdr.offset_1 = 80                 
                    fdr.response = 0xffff

                    ud_cfg = UserDataConnectionConfigTia(ip=ip)
                    (length, buffer) = ud_cfg.to_buffer()
                    fdr.set_user_data(126, buffer+ b'\x00'*(126-length))
                self.send_block(fdr)
                rec = self.receive_block()
                assert (rec.opcode == 0x01 and rec.response == 0x01), "TODO"

                if self.opt:
                    fdr = S7OexchangeBlock(user=0, opcode=13, application_block_opcode=self.app_opcode, application_block_subsystem=self.app_subs)
                    fdr.fill_length_1 = 0
                    fdr.seg_length_1 = 1024
                    fdr.offset_1 = 80            
                    fdr.response = 0xffff
                    self.send_block(fdr)

                    fdr = S7OexchangeBlock(user=0, opcode=7, application_block_opcode=self.app_opcode, application_block_subsystem=self.app_subs)
                    fdr.fill_length_1 = 0
                    fdr.seg_length_1 = 0
                    fdr.offset_1 = 80            
                    fdr.response = 0xffff
                    self.send_block(fdr)

                # Connection is valid
                return True

        except Exception as e:
            return False


    def exchangePDU(self, pdu:PDU)->PDU:  
        """ Send a PDU."""
        if self.connectionHandle<0:
            return None
        try:
            # Send PDU
            user = pdu.SourceRef if not self.opt else 0
            fdr = S7OexchangeBlock(user=user, opcode=6, application_block_opcode=self.app_opcode, application_block_subsystem=self.app_subs)
            buffer = formatPDU(pdu)
            fdr.response = 0xff if not self.opt else 0xffff
            fdr.set_user_data(len(buffer), buffer)
            self.send_block(fdr)

            # Acknowledge send
            rec = self.receive_block()
            assert (rec.opcode == 0x06 and rec.response == 0x01), "TODO"

            # Extra Acknowledge is needed only once!
            if not self.extra_ack and not self.opt:
                self.extra_ack = True
                fdr = S7OexchangeBlock(user=0, opcode=7, application_block_opcode=rec.application_block_opcode, application_block_subsystem=rec.application_block_subsystem)
                fdr.seg_length_1 = 1024
                self.send_block(fdr)

            # Receive data
            rec = self.receive_block()
            assert (rec.opcode == 0x07 and rec.response == 0x03), "TODO"

            # Acknowledge reception
            fdr = S7OexchangeBlock(user=0, opcode=7, application_block_opcode=rec.application_block_opcode, application_block_subsystem=rec.application_block_subsystem, response=0)
            fdr.seg_length_1 = 1024
            fdr.response = 0xff if not self.opt else 0xffff
            self.send_block(fdr)

            # Return PDU
            return getPDU(rec.user_data_1)

        except:
            return None