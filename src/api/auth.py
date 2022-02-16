from ..models.other import (
    LoginModel,
    CurrentUserResponseModel
)
from ..core.exc_class import ErrorResponseModel
from ..services.auth import Auth

from fastapi import APIRouter, Depends, Response 

router = APIRouter(
    tags=['auth']
)

@router.post(
    '/login', 
    response_model=CurrentUserResponseModel,
    description='Аунтификация по email и password. Выдача cookies',
    responses = {
        400: {'model': ErrorResponseModel}
    }
)
def login_user(
    auth_data: LoginModel,
    response: Response,
    auth: Auth = Depends(),
):
    token, model = auth.autheficate_user(auth_data) 
    response.set_cookie(key='access_token', value=token, httponly=True)
    return model 

@router.get(
    '/logout', 
    status_code=200, 
    description='Выход из сессии. Удаление cookies'
)
def logout_user(response: Response):
    response.delete_cookie('access_token')

