import logging

from .datadog import DataDogHandler


def create_logger(driver: logging.Handler, name=""):
    if name == "":
        name = __name__
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    driver.setFormatter(formatter)
    logger.addHandler(driver)
    return logger


class Printer(logging.Handler):
    def emit(self, record):
        print(record)


class Hoarder(logging.Handler):
    records: list[logging.LogRecord] = []

    def emit(self, record):
        self.records.append(record)
