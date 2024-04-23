#!/usr/bin/env python3
"""module for hashing password"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """function that returns bytes crypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
