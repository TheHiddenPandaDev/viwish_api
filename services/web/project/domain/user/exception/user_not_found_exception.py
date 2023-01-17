from project.domain.viwish_exception import ViWishException


class UserNotNotFoundException(ViWishException):
    code: int
    api_error_code: int
    documentation: str
    description: str
    def __init__(
        self,
        code: int,
        api_error_code: int,
        documentation: str,
        description="User not found"
    ):
        self.code = code
        self.api_error_code = api_error_code
        self.documentation = documentation
        self.description = description
        super().__init__(
            code=code,
            api_error_code=api_error_code,
            documentation=documentation,
            description=description,
        )
    pass