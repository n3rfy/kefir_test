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
from ..models.other import CurrentUserResponseModel
from ..core.exceptions import error
from ..core.secure import hash_password

from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

def permissions(fn):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if not user:
            raise HTTPException(
                status_code=401
            )        
        if not user.is_admin:
            raise HTTPException(
                status_code=403
            )
        return fn(*args, **kwargs)
    return wrapper


class Private:
    

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session 

    @error
    @permissions
    def create(
        self,
        create_user: PrivateCreateUserModel,
        user: CurrentUserResponseModel
    ) -> PrivateDetailUserResponseModel:
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
    
    @permissions
    def get_user_by_id(self,
        id: int,
        user: CurrentUserResponseModel
    ) -> PrivateDetailUserResponseModel:
        user = self._get_user_by_id(id, user=user)
        return PrivateDetailUserResponseModel(**user.get_dict())

    @error
    @permissions
    def get(
        self, 
        page: int,
        size: int,
        user: CurrentUserResponseModel
    ) -> PrivateUsersListResponseModel:
                     
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

    @permissions
    def delete_user_by_id(self, id: int, user: CurrentUserResponseModel):
        user = self._get_user_by_id(id, user=user)
        self.session.delete(user)
        self.session.commit()

    @error 
    @permissions
    def update_user_by_id(
        self,
        id: int,
        update_user: PrivateUpdateUserModel,
        user: CurrentUserResponseModel
    ) -> PrivateDetailUserResponseModel:
        user = self._get_user_by_id(id, user=user) 
        for key, value in update_user:
            setattr(user, key, value)
        self.session.commit()
        return PrivateDetailUserResponseModel(**user.get_dict())

    @permissions
    def _get_user_by_id(
        self, 
        id: int,
        user: CurrentUserResponseModel
    ) -> tables.User:
        if not user or not user.is_admin:
            raise HTTPException(
                status_code=401
            )        
        userx = self.session.query(tables.User).filter(tables.User.id==id).first()
        if not userx:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return userx
    
