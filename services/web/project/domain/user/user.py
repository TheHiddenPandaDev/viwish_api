from __future__ import annotations

from project import db

class User(db.Model):

    user_id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(64), unique=True)

    def __init__(
        self,
        user_id: int,
        email: str,
     ):
        self.user_id = user_id
        self.email = email

    @classmethod
    def create(cls,
       user_id: int,
       email: str,
    ) -> User:
        return cls(
            user_id,
            email,
        )

    def json(self) -> dict:
        return {
            "user_id": self.user_id,
            "email": self.email,
        }