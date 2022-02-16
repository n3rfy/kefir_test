from ..services.auth import get_user_email
from ..core.exc_class import ErrorResponseModel
from ..services.user import User
from ..models.user import (
    UsersListResponseModel,
    UpdateUserModel,
    UpdateUserResponseModel
)
from ..models.other import (
    CurrentUserResponseModel
)

from fastapi import APIRouter, Depends, Response

router = APIRouter(
    prefix='/users',
    tags=['user']
)

@router.get(
    '/current', 
    response_model=CurrentUserResponseModel,
    description='Информация о текущем пользователе (user)',
    responses = {
        400: {'model': ErrorResponseModel},
        401: {'model': str}
    }
)
def get_current_user(
    user_service: User = Depends(),
    email: str = Depends(get_user_email),
):
    return user_service.get_current_user(email=email) 

@router.get(
    '/',
    response_model=UsersListResponseModel,
    description='Краткая информация о всех пользователях (user)',
    responses = {
        400: {'model': ErrorResponseModel},
        401: {'model': str}
    }
)
def get_users(
    user_service: User = Depends(),
    page: int = 0,
    size: int = 10,
    email: str = Depends(get_user_email),
):
    return user_service.get(page, size, email=email) 

@router.patch(
    '/', 
    response_model=UpdateUserResponseModel,
    description='Изменение своих данных (user)',
    responses = {
        400: {'model': ErrorResponseModel},
        401: {'model': str}
    }
)
def update_current_user(
    response: Response,
    update_user: UpdateUserModel,
    user_service: User = Depends(),
    email: str = Depends(get_user_email)
):
    response.delete_cookie('access_token')
    return user_service.update_user(update_user, email=email) 

