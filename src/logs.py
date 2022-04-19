#Logging
import logging
import os

ACTUAL_PATH = os.path.dirname(os.path.abspath(__file__))
USER_PATH = os.path.expanduser('~')
if USER_PATH in ACTUAL_PATH:
    LOCAL_FOLDER = os.path.dirname(ACTUAL_PATH) # Works for different branches
else:
    LOCAL_FOLDER =  f"{USER_PATH}/Simumatik"

FORMAT = '%(asctime)-15s %(levelname)s %(name)s: %(message)s'
logging.basicConfig(filename=f"{LOCAL_FOLDER}/gateway.log",
                    filemode='w',
                    level=logging.ERROR, 
                    #format=FORMAT
                    )

logger = logging.getLogger('GATEWAY')
logger.propagate = True
logger.setLevel(level=logging.INFO)