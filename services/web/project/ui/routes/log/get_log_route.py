from flask import Blueprint, jsonify, Response
from dependency_injector.wiring import inject, Provide

from project.domain.log.log import Log
from project.container import Container
from project.infrastructure.persistance.PostgreeSQL.log.log_repository import LogRepository

blueprint = Blueprint('get_log_route', __name__)

@blueprint.route("/<log_id>", methods=["GET"])
@inject
def get_log(log_id: int, repository: LogRepository = Provide[Container.log_repository]) -> tuple[Response, int]:

    print('----- START -----')
    print(repository.getAll())
    print('----- END -----')

    return jsonify({}), 200

    log: Log = repository.get(log_id)

    return jsonify(log.json()), 200