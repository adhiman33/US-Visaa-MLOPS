from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys 


try:
    a=2/0
except Exception as e:
    logging.error("An error occured",exc_info=True)
    raise USvisaException(e,sys)


logging.info("Welcome to the custok logg")
