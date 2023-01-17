
from dataclasses import dataclass
from typing import Optional

from project.infrastructure.persistance.PostgreeSQL.user.user_repository import UserRepository
from ..user import User


@dataclass
class UserFinder:
    user_repository: UserRepository

    def __init__(
        self,
        user_repository: UserRepository,
    ):
        self.user_repository = user_repository

    def __call__(
        self,
        id_user: int
    ) -> Optional[User]:
       return self.user_repository.get(
            id_user
        )