
from app.core.rcode import ResponseModel

class CustomException(Exception):
    def __init__(self, err: ResponseModel):
        self.err = err
    def toJson(self):
        return {
            "code": self.err.code,
            "msg": self.err.msg
        }