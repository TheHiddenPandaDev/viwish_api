from dataclasses import dataclass

from .user_creator import UserCreator


@dataclass
class CreateUserUseCase:
    user_creator: UserCreator

    def __init__(
        self,
        user_creator: UserCreator,
    ):
        self.user_creator = user_creator

    def __call__(
        self,
        email: str
    ):
        self.user_creator.__call__(email)