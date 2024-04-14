#!/usr/bin/env python3
"""0. Regex-ing"""

from typing import List
import re
import logging

PII_FIELDS = ("name", "password", "email", "ssn", "phone")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """filtering values of incoming records"""
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """Regex-ing"""
    regex = r'(' + '|'.join(fields) + r')=[^' + separator + r']*'
    return re.sub(regex, lambda match: match.group(1) + '=' + redaction,
                  message)


def get_logger() -> logging.Logger:
    """ Create logger"""
    logger = logging.getLogger('user_data')
    logger.seLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler = logging.streamHandler(sys.out)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
