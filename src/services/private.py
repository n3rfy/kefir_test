from ..database.database import get_session 
from ..database import tables
from ..models.private import ( 
    PrivateCreateUserModel, 
    PrivateDetailUserResponseModel,
    PrivateUsersListResponseModel,
    PrivateUpdateUserModel,
    CitiesHintModel
)
from ..models.user import (
    UsersListElementModel
)
from ..core.exceptions import error

from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException


class Private:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session 

    @error
    def create(
        self,
        create_user: PrivateCreateUserModel
    ) -> PrivateDetailUserResponseModel:
        user = tables.User(
            first_name = create_user.first_name,
            last_name = create_user.last_name,
            email = create_user.email,
            is_admin = create_user.is_admin,
            password_hash = create_user.password + '123',
            other_name = create_user.other_name,
            phone = create_user.phone,
            birthday = create_user.birthday,
            city = create_user.city,
            additional_info = create_user.additional_info,
        )
        self.session.add(user)
        self.session.commit()
        return PrivateDetailUserResponseModel(**user.get_dict())

    def get_user_by_id(
        self,
        id: int
    ) -> PrivateDetailUserResponseModel:
        user = self._get_user_by_id(id)
        return PrivateDetailUserResponseModel(**user.get_dict())

    def get(self, page: int, size: int) -> PrivateUsersListResponseModel:
        users = self.session.query(tables.User).limit(size).offset(page*10).all()
        citys = self.session.query(tables.City).all()
        data = [ UsersListElementModel(**user.get_dict()) for user in users ]
        citys = [ CitiesHintModel(**city.get_dict()) for city in citys ] 
        return PrivateUsersListResponseModel.convert(
            data=data,
            page=page,
            size=size,
            total=len(data),
            citys=citys
        )

    def delete_user_by_id(self, id: int):
        user = self._get_user_by_id(id)
        self.session.delete(user)
        self.session.commit()
         
    def update_user_by_id(
        self,
        id: int,
        update_user: PrivateUpdateUserModel
    ) -> PrivateDetailUserResponseModel:
        user = self._get_user_by_id(id) 
        for key, value in update_user:
            setattr(user, key, value)
        self.session.commit()
        return PrivateDetailUserResponseModel(**user.get_dict())

    def _get_user_by_id(self, id: int) -> tables.User:
        user = self.session.query(tables.User).filter(tables.User.id==id).first()
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return user
    
