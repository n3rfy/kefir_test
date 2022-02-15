from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    is_admin: bool
    heshed_password: str
    other_name: Optional[str] = None
    phone: Optional[str] = None
    birthday:Optional[date] = None
    city: Optional[int] = None
    additional_info: Optional[str] = None



