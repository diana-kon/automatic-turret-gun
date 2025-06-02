import logging


class Hoarder(logging.Handler):
    records: list[logging.LogRecord] = []

    def emit(self, record):
        self.records.append(record)
