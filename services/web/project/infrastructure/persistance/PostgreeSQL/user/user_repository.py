from dataclasses import dataclass

from project import db
from project.domain.user.repository.user_repository import ITUserRepository
from project.domain.user.user import User


@dataclass
class UserRepository(ITUserRepository):
    def getAll(self) -> None:
        print(User.query.all())
    def get(self, email: str) -> User:
        return User.query.filter_by(email=email).first()

    def create(self, user: User) -> User:
        db.session.add(user)
        return user