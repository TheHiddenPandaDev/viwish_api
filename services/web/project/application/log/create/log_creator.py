from dataclasses import dataclass

from project.domain.log.log import Log
from project.infrastructure.persistance.PostgreeSQL.log.log_repository import LogRepository


@dataclass
class LogCreator:
    log_repository: LogRepository

    def __init__(
        self,
        log_repository: LogRepository,
    ):
        self.log_repository = log_repository

    def __call__(
        self,
        action_type: str,
        id_user: int,
        id_user_referred: int,
        description: str,
    ):
        log = Log(
            action_type,
            id_user,
            id_user_referred,
            description,
        )
        self.log_repository.create(log)