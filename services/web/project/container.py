from dependency_injector import containers, providers

from project.infrastructure.persistance.PostgreeSQL.user.user_repository import UserRepository

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    # Repositories
    user_repository = providers.Singleton(UserRepository)
