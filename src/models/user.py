from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr

from .other import PaginatedMetaDataModel

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

class UsersListMetaDataModel(BaseModel):
    pagination: PaginatedMetaDataModel

class UsersListResponseModel(BaseModel):
    data: list[UsersListElementModel]
    meta: UsersListMetaDataModel
    
    @staticmethod
    def convert(data, size, page, total):
        return UsersListResponseModel(
            data = data,
            meta = UsersListMetaDataModel(
                pagination=PaginatedMetaDataModel(
                    total=total,
                    page=page,
                    size=size
                )
            )
        )

class UpdateUserModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    other_name: Optional[str]
    phone: Optional[str]
    birthday:Optional[date]

class UpdateUserResponseModel(UpdateUserModel):
    id: int 
