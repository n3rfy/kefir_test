from ..models.other import LoginModel,CurrentUserResponseModel
from ..core.secure import create_token, verify_password, verify_token
from ..database import tables
from ..database.database import get_session

from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, status, Cookie
from typing import Optional


def check_admin(access_token: Optional[str] = Cookie(None)) -> Optional[bool]:
    if access_token:
        is_admin = verify_token(access_token)
        return is_admin
    return None

class Auth:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session 

    def autheficate_user(self, login_data: LoginModel):
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
        user = (
            self.session
            .query(tables.User)
            .filter(tables.User.email==login_data.email)
            .first()
        )
        if not user:
            raise exception
        if not verify_password(login_data.password, user.password_hash):
            raise exception
        token = create_token(user)
        return token, CurrentUserResponseModel(**user.get_dict())

    
