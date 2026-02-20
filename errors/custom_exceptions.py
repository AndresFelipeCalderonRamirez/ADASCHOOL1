class BaseAppException(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class ValidationException(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, 400)


class InternalException(BaseAppException):
    def __init__(self, message: str = "Internal Server Error"):
        super().__init__(message, 500)