import logging


class Printer(logging.Handler):
    def emit(self, record):
        print(record)
