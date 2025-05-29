from .bale_exception import BaleException

class ForbiddenException(BaleException):
    def __init__(self, message:str, code:int):
        super().__init__(
            name="ForbiddenException",
            message=message,
            code=code
        )
