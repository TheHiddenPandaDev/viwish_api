from dataclasses import dataclass
from typing import Optional

from project import db
from project.domain.user.repository.user_repository import ITUserRepository
from project.domain.user.user import User


@dataclass
class UserRepository(ITUserRepository):
    def getAll(self) -> list[User]:
        return User.query.all()
    def get(self, id_user: int) -> Optional[User]:
        return User.query.get(id_user)
    def getByEmail(self, email: str) -> User:
        return User.query.filter_by(email=email).first()

    def create(self, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user