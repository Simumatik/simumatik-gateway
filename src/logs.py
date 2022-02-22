#Logging
import logging
import os

LOCAL_FOLDER =  f"{os.path.expanduser('~')}/Simumatik"
FORMAT = '%(asctime)-15s %(levelname)s %(name)s: %(message)s'
logging.basicConfig(filename=f"{LOCAL_FOLDER}/gateway.log",
                    filemode='w',
                    level=logging.ERROR, 
                    #format=FORMAT
                    )

logger = logging.getLogger('GATEWAY')
logger.propagate = True
logger.setLevel(level=logging.INFO)