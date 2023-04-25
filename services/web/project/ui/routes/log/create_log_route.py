from flask import Blueprint, request, json
from dependency_injector.wiring import inject, Provide
from werkzeug import Response

from project.application.log.create.create_log_command import CreateLogCommand
from project.application.log.create.create_log_command_handler import CreateLogCommandHandler
from project.container import Container
from project.documentation_urls import DocumentationUrls
from project.infrastructure.validation.validation_rules.create_log_route_validation_rules import \
    CreateLogRouteValidationRules
from project.infrastructure.validation.validator import Validator

blueprint = Blueprint('create_log_route', __name__)

@blueprint.route("/create", methods=["POST"])
@inject
def create_log(
     create_log_command_handler: CreateLogCommandHandler = Provide[Container.create_log_command_handler],
) -> [Response, int]:

    post_request: dict = request.get_json()

    Validator.validate(
        json_to_validate=post_request,
        json_validation_rules=CreateLogRouteValidationRules
    )

    create_log_command = CreateLogCommand(
        post_request['action_type'],
        post_request['id_user'],
        post_request['id_user_referred'],
        post_request['description'],
    )

    create_log_command_handler.__call__(create_log_command)

    return Response(
        {
            json.dumps({
                "code": 201,
                "api_error_code": None,
                "api_error_event": None,
                "documentation": DocumentationUrls.url_create_log,
                "description": "OK",
            }),
        },
        content_type="application/json",
    ), 201