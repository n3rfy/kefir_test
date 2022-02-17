from .exc_class import ExceptionAll

from sqlalchemy.exc import IntegrityError
import functools

def error(fn):
    
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except IntegrityError as e:
            if 'UniqueViolation' in str(e) and 'email' in str(e):
                raise ExceptionAll(
                    status_code=400,
                    content = {'code':1, 'message':'email alredy taken'}
                )
            elif 'UniqueViolation' in str(e) and 'name' in str(e):
                raise ExceptionAll(
                    status_code=400,
                    content = {'code':2, 'message':'city alredy have'}
                )
            elif 'ForeignKeyViolation' in str(e) and '(id)=' in str(e):
                raise ExceptionAll(
                    status_code=400,
                    content = {
                        'code':3,
                        'message':"You can't delete a city! " + 
                                  "There is a user who is join with it"}
                )
            elif 'ForeignKeyViolation' in str(e) and '(city)=' in str(e):
                raise ExceptionAll(
                    status_code=400,
                    content = {'code':4, 'message':'city not found'}
                )
    return inner


