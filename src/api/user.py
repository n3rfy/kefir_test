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
from pydantic import conint
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
    description='Краткая информация о всех пользователях (user)<br>'+ 
                'page > 0<br>0 < size < 11 ',
    responses = {
        400: {'model': ErrorResponseModel},
        401: {'model': str}
    }
)
def get_users(
    page: conint(gt=-1) = 0,
    size: conint(gt=0, lt=11) = 10,
    user_service: User = Depends(),
    email: str = Depends(get_user_email),
):
    return user_service.get(page, size, email=email) 

@router.patch(
    '/', 
    response_model=UpdateUserResponseModel,
    description='Изменение своих данных (user)<br>'+
                'Сбрасываются куки нужен релогин!',
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

