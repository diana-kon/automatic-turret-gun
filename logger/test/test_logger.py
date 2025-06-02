import logging

from logger import Hoarder, create_logger


def test_it_forwards_formatted_messages_to_logger():
    hoarder = Hoarder()
    logger = create_logger(hoarder, "test")

    logger.info("info")

    expectedOne = {
        "levelno": logging.INFO,
        "name": "test",
        "msg": "info",
        "pathname": __file__,
        "lineno": 10
    }

    actual = []
    for x in hoarder.records:
        raw = x.__dict__
        filtered = {k: raw[k] for k in expectedOne.keys() if k in raw}
        actual.append(filtered)

    assert [expectedOne] == actual
