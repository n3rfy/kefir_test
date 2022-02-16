from sqlalchemy.exc import IntegrityError, DataError
from pydantic import BaseModel
from fastapi import HTTPException

import functools

def error(fn):
    
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except IntegrityError as e:
            if 'UniqueViolation' in str(e):
                raise HTTPException(
                    status_code=400, 
                    detail={
                        'code':0,
                        'message':'email alredy taken'
                    }
                )
                
            elif 'ForeignKeyViolation' in str(e):
                raise HTTPException(
                    400,
                    detail={
                        'code':0,
                        'message':'city not found'
                    }
                )
        except DataError as e:
            if 'LIMIT must not be negative' in str(e):
                raise HTTPException(
                    400,
                    detail={
                        'code':0,
                        'message':'size must not be negative'
                    }
                )
            elif 'OFFSET must not be negative' in str(e):
                raise HTTPException(
                    400,
                    detail={
                        'code':0,
                        'message':'page must not be negative'
                    }
                )



    return inner

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


