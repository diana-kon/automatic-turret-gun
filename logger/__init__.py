import logging

from .datadog import DataDogHandler
from .hoarder import Hoarder
from .printer import Printer


def create(driver: logging.Handler, name=""):
    if name == "":
        name = __name__
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    driver.setFormatter(formatter)
    logger.addHandler(driver)
    return logger


# compatibility with existing sources
create_logger = create
