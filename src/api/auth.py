from ..models.other import (
    LoginModel,
    CurrentUserResponseModel
)
from ..services.auth import Auth


from fastapi import APIRouter, Depends, Response 

router = APIRouter(
    tags=['auth']
)

@router.post('/login', response_model=CurrentUserResponseModel)
def login_user(
    auth_data: LoginModel,
    response: Response,
    auth: Auth = Depends(),
):
    token, model = auth.autheficate_user(auth_data) 
    response.set_cookie(
        key='access_token', 
        value=token, 
        httponly=True)
    return model 

@router.get('/logout', status_code=200)
def logout_user(response: Response):
    response.delete_cookie('access_token')

