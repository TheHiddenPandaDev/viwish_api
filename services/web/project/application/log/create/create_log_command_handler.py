from dataclasses import dataclass

from .create_log_command import CreateLogCommand
from .create_log_use_case import CreateLogUseCase


@dataclass
class CreateLogCommandHandler:
    create_log_use_case: CreateLogUseCase

    def __init__(
        self,
        create_log_use_case: CreateLogUseCase,
    ):
        self.create_log_use_case = create_log_use_case


    def __call__(
        self,
        create_log_command: CreateLogCommand
    ):
        self.create_log_use_case.__call__(
            create_log_command.action_type,
            create_log_command.id_user,
            create_log_command.id_user_referred,
            create_log_command.description,
        )