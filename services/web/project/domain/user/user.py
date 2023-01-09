from __future__ import annotations

from project import db

class User(db.Model):

    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(64), unique=True)

    def __init__(self, email):
        self.email = email

    @classmethod
    def create(cls, email: str) -> User:
        return cls(email)

    def json(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
        }