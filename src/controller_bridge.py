import multiprocessing
import threading
import logging
import time
import sys
import os
import json

from driver_manager import RunDriverManager, DriverMgrCommands

# Version
version = "1.0.1"
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
        except Exception as e:
            self._logger.error(f"Config File is not correct. {e}")
            ready = False
        if self._driver_manager:
            self._pipe.send((DriverMgrCommands.SETUP_DRIVERS, drivers))
        while ready:
            pending_writes = {}
            if self._pipe:
                counter = 0
                while self._pipe.poll():
                    (command, data) = self._pipe.recv()
                    if command == DriverMgrCommands.UPDATES:
                        for handle, value in data.items():
                            bridge_handles = connections.get(handle, [])
                            for bridge_handle in bridge_handles:
                                pending_writes[bridge_handle] = value 
                    counter += 1
                    if counter >= MAX_PIPE_LOOPS: break
                if pending_writes:
                    self._pipe.send((DriverMgrCommands.UPDATES, pending_writes))
                time.sleep(1e-3)
    
if __name__ == '__main__':
    multiprocessing.freeze_support()
    # print(sys.argv)
    cb = ControllerBridge(use_processes=True, log_level=logging.INFO)
    config_file = os.path.dirname(os.path.abspath(__file__))+'/Controller_Bridge_Setup.json'
    cb.run(config_file=config_file)