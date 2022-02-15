from .user import (
    UserBase, 
    UsersListElementModel
)
from .other import PaginatedMetaDataModel

from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional


class PrivateDetailUserResponseModel(UserBase):
    id: int

class PrivateCreateUserHesh(UserBase):
    heshed_password: str
    
class PrivateUpdateUserModel(BaseModel):
    first_name: str 
    last_name: str
    email: EmailStr
    is_admin: bool
    other_name: Optional[str] 
    phone: Optional[str]
    birthday:Optional[date]
    city: Optional[int]
    additional_info: Optional[str]


class PrivateCreateUserModel(UserBase):
    password: str

    def get_heshed(self):
        return PrivateCreateUserHesh(
            heshed_password=self.password + '123',
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            is_admin=self.is_admin,
            other_name=self.other_name,
            phone=self.phone,
            birthday=self.birthday,
            city=self.city,
            additional_info=self.additional_info
        )

class CitiesHintModel(BaseModel):
    id: int
    name: str

class PrivateUsersListHintMetaModel(BaseModel):
    city: list[CitiesHintModel]

class PrivateUsersListMetaDataModel(BaseModel):
    pagination: PaginatedMetaDataModel
    hint: PrivateUsersListHintMetaModel

class PrivateUsersListResponseModel(BaseModel):
    data: list[UsersListElementModel]
    meta: PrivateUsersListMetaDataModel
    
    @staticmethod
    def convert(data, page, size, total, citys):
        return PrivateUsersListResponseModel(
            data = data,
            meta = PrivateUsersListMetaDataModel(
                pagination = PaginatedMetaDataModel(
                    size = size,
                    page = page,
                    total = total
                ),
                hint = PrivateUsersListHintMetaModel(
                    city = citys
                )

            )
        )
