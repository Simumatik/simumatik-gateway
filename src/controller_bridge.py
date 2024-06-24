import multiprocessing
import threading
import logging
import time
import sys
import os
import json

from driver_manager import RunDriverManager, DriverMgrCommands

# Version
version = "1.0.2"
class ControllerBridge():
    
    def __init__(self, use_processes:bool=False, log_level:int=logging.ERROR) -> None:
        """
        :param use_processes: Allows to use processes instead of threads.
            it will have impact in performance and used resources

        :param log_level: Sets the logging level.

        Class to help testing drivers.
        """
        self._logger = logging.getLogger('DriverTester')
        self._logger.setLevel(log_level)
        if not self._logger.handlers: self._logger.addHandler(logging.StreamHandler())
        
        self._logger.info(f"Controller Bridge version {version} started. (Using processes={use_processes})")
        self._pipe, pipe = multiprocessing.Pipe()
        self._driver_manager = threading.Thread(target=RunDriverManager, args=(pipe, use_processes, log_level,), daemon=True)
        self._logger.info("ControllerBridge: Running using threads")
        self._driver_manager.start()
    
    def run(self, config_file:str="") -> None:
        """ 
        Processes requests and responses from the DriverManager
        """
        def invert_value_byte_order(value, datatype):
            if datatype == "word":
                byte_1 = ((value & 0x00ff) << 8)
                byte_0 = ((value & 0xff00) >> 8)
                return byte_1+byte_0
            elif datatype == "dword":
                byte_3 = ((value & 0x000000ff) << 8*3)
                byte_2 = ((value & 0x0000ff00) << 8)
                byte_1 = ((value & 0x00ff0000) >> 8)
                byte_0 = ((value & 0xff000000) >> 8*3)
                return byte_3+byte_2+byte_1+byte_0
            elif datatype == "qword":
                byte_7 = ((value & 0x00000000000000ff) << 8*7)
                byte_6 = ((value & 0x000000000000ff00) << 8*5)
                byte_5 = ((value & 0x0000000000ff0000) << 8*3)
                byte_4 = ((value & 0x00000000ff000000) << 8)
                byte_3 = ((value & 0x000000ff00000000) >> 8)
                byte_2 = ((value & 0x0000ff0000000000) >> 8*3)
                byte_1 = ((value & 0x00ff000000000000) >> 8*5)
                byte_0 = ((value & 0xff00000000000000) >> 8*7)
                return byte_7+byte_6+byte_5+byte_4+byte_3+byte_2+byte_1+byte_0
            else:
                return value

        MAX_PIPE_LOOPS = 10 # Is important to not never get locked in while loops
        ready = True
        try:
            f = open(config_file, "r")
            data = json.load(f)
            drivers = data["drivers"]
            connections = data["connections"]
            # Transform connections to lists
            for key, value in connections.items():
                if not isinstance(value, list):
                    connections[key] = [value]
            # Get Invert Byte orders
            invert_byte_order = {}
            for key, driver_data in drivers.items():
                setup_data = driver_data["SETUP"]
                variables = setup_data.get("variables", None)
                if variables:
                    for _, var_data in variables.items():
                        handle = var_data.get("handle", None)
                        inv = var_data.get("invert_byte_order", False)
                        inv_datatype = var_data.get("datatype", bool)
                        if handle and inv and (inv_datatype in ["word", "dword", "qword"]):
                            invert_byte_order[handle] = inv_datatype
        except Exception as e:
            self._logger.error(f"Config File is not correct. {e}")
            ready = False
        if self._driver_manager and ready:
            self._pipe.send((DriverMgrCommands.SETUP_DRIVERS, drivers))
        while ready:
            pending_writes = {}
            if self._pipe:
                counter = 0
                while self._pipe.poll():
                    (command, data) = self._pipe.recv()
                    if command == DriverMgrCommands.UPDATES:
                        for handle, value in data.items():
                            inv_read = invert_byte_order.get(handle, '')
                            bridge_handles = connections.get(handle, [])
                            for bridge_handle in bridge_handles:
                                inv_write = invert_byte_order.get(bridge_handle, '')
                                if (not inv_read and not inv_write) or (inv_read and inv_write):
                                    pending_writes[bridge_handle] = value 
                                else:
                                    pending_writes[bridge_handle] = invert_value_byte_order(value, inv_write if inv_write else inv_read)
                    counter += 1
                    if counter >= MAX_PIPE_LOOPS: break
                if pending_writes:
                    self._pipe.send((DriverMgrCommands.UPDATES, pending_writes))
                if counter == 0:
                    time.sleep(1e-3)
    
if __name__ == '__main__':
    multiprocessing.freeze_support()
    # print(sys.argv)
    cb = ControllerBridge(use_processes=True, log_level=logging.INFO)
    config_file = os.path.dirname(os.path.abspath(__file__))+'/Controller_Bridge_Setup.json'
    cb.run(config_file=config_file)