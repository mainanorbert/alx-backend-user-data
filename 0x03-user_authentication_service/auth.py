#!/usr/bin/env python3
"""module for hashing password"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """function that returns bytes crypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def _generate_uuid() -> str:
    """method to generate uuids"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """method returning user object"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            passwd = _hash_password(password)
            return self._db.add_user(email, passwd)

    def valid_login(self, email: str, password: str) -> bool:
        """method for validation"""
        try:
            user = self._db.find_user_by(email=email)
            passwd_b = password.encode('utf-8')
            return bcrypt.checkpw(passwd_b, user.hashed_password)
        except NoResultFound:
            return False
