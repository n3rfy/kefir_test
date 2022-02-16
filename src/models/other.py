from pydantic import BaseModel, EmailStr
from datetime import date

class PaginatedMetaDataModel(BaseModel):
    total: int
    page: int
    size: int

class LoginModel(BaseModel):
    email: str
    password: str

class CurrentUserResponseModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    is_admin: bool
    other_name: str
    phone: str
    birthday: date

class CitiesHintModel(BaseModel):
    id: int
    name: str


