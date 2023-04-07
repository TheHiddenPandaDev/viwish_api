from dataclasses import dataclass

from project.api_errors import ApiErrors
from project.documentation_urls import DocumentationUrls
from project.domain.log.log import Log
from project.domain.user.exception.user_not_found_exception import UserNotNotFoundException
from project.domain.user.service.user_finder import UserFinder
from project.domain.user.user import User
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
        if  (
            self.user_finder.__call__(id_user) is None or
            self.user_finder.__call__(id_user_referred) is None
        ):
            raise UserNotNotFoundException(
                code=400,
                description=f"id_user: {id_user} or id_user_referred: {id_user_referred}. Don't exist in database.",
                api_error_code=ApiErrors.table_log_unexpected_error['code'],
                api_error_event=ApiErrors.table_log_unexpected_error['event'],
                documentation=DocumentationUrls.url_create_log,
            )

        log = Log(
            log_id=None,
            action_type=action_type,
            id_user=id_user,
            id_user_referred=id_user_referred,
            description=description,
        )
        self.log_repository.create(log)