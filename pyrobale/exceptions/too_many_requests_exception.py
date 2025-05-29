from .bale_exception import BaleException

class TooManyRequestsException(BaleException):
    def __init__(self, message:str="Too many requests", code:int):
        super().__init__(
            name="TooManyRequestsException",
            message=message,
            code=code
        )
