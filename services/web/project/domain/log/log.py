from __future__ import annotations

import datetime
from typing import Optional

from project import db

class Log(db.Model):

    log_id: int = db.Column(db.Integer, primary_key=True)
    action_type: str = db.Column(db.String(64))
    id_user: int = db.Column(db.Integer)
    id_user_referred: int = db.Column(db.Integer)
    description: str = db.Column(db.Text)
    created_at: datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self,
        log_id: Optional[int],
        action_type: str,
        id_user: int,
        id_user_referred: int,
        description:str,
    ):
        self.log_id = log_id
        self.action_type = action_type
        self.id_user = id_user
        self.id_user_referred = id_user_referred
        self.description = description

    @classmethod
    def create(cls,
       log_id: int,
       action_type: str,
       id_user: int,
       id_user_referred: int,
       description: str,
    ) -> Log:
        return cls(
            log_id,
            action_type,
            id_user,
            id_user_referred,
            description,
        )

    def json(self) -> dict:
        return {
            "log_id": self.log_id,
            "action_type": self.action_type,
            "id_user": self.id_user,
            "id_user_referred": self.id_user_referred,
            "description": self.description,
            "created_at": self.created_at,
        }