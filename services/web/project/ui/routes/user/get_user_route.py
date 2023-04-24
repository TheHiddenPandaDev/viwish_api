from flask import Blueprint, jsonify, Response
from dependency_injector.wiring import inject, Provide

from project.domain.user.user import User
from project.container import Container
from project.infrastructure.persistance.PostgreeSQL.user.user_repository import UserRepository

blueprint = Blueprint('get_user_route', __name__)

@blueprint.route("/<email>", methods=["GET"])
@inject
def get_user(email: str, repository: UserRepository = Provide[Container.user_repository]):

    user: User = repository.get(email)

    return jsonify(user.json()), 200