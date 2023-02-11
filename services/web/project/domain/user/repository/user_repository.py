from abc import ABC
from typing import Optional

from project.domain.user.user import User


class ITUserRepository(ABC):
    def getAll(self) -> None:
        ...
    def get(self, id_user: int) -> Optional[User]:
        ...
    def getByEmail(self, email: str) -> User:
        ...

    def create(self, user: User) -> User:
        ...