from flask import json
from werkzeug import Response
from werkzeug.exceptions import HTTPException


class ViWishException(HTTPException):
    code: int
    api_error_code: int
    api_error_event: str
    documentation: str
    description: str
    response: Response
    def __init__(
        self,
        code: int,
        api_error_code: int,
        api_error_event: str,
        documentation: str,
        description="User not found"
    ):
        self.code = code
        self.api_error_code = api_error_code
        self.api_error_event = api_error_event
        self.description = description
        self.response = Response(
            {
                json.dumps({
                    "code": code,
                    "api_error_code": api_error_code,
                    "api_error_event": api_error_event,
                    "documentation": documentation,
                    "description": description,
                }),
            },
            content_type="application/json",
        )
    pass