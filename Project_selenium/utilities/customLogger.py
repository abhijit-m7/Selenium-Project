import logging

class logGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename = "/home/abhijit/Desktop/python/Project_selenium/Logs/automation.log",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger