from ..core.settings import settings
from ..database import tables
from ..models.other import CurrentUserResponseModel

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from datetime import datetime, timedelta
from jose import jwt, JWTError 
from typing import Optional


def verify_password(password: str, hashed_password: str) -> bool:
    return check_password_hash(hashed_password, password)

def hash_password(password: str) -> str:
    return generate_password_hash(password)

def create_token(user: tables.User) -> str:
        user_data = CurrentUserResponseModel(**user.get_dict()).dict()
        user_data['birthday'] = str(user_data['birthday'])
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expires_s),
            'user': user_data
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        return token

def verify_token(token: str) -> Optional[dict]:
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            return None
        except:
            return None
            
        return payload.get('user')
