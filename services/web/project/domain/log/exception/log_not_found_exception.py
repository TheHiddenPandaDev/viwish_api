from project.domain.viwish_exception import ViWishException

class LogNotNotFoundException(ViWishException):
    code: int
    api_error_code: int
    api_error_event: str
    documentation: str
    description: str
    def __init__(
        self,
        code: int,
        api_error_code: int,
        api_error_event: str,
        documentation: str,
        description="Log not found"
    ):
        self.code = code
        self.api_error_code = api_error_code
        self.api_error_event = api_error_event
        self.documentation = documentation
        self.description = description
        super().__init__(
            code=code,
            api_error_code=api_error_code,
            api_error_event=api_error_event,
            documentation=documentation,
            description=description,
        )
    pass