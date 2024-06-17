import multiprocessing
import threading
import logging
import time

from driver_manager import RunDriverManager, DriverMgrCommands
from drivers.driver import VariableOperation, VariableDatatype

class DriverTester():
    
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
        
        self._pipe, pipe = multiprocessing.Pipe()
        self._driver_manager = threading.Thread(target=RunDriverManager, args=(pipe, use_processes, log_level,), daemon=True)
        self._logger.debug("Driver Tester: Running using threads")
        self._driver_manager.start()
        
        self._pending_writes = {}
        self._pending_reads = {}
        
    def setupDrivers(self, drivers_setup_data:dict) -> None:
        """ 
        :param drivers_setup_data: Dictionay including setup data for each of the drivers {<driver_handle>:<setup_data>}

        Send one or several driver setup request to the Driver Manager
        """
        if self._driver_manager:
            self._pipe.send((DriverMgrCommands.SETUP_DRIVERS, drivers_setup_data))
            (_, result) = self._pipe.recv()
            self._logger.debug(f"Driver Tester: Driver setup results received: {result}") 
    
    def writeVariables(self, write_data:dict) -> None:
        """ 
        :param write_data: Dictionay including variable handles with the value to be written {<var_handle>:<var_value>}

        Make a multiple variable write request to the Driver Manager. The request will be sent pending until next cycle.
        """
        self._pending_writes.update(write_data)

    def getReadUpdates(self) -> dict:
        """ 
        Returns read variable updates since last call. Dictionay including variable handles with the read value {<var_handle>:<var_value>}
        """
        res = dict(self._pending_reads)
        self._pending_reads = {}
        return res
    
    def process(self) -> None:
        """ 
        Processes requests and responses from the DriverManager
        """
        MAX_PIPE_LOOPS = 10 # Is important to not never get locked in while loops
        if self._pipe:
            if self._pending_writes:
                self._pipe.send((DriverMgrCommands.UPDATES, self._pending_writes))
                self._pending_writes = {}
            counter = 0
            while self._pipe.poll():
                (command, data) = self._pipe.recv()
                if command == DriverMgrCommands.UPDATES:
                    self._pending_reads.update(data) 
                elif command == DriverMgrCommands.STATUS:
                    self._logger.debug(f"Driver Tester: Driver status changes received: {data}") 
                elif command == DriverMgrCommands.INFO:
                    self._logger.debug(f"Driver Tester: Driver info changes received: {data}") 
                elif command == DriverMgrCommands.VAR_INFO:
                    self._logger.debug(f"Driver Tester: Driver variable info changes received: {data}") 
                elif command == DriverMgrCommands.STATS:
                    self._logger.debug(f"Driver Tester: Driver manager stats received: {data}") 
                else:
                    print(f"Pending command processing: {command}")
                counter += 1
                if counter >= MAX_PIPE_LOOPS: break

    def clean(self):
        """ 
        Closes Driver Manager
        """
        if self._driver_manager:
            self._logger.debug("Driver Tester: Cleaning request sent to DriverManager...")
            self._pipe.send((DriverMgrCommands.CLEAN, None))
            while True:
                (command, result) = self._pipe.recv()
                if command == DriverMgrCommands.CLEAN:
                    self._logger.debug(f"Driver Tester: Cleaning response received from DriverManager -> {result}")
                    break
            self._driver_manager.join()
            self._driver_manager = None
            self._logger.debug("Driver Tester: Cleaned up, DriverManager closed")
    
def Test_Driver(setup_data:dict, run_time:int=20, log_level:int=logging.INFO, sleep_time:float=1e-3):
    # SETUP LOGGING
    LOG_FORMAT = '[%(asctime)s] - %(name)s - %(levelname)s - %(message)s'
    LOG_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z' # ISO8601 date format with timezone offset from UTC+0: YYYY-mm-ddTHH:MM:SS+HH:MM
    logging.basicConfig(
        level=log_level,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT
    )
    logger = logging.Logger("Test")
    logger.addHandler(logging.StreamHandler())
    logger.debug("Starting test")
    # CRAWL VARIABLES TO ADD HANDLES IF NEEDED AND GET WRITE VARIABLES
    input_variables = {}
    var_counter = 0
    for driver_setup in setup_data.values():
        setup = driver_setup.get("SETUP")
        variables = setup.get('variables')
        for var_data in variables.values():
            if 'handle' not in var_data:
                var_data['handle'] = 'h'+str(var_counter).zfill(5)
                var_counter += 1
            if var_data.get('operation') in [VariableOperation.WRITE, VariableOperation.BOTH]:
                input_variables[var_data.get('handle')] = (var_data.get('datatype'), var_data.get('size'))
    # SETUP DRIVER TESTER
    test = DriverTester(use_processes=False, log_level=log_level)
    test.setupDrivers(setup_data)
    # START LOOP
    start = time.perf_counter()
    counter = 0
    while (time.perf_counter()-start)<run_time:
        counter += 1
        new_values = {}
        for var_handle, (datatype, size) in input_variables.items():
            if datatype in [VariableDatatype.BOOL]:
                new_values[var_handle] = True if counter%2 else False
            elif datatype in [VariableDatatype.BYTE]:
                new_values[var_handle] = counter%2**8
            elif datatype in [VariableDatatype.WORD]:
                new_values[var_handle] = counter%2**16
            elif datatype in [VariableDatatype.INTEGER]:
                new_values[var_handle] = -2**15 + counter%2**16
            elif datatype in [VariableDatatype.DWORD]:
                new_values[var_handle] = counter%2**32
            elif datatype in [VariableDatatype.QWORD]:
                new_values[var_handle] = counter%2**64
            elif datatype in [VariableDatatype.FLOAT]:
                new_values[var_handle] = counter*3.1415
            elif datatype in [VariableDatatype.FLOAT]:
                new_values[var_handle] = str(counter)
        test.writeVariables(new_values)
        test.process()
        #test.getReadUpdates()
        time.sleep(sleep_time)
    test.clean()
    # Finish
    logger.debug("Driver test finished")