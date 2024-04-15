#!/usr/bin/env python3
"""module for Auth class"""

from flask import request
from typing import List, TypeVar


class Auth:
    """class auth"""

    def __init__(self):
        """initializing class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """function that  returns False"""
        return False

    def authorization_header(self, request=None) -> str:
        """that returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None"""
        return None
