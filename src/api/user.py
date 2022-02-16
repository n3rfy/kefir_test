from fastapi import APIRouter, Depends
from ..services.user import User

from ..models.user import (
    UsersListResponseModel,
)
from ..models.other import (
    CurrentUserResponseModel
)

router = APIRouter(
    prefix='/users',
    tags=['user']
)

@router.get('/current', response_model=CurrentUserResponseModel)
def get_current_user(
    user: User = Depends(),
    page: int = 0,
    size: int = 10
):
    return user.get(page, size) 

@router.get('/', response_model=UsersListResponseModel)
def get_users(
    user: User = Depends(),
    page: int = 0,
    size: int = 10
):
    return user.get(page, size) 

