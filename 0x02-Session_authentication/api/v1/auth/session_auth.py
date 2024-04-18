#!/usr/bin/env python3
"""model with class sessession"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """class session"""
    def __init__(self):
        """Create a session"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session"""
        if user_id is None:
            None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
