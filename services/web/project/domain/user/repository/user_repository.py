from abc import ABC

from project.domain.user.user import User


class ITUserRepository(ABC):
    def getAll(self) -> None:
        ...
    def get(self, id_user: str) -> User:
        ...

    def create(self, user: User) -> User:
        ...