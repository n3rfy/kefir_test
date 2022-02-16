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
from ..core.secure import hash_password

from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException


class Private:
      
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session 

    def permissions(self, email):
        if email is None:
            raise HTTPException(
                status_code=401
            )
        user = self._get_user_by_email(email)
        if not user.is_admin:
            raise HTTPException(
                status_code=403
            )

    @error
    def create(
        self,
        create_user: PrivateCreateUserModel,
        email: str
    ) -> PrivateDetailUserResponseModel:
        self.permissions(email)
        user_dict = create_user.dict()
        password = hash_password(user_dict['password'])
        del user_dict['password']
        user = tables.User(
            password_hash = password,
            **user_dict
            )
        self.session.add(user)
        self.session.commit()
        return PrivateDetailUserResponseModel(**user.get_dict())
    
    def get_user_by_id(self,
        id: int,
        email: str
    ) -> PrivateDetailUserResponseModel:
        self.permissions(email)
        user = self._get_user_by_id(id)
        return PrivateDetailUserResponseModel(**user.get_dict())

    @error
    def get(
        self, 
        page: int,
        size: int,
        email: str
    ) -> PrivateUsersListResponseModel:
                     
        self.permissions(email)
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

    def delete_user_by_id(self, id: int, email: str):
        self.permissions(email)
        user = self._get_user_by_id(id)
        self.session.delete(user)
        self.session.commit()

    @error 
    def update_user_by_id(
        self,
        id: int,
        update_user: PrivateUpdateUserModel,
        email: str
    ) -> PrivateDetailUserResponseModel:
        self.permissions(email)
        user = self._get_user_by_id(id) 
        for key, value in update_user:
            setattr(user, key, value)
        self.session.commit()
        return PrivateDetailUserResponseModel(**user.get_dict())

    def _get_user_by_id(
        self, 
        id: int,
    ) -> tables.User:
        userx = self.session.query(tables.User).filter(tables.User.id==id).first()
        if not userx:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return userx

    def _get_user_by_email(
        self, 
        email: str
    ) -> tables.User:
        userx = self.session.query(tables.User).filter(
            tables.User.email==email
        ).first()
        if not userx:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return userx
    
