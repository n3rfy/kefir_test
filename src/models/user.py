from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    is_admin: bool
    other_name: Optional[str] = None
    phone: Optional[str] = None
    birthday:Optional[date] = None
    city: Optional[int] = None
    additional_info: Optional[str] = None

    
class UsersListElementModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr

