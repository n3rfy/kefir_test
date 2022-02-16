from pydantic import BaseModel

class ExceptionAll(Exception):
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content

class ErrorResponseModel(BaseModel):
    code: int
    message: str

    class Config:
        schema_extra = {
            "example": {
                "code": 0,
                "message":"string"
            },
        }
