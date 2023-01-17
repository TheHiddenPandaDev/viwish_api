from flask import json
from werkzeug import Response
from werkzeug.exceptions import HTTPException


class ViWishException(HTTPException):
    code: int
    api_error_code: int
    documentation: str
    description: str
    response: Response
    def __init__(
        self,
        code: int,
        api_error_code: int,
        documentation: str,
        description="User not found"
    ):
        self.code = code
        self.api_error_code = api_error_code
        self.description = description
        self.response = Response(
            {
                json.dumps({
                    "code": code,
                    "api_error_code": api_error_code,
                    "documentation": documentation,
                    "description": description,
                }),
            },
            content_type="application/json",
        )
    pass