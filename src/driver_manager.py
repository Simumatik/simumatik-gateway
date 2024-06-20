import time
import logging
import multiprocessing
import threading
import enum 
import os

from drivers import *

def RunDriverManager(pipe:multiprocessing.Pipe, use_processes:bool=False, log_level:int=logging.ERROR) -> None:
    _object = DriverManager(pipe, use_processes, log_level)
    _object.run()
    
def RunDriver(driver_object:any, name:str, pipe:multiprocessing.Pipe, params:dict, log_level:int=logging.ERROR) -> None:
    _object = driver_object(name, pipe, params)
    _object.run()

class DriverMgrCommands(str, enum.Enum):
    SETUP_DRIVERS = 'SETUP_DRIVERS'
    CLEAN = 'CLEAN'
    UPDATES = 'UPDATES'
    STATUS = 'STATUS'
    INFO = 'INFO'
    VAR_INFO = 'VAR_INFO'
    STATS = 'STATS'

class DriverStructure():
    
    def __init__(self, class_name:str, driver_name:str, handle:str, parameters:dict, pipe:multiprocessing.Pipe, driver_process:any):
        self.class_name = class_name
        self.name = driver_name
        self.handlers = [handle]
        self.parameters = parameters
        self.variables = {}
        self.status = ""
        self.info = ""
        self.pipe = pipe
        self.process = driver_process
        self.updates = {}
        
    def addHandle(self, handle:str):
        self.handlers.append(handle)
    
    def isCompatible(self, driver_data: dict) -> bool:
        """ Tells if the driver is compatible with the given class and setup parameters. 

        :param driver_data: Driver setup data, including parameters. (See documentation)

        :returns: True if compatible or False if not
        """
        driver_class_name = driver_data.get("DRIVER", "None")
        setup_data = driver_data.get("SETUP", {})
        parameters = setup_data.get("parameters", None)
        if self.class_name == driver_class_name:
            for key, value in parameters.items():
                if key in self.parameters:
                    if self.parameters[key] != value:
                        return False
            return True
        return False

    def addDriverVariables(self, variables:dict) -> dict:
        """ Adds variables to the given driver. 
        :param variables: Dictionary with all variables to be added. (See documentation)
        
        :returns: Dictionary with {<var_handle>: (<var_id>, <driver_name>)}
        """          
        res = {}
        var_setup_data = {}
        for var_id, var_data in variables.items(): 
            var_handle = var_data.get('handle', None)
            if var_handle is not None:
                if var_id not in self.variables:
                    var_structure = VariableStructure(var_handle, var_data)
                    self.variables[var_id] = var_structure
                    var_setup_data[var_id] = var_data
                else:
                    # TODO: Consider a variable that already has ben setup but now is the other type (READ/WRITE) so it should be changed to BOTH
                    # An option can be to store the variable operation as well in the self.variables dict ([handles], operation)
                    var_structure = self.variables[var_id] 
                    var_structure.addHandle(var_handle)   
                res[var_handle] = (var_id, self.name)
        if self.pipe and var_setup_data:
            self.pipe.send((DriverActions.ADD_VARIABLES, var_setup_data))
        return res
    
class VariableStructure():
    
    def __init__(self, handle:str, parameters:dict):
        self.handlers = [handle]
        self.parameters = parameters
        self.value = None
        self.info = ''
        self.write_count = 0
        self.read_count = 0

    def addHandle(self, handle:str):
        self.handlers.append(handle)

STATUS_FILE_PATH = os.path.dirname(os.path.abspath(__file__))+'/Driver_Manager_status.txt'

class DriverManager():
    
    def __init__(self, pipe:multiprocessing.Pipe, use_processes:bool=False, log_level:int=logging.ERROR) -> None:
        """

        :param use_processes: Allows to use processes instead of threads.
            it will have impact in performance and used resources

        :param log_level: Sets the logging level.

        Class to help testing drivers.
        """
        self._logger = logging.getLogger('DriverManager')
        self._logger.setLevel(log_level)
        if not self._logger.handlers: self._logger.addHandler(logging.StreamHandler())
        self._log_level = log_level
        
        self._pipe = pipe
        self._use_processes = use_processes
        self._drivers = {} # Dict to store drivers: {<driver_name>:<driver_struct>}
        self._driver_counter = 0
        self._handles = {} # Dict to store variables data: {<handle>: (<var_id>, <driver name>)}
        self._logger.info("Driver Manager: Created")        
        self._logger.info(f"Driver Manager: Status File path is {STATUS_FILE_PATH}")
        self._running = True
        self._start_time = int(time.perf_counter())
        self._last_status_record = 0
        self._save_status_time = 0
    
    def saveStatus(self, now_sec:int):
        start = time.perf_counter()
        try:
            with open(STATUS_FILE_PATH, 'w') as f:
                N = 100
                f.write(f'Driver Manager status: (clock = {now_sec}s, {round(self._save_status_time*1000,2)}ms to write)\n') 
                f.write('-'*N+'\n')
                for driver_struct in self._drivers.values():
                    f.write(f' {driver_struct.name}:\n') 
                    f.write(f'   - Type = {driver_struct.class_name}, Status = {driver_struct.status.value}, Info = {driver_struct.info}\n')
                    f.write(f'   - Parameters = {driver_struct.parameters}\n')
                    f.write(f'   - Handles = {driver_struct.handlers}, Variable count = {len(driver_struct.variables)}\n') 
                    f.write(f'   - Variables:\n')
                    for var_id, var_struct in driver_struct.variables.items():
                        f.write(f'    - {var_id} {var_struct.handlers} = {var_struct.value}  (R:{var_struct.read_count} W:{var_struct.write_count}) - {var_struct.info}\n')
                    f.write('-'*N+'\n')
        except:
            pass
        self._save_status_time = time.perf_counter() - start
        
    def run(self) -> None:
        MAX_PIPE_LOOPS = 10 # Is important to not never get locked in while loops
        self._logger.info("Driver Manager: Running")
        while self._running:
            can_sleep = True
            # INCOMMING COMMANDS (MULTIPLEX)
            counter = 0
            while self._pipe.poll():
                (command, data) = self._pipe.recv()
                if command == DriverMgrCommands.CLEAN:
                    self._logger.debug("Driver Manager: Clean request received")
                    self.cleanDrivers()
                    self._pipe.send((DriverMgrCommands.CLEAN, "SUCCESS"))
                    self._running = False
                    break
                elif command == DriverMgrCommands.SETUP_DRIVERS:
                    self._logger.debug("Driver Manager: Setup Drivers request received")
                    res, status_updates = self.setupDrivers(data)
                    self._pipe.send((DriverMgrCommands.SETUP_DRIVERS, res))
                    if status_updates:
                        self._pipe.send((DriverMgrCommands.STATUS, status_updates))
                elif command == DriverMgrCommands.UPDATES:
                    for var_handle, var_value in data.items():
                        (var_id, driver_name) = self._handles.get(var_handle, (None, None))
                        if driver_name:
                            if self._drivers[driver_name].status == DriverStatus.RUNNING:
                                if self._drivers[driver_name].variables[var_id].value != var_value:
                                    self._drivers[driver_name].updates[var_id] = var_value    
                                    self._drivers[driver_name].variables[var_id].write_count += 1
                                    self._drivers[driver_name].variables[var_id].value = var_value 
                        else:
                            self._logger.error(f"Driver Manager: Variable handle not found! {var_handle}")
                    for driver_struct in self._drivers.values():
                        if driver_struct.updates:
                            driver_struct.pipe.send((DriverActions.UPDATE, driver_struct.updates))
                            driver_struct.updates = {}     
                else:
                    self._logger.error(f"Driver Manager: Command not implemented!!!! {command}")
                counter += 1
                can_sleep = False
                if counter>=MAX_PIPE_LOOPS: break
                
            # OUTGOING COMMANDS (DEMULTIPLEX)
            status = {}       
            info = {}   
            var_info = {}   
            updates = {}    
            for driver_struct in self._drivers.values():
                counter = 0
                while driver_struct.pipe.poll():
                    (command, data) = driver_struct.pipe.recv()
                    if command == DriverActions.STATUS:
                        if driver_struct.status != data:
                            driver_struct.status = data
                            for handle in driver_struct.handlers:
                                status.update({handle: data})       
                    elif command == DriverActions.INFO:
                        if driver_struct.info != data:
                            driver_struct.info = data
                            for handle in driver_struct.handlers:
                                info.update({handle: data})       
                    elif command == DriverActions.VAR_INFO:
                        (msg, var_id) = data
                        var_struct = driver_struct.variables.get(var_id, None)
                        if var_struct is not None:
                            if var_struct.info != msg:
                                var_struct.info = msg
                                for handle in var_struct.handlers:
                                    var_info.update({handle: msg})       
                    elif command == DriverActions.UPDATE:
                        for var_id, value in data.items():
                            var_struct = driver_struct.variables.get(var_id, None)
                            if var_struct is not None:
                                if var_struct.value != value:
                                    var_struct.value = value
                                    var_struct.read_count += 1
                                    for handle in var_struct.handlers:
                                        updates.update({handle: value})       
                    else:
                        self._logger.debug(f"Driver Manager: Message received from {driver_struct.name}, {command} -> {data}")
                    can_sleep = False
                    counter += 1
                    if counter>=MAX_PIPE_LOOPS: break
            if status:
                self._pipe.send((DriverMgrCommands.STATUS, status))
            if info:
                self._pipe.send((DriverMgrCommands.INFO, info))
            if var_info:
                self._pipe.send((DriverMgrCommands.VAR_INFO, var_info))
            if updates:
                self._pipe.send((DriverMgrCommands.UPDATES, updates))
            
            # WRITE STATUS FILE
            now_sec = int(time.perf_counter()) - self._start_time
            if now_sec - self._last_status_record >= 1:
                self._last_status_record = now_sec
                self._pipe.send((
                    DriverMgrCommands.STATS, 
                    {
                        "DRIVER_COUNT":len(self._drivers), 
                        "VARIABLE_COUNT":len(self._handles),
                    }
                ))
                self.saveStatus(now_sec)            
            
            # SLEEP IF NO ACTIVITY
            if can_sleep:
                time.sleep(1e-3)    
                
        self._logger.debug("Driver Manager: Closed")
    
    def setupDrivers(self, drivers_setup_data:dict)->tuple:
        res = {}
        status_updates = {}
        for driver_handle, driver_data in drivers_setup_data.items():
            driver_struct = self.findCompatibleDriver(driver_data)
            if driver_struct is not None:
                driver_struct.addHandle(driver_handle)
                self._logger.info(f"Driver Manager: Driver {driver_handle} using compatible driver {driver_struct.name}")
                res[driver_handle] = "SUCCESS"
                if driver_struct.status:
                    status_updates[driver_handle] = driver_struct.status
            else:
                driver_struct = self.startDriver(driver_handle, driver_data)
                if driver_struct is not None:
                    self._drivers[driver_struct.name] =driver_struct
                    self._logger.info(f"Driver Manager: New Driver started {driver_struct.name} -> {driver_struct.class_name}")
                    res[driver_handle] = "SUCCESS"
                else:
                    res[driver_handle] = "FAILED"
            if driver_struct is not None:
                setup_data = driver_data.get("SETUP", {})
                self._handles.update(driver_struct.addDriverVariables(setup_data.get("variables", {})))
        return res, status_updates
    
    def cleanDrivers(self):
        for driver_name, driver_struct in self._drivers.items(): 
            self._logger.debug(f"Driver Manager: Exit command sent to driver {driver_name}")
            driver_struct.pipe.send((DriverActions.EXIT, None))
        
        while self._drivers:
            driver_name, driver_struct = self._drivers.popitem()
            driver_struct.process.join()
            self._logger.debug(f"Driver Manager: Driver {driver_name} closed")
    
    def startDriver(self, driver_handle:str, driver_data:dict) -> DriverStructure: 
        """ Starts a new Driver Process using the given parameters. 

        :param driver_handle: Driver handle procived by the user. (See documentation)

        :param driver_data: Driver setup data, including parameters. (See documentation)

        :returns: DriverStructure if Driver has been created, or None if not
        """
        driver_class_name = driver_data.get("DRIVER", "None")
        (driver_class, _) = registered_drivers.get(driver_class_name, (None, None))
        if driver_class is not None:
            self._driver_counter += 1
            driver_name = f"DRIVER_{self._driver_counter}"
            setup_data = driver_data.get("SETUP", {})
            parameters = setup_data.get("parameters", None)
            pipe, driver_pipe = multiprocessing.Pipe()
            if self._use_processes:
                driver_proc = multiprocessing.Process(target=RunDriver, args=(driver_class, driver_name, driver_pipe, parameters, self._log_level,), daemon=True)
            else:
                driver_proc = threading.Thread(target=RunDriver, args=(driver_class, driver_name, driver_pipe, parameters, self._log_level,), daemon=True)
            driver_proc.start()
            new_driver = DriverStructure(driver_class_name, driver_name, driver_handle, parameters, pipe, driver_proc)
            return new_driver
        return None
    
    def findCompatibleDriver(self, driver_data: dict) -> DriverStructure:
        """ Finds a compatible driver comparing the class and setup parameters within the existing ones. 

        :param driver_data: Driver setup data, including parameters. (See documentation)

        :returns: DriverStructure if compatible driver found or None if note
        """
        for driver_structure in self._drivers.values():
            if driver_structure.isCompatible(driver_data):
                return driver_structure
        return None
        
