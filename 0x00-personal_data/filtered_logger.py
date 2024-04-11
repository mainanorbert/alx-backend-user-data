#!/usr/bin/env python3
"""0. Regex-ing"""

from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """Regex-ing"""
    regex = r'(' + '|'.join(fields) + r')=[^' + separator + r']*'
    return re.sub(regex, lambda match: match.group(1) + '=' + redaction,
                  message)
