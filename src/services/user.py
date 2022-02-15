from ..database.database import get_session
from ..models.user import (
    UsersListResponseModel,
    UsersListElementModel
)
from ..database import tables

from fastapi import Depends
from sqlalchemy.orm import Session


class User:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session 

    def get(self, page: int, size: int) -> UsersListResponseModel:
        users = (
            self.session
            .query(tables.User)
            .limit(size)
            .offset(page*10)
            .all()
        )
        data = [ UsersListElementModel(**user.get_dict()) for user in users ]
        return UsersListResponseModel.convert(
            data=data,
            size=size,
            page=page,
            total=len(data)
)

