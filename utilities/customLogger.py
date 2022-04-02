import logging

class LogGeneration:

    @staticmethod
    def loggen():
        logging.basicConfig(
            filename='C:\\Users\\Elitebook\\PycharmProjects\\eCommerce\\automation.log',
            datefmt='%d/%m/%Y %I:%M:%S %p',
            format='%(asctime)s: %(levelname)s: %(message)s')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger