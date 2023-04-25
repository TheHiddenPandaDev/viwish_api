from project.api_errors import ApiErrors
from project.documentation_urls import DocumentationUrls
from project.infrastructure.validation.abstract_validation_rules import AbstractValidationRules


class CreateLogRouteValidationRules(AbstractValidationRules):

    schema: dict = {
        "type": "object",
        "properties": {
            "action_type": {"type": "string"},
            "id_user": {"type": "number"},
            "id_user_referred": {"type": "number"},
            "description": {"type": "string"},
        },
        "required": ["action_type"],
    }
    http_error_code: int = 400
    api_error_code: int = ApiErrors.table_log_unexpected_error['code']
    api_error_event: str = ApiErrors.table_log_unexpected_error['event']
    documentation: str = DocumentationUrls.url_create_log
