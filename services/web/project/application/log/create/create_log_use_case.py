from dataclasses import dataclass

from project.domain.log.log import Log
from project.domain.user.exception.user_not_found_exception import UserNotNotFoundException
from project.domain.user.service.user_finder import UserFinder
from project.infrastructure.persistance.PostgreeSQL.log.log_repository import LogRepository


@dataclass
class CreateLogUseCase:
    log_repository: LogRepository
    user_finder: UserFinder

    def __init__(
        self,
        log_repository: LogRepository,
        user_finder: UserFinder,
    ):
        self.log_repository = log_repository
        self.user_finder = user_finder

    def __call__(
        self,
        action_type: str,
        id_user: int,
        id_user_referred: int,
        description: str,

    ):

        # Finder id_user
        if  (
            self.user_finder.__call__(id_user) is None or
            self.user_finder.__call__(id_user_referred) is None
        ):
            raise UserNotNotFoundException(
                code=403,
                description=f"id_user: {id_user} or id_user_referred: {id_user_referred} don't exist in database",
                api_error_code=1234,
                documentation='test',
            )

        log = Log(
            action_type,
            id_user,
            id_user_referred,
            description,
        )
        self.log_repository.create(log)