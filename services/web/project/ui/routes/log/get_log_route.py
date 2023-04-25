from flask import Blueprint, jsonify, Response
from dependency_injector.wiring import inject, Provide

from project.domain.log.log import Log
from project.container import Container
from project.infrastructure.persistance.PostgreeSQL.log.log_repository import LogRepository

blueprint = Blueprint('get_log_route', __name__)

@blueprint.route("/<id_log>", methods=["GET"])
@inject
def get_log(id_log: int, repository: LogRepository = Provide[Container.log_repository]) -> tuple[Response, int]:

    log: Log = repository.get(id_log)

    if log is None : return jsonify([]), 200

    return jsonify(log.json()), 200