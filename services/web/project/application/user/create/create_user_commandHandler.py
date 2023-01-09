from dataclasses import dataclass

from .create_user_command import CreateUserCommand
from .create_user_use_case import CreateUserUseCase


@dataclass
class CreateUserCommandHandler:
    create_user_use_case: CreateUserUseCase

    def __init__(
        self,
        create_user_use_case: CreateUserUseCase,
    ):
        self.create_user_use_case = create_user_use_case


    def __call__(
        self,
        create_user_command: CreateUserCommand
    ):
        self.create_user_use_case.__call__(
            create_user_command.email,
        )