import logging
from asyncio.log import logger


class LogGen:
    @staticmethod
    def loggen():
        logging.getLogger()
        file = logging.FileHandler("D:\\Avinash\\Testing\\Automation\\Practice\\DPDzero\\Logs\\logfile.log")
        format1 = logging.Formatter("%(asctime)s : %(levelname)s :  %(name)s : %(funcName)s: %(message)s")
        file.setFormatter(format1)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger
