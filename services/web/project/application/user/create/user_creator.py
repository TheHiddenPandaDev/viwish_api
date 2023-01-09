from dataclasses import dataclass

from project.domain.user.user import User
from project.infrastructure.persistance.PostgreeSQL.user.user_repository import UserRepository


@dataclass
class UserCreator:
    user_repository: UserRepository

    def __init__(
        self,
        user_repository: UserRepository,
    ):
        self.user_repository = user_repository

    def __call__(
        self,
        email: str
    ):
        user = User(
            email,
        )
        self.user_repository.create(user)