import time
import logging
import multiprocessing
import threading
import enum 


def RunDriverManager(pipe:multiprocessing.Pipe, use_processes:bool=False, log_level:int=logging.ERROR) -> None:
    _object = DriverManager(pipe, use_processes, log_level)
    _object.run()

class DriverMgrCommands(str, enum.Enum):
    SETUP_DRIVER = 'SETUP_DRIVER'
    CLEAN = 'CLEAN'
    UPDATES = 'UPDATES'


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
        
        self._pipe = pipe
        
        self._logger.debug("Driver Manager created")
    
    def run(self) -> None:
        self._logger.debug("Driver Manager running")
        while True:
            if self._pipe.poll():
                (command, data) = self._pipe.recv()
                if command == DriverMgrCommands.CLEAN:
                    break
        self._logger.debug("Driver Manager closed")
    
    