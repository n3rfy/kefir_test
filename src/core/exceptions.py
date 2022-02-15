from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import functools

def error(fn):
    
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except IntegrityError:
            raise HTTPException(status_code=400, detail = {
                'code':0,
                'message': 'email alredy taken'
            })

    return inner

