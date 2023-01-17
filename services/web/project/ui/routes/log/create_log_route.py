from flask import Blueprint, request, json
from dependency_injector.wiring import inject, Provide
from werkzeug import Response

from project.application.log.create.create_log_command import CreateLogCommand
from project.application.log.create.create_log_commandHandler import CreateLogCommandHandler
from project.container import Container

blueprint = Blueprint('create_log_route', __name__)

@blueprint.route("/create", methods=["POST"])
@inject
def create_log(
     create_log_command_handler: CreateLogCommandHandler = Provide[Container.create_log_command_handler],
) -> [Response, int]:

    postRequest: dict = request.get_json()

    create_log_command = CreateLogCommand(
        postRequest['action_type'],
        postRequest['id_user'],
        postRequest['id_user_referred'],
        postRequest['description'],
    )

    create_log_command_handler.__call__(create_log_command)

    return Response(
        {
            json.dumps({
                "code": 201,
                "api_error_code": None,
                "api_error_event": None,
                "documentation": "https://viwish.atlassian.net/wiki/spaces/VIWISH/pages/262145/Create+Log",
                "description": "OK",
            }),
        },
        content_type="application/json",
    ), 201