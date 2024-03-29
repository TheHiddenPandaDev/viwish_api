from dependency_injector import containers, providers

from project.application.log.create.create_log_command_handler import CreateLogCommandHandler
from project.application.log.create.create_log_use_case import CreateLogUseCase
from project.application.user.create.create_user_command_handler import CreateUserCommandHandler
from project.application.user.create.create_user_use_case import CreateUserUseCase
from project.application.user.create.user_creator import UserCreator
from project.domain.user.service.user_finder import UserFinder
from project.infrastructure.persistance.PostgreeSQL.log.log_repository import LogRepository
from project.infrastructure.persistance.PostgreeSQL.user.user_repository import UserRepository

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    # Domain Layer
    log_repository = providers.Singleton(LogRepository)
    user_repository = providers.Singleton(UserRepository)

    user_finder = providers.Factory(UserFinder, user_repository=user_repository)

    # Application Layer

    # Log - Create
    create_log_use_case = providers.Factory(
        CreateLogUseCase,
        log_repository=log_repository,
        user_finder=user_finder,
    )
    create_log_command_handler = providers.Factory(CreateLogCommandHandler, create_log_use_case=create_log_use_case)


    # User - Create
    user_creator = providers.Factory(UserCreator, user_repository=user_repository)
    create_user_use_case = providers.Factory(CreateUserUseCase, user_creator=user_creator)
    create_user_command_handler = providers.Factory(CreateUserCommandHandler, create_user_use_case=create_user_use_case)
