import inspect
import logging
import time


class Logger:
    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        current_time = time.strftime("%Y-%m-%d-%H")
        fileHandler = logging.FileHandler(f'..//Logs/logfile{current_time}.log')
        formatter = logging.Formatter("%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger