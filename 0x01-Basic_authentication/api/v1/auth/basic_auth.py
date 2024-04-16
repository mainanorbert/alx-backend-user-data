#!/usr/bin/env python3
"""Basic auth class"""

import base64
from api.v1.auth.auth import Auth
import binascii


class BasicAuth(Auth):
    """basic auth class inheriting from Auth"""
    def __init__(self):
        pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ that returns the Base64 part of
        the Authorization header for a Basic Authentication"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """"returns the decoded value of a Base64 string
        base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decode_str = base64.b64decode(base64_authorization_header)
            return decode_str.decode('utf-8')
        except binascii.Error:
            return None
