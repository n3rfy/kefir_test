from ..database.database import get_session
from ..models.user import (
    UsersListResponseModel,
    UsersListElementModel,
    UpdateUserModel,
    UpdateUserResponseModel
)
from ..core.exceptions import error
from ..models.other import CurrentUserResponseModel
from ..database import tables

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

class User:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session 

    def permissions(self, email):
        if email is None:
            raise HTTPException(
                status_code=401
            )

    @error
    def get(self, page: int, size: int,email: str) -> UsersListResponseModel:
        self.permissions(email)
        users = self.session.query(tables.User).limit(size).offset(page*10).all()
        data = [ UsersListElementModel(**user.get_dict()) for user in users ]
        return UsersListResponseModel.convert(
            data=data,
            size=size,
            page=page,
            total=len(data)
        )

    def get_current_user(
        self, 
        email: str
    ) -> CurrentUserResponseModel:
        self.permissions(email)
        user = CurrentUserResponseModel(
            **self._get_user_by_email(email).get_dict()
        )
        return user

    @error
    def update_user(
        self,
        update_user: UpdateUserModel,
        email: str
    ) -> UpdateUserResponseModel:
        self.permissions(email)
        user = self._get_user_by_email(email) 
        for key, value in update_user:
            setattr(user, key, value)
        self.session.commit()
        return UpdateUserResponseModel(**user.get_dict())



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
        
