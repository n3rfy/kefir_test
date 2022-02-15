from pydantic.main import BaseModel
from .user import (
    UserBase, 
    UsersListElementModel
)
from .other import PaginatedMetaDataModel


class PrivateDetailUserResponseModel(UserBase):
    id: int

class PrivateCreateUserHesh(UserBase):
    heshed_password: str
    
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

