#!/usr/bin/env python3
"""module for Auth class"""

from flask import request
import os
from typing import List, TypeVar


class Auth:
    """class auth"""

    def __init__(self):
        """initializing class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """function that  returns False"""
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        for excluded_path in excluded_paths:
            if not path.endswith('/'):
                excluded_path = excluded_path[:-1]
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """that returns None"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None"""
        return None

    def session_cookie(self, request=None):
        """Session cookie"""
        if request is None:
            return None
        session_name = os.getenv("SESSION_NAME", "_my_session")
        return request.cookies.get(session_name)
