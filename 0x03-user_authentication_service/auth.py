#!/usr/bin/env python3
"""module for hashing password"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Optional


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

    def create_session(self, email: str) -> str:
        """creating session with id"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            user.session_id = session_id
            self._db._session.commit()
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """finding user by session id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """method that destroys a session"""
        if user_id is None:
            return None
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(email: str) -> str:
        """Generate reset password token"""
        try:
            user = self._db.find_user_by(email=email)
            uuid = _generate_uuid()
            user.update_user(user.id, reset_token=uuid)
            return uuid
        except NoResultFound:
            raise ValueError()
