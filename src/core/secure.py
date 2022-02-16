from ..core.settings import settings

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

def create_token(email: str) -> str:
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expires_s),
            'email': str(email)
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        return token

def verify_token(token: str) -> Optional[str]:
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
            
        return payload.get('email')
