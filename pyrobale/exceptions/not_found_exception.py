from .bale_exception import BaleException

class NotFoundException(BaleException):
    def __init__(self, message:str="Not Found!", code:int):
        super().__init__(
            name="NotFoundException",
            message=message,
            code=code
        )
