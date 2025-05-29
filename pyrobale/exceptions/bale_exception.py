class BaleException(Exception):
    def __init__(self, name:str="BaleException", message:str=None, code:int=None):
        self.name = name
        self.message = message
        self.code = code
        super().__init__(str(self))
    def __str__(self):
        code = "" if code is None else self.code
        message = "" if code is None else self.message
        error_msg = f"{self.name} {code}: {message}"
        return error_msg
        
