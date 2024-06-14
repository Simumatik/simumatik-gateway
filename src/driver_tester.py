import multiprocessing
import threading
import logging

from driver_manager import RunDriverManager, DriverMgrCommands


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
        
        self._pipe, pipe = multiprocessing.Pipe()
        
        if use_processes:
            self._driver_manager = multiprocessing.Process(target=RunDriverManager, args=(pipe, use_processes, log_level,), daemon=True)
            self._logger.debug("DriverTester running using processes")
        else:
            self._driver_manager = threading.Thread(target=RunDriverManager, args=(pipe, use_processes, log_level,), daemon=True)
            self._logger.debug("DriverTester running using threads")
            
        self._driver_manager.start()
        
    def setupDriver(self, setup_data:dict) -> None:
        pass
    
    def clean(self):
        self._logger.debug("DriverTester cleaning...")
        if self._driver_manager:
            self._pipe.send((DriverMgrCommands.CLEAN, None))
            self._driver_manager.join()
            self._driver_manager = None
        self._logger.debug("DriverTester cleaned up")
    
    def writeVariables(self, data:dict) -> None:
        pass
    
    def process(self) -> None:
        pass
    
    def getUpdates(self) -> dict:
        return {}
    

# Usage example
if __name__ == '__main__':
    
    import time

    LOG_FORMAT = '[%(asctime)s] - %(name)s - %(levelname)s - %(message)s'
    LOG_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z' # ISO8601 date format with timezone offset from UTC+0: YYYY-mm-ddTHH:MM:SS+HH:MM    logging.basicConfig(
    logging.basicConfig(
        level=logging.ERROR,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT
    )
    
    # Parameters
    TEST_TIME = 5
    
    # Create
    test = DriverTester(use_processes=False, log_level=logging.DEBUG)
    
    # Run for limited time
    start = time.perf_counter()
    while (time.perf_counter()-start)<TEST_TIME:
        test.process()
        res = test.getUpdates()
        if res:
            print(res)
    
    # Clean
    test.clean()