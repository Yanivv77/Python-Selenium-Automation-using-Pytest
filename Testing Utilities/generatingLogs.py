import logging

# logging.basicConfig(filename=".\\logs\\logfile.log", format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%d-%m-%Y %H:%M:%S ', level=logging.INFO)
# log = logging.getLogger()
# log.info("First Log")

def log():
    logging.basicConfig(filename=".\\logs\\logfile.log", format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%d-%m-%Y %H:%M:%S ', level=logging.INFO)
    logger = logging.getLogger()
    return logger


logger = log()
logger.info("new log")
