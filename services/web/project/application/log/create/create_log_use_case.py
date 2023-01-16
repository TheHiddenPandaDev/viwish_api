from dataclasses import dataclass

from .log_creator import LogCreator


@dataclass
class CreateLogUseCase:
    log_creator: LogCreator

    def __init__(
        self,
        log_creator: LogCreator,
    ):
        self.log_creator = log_creator

    def __call__(
        self,
        action_type: str,
        id_user: int,
        id_user_referred: int,
        description: str,

    ):
        self.log_creator.__call__(
            action_type,
            id_user,
            id_user_referred,
            description,
        )