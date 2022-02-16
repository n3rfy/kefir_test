from ..services.private import Private
from ..models.private import (
    PrivateDetailUserResponseModel,
    PrivateCreateUserModel,
    PrivateUsersListResponseModel,
    PrivateUpdateUserModel
)
from ..models.other import CurrentUserResponseModel
from ..core.exceptions import ErrorResponseModel
from ..services.auth import get_user

from fastapi import APIRouter, Depends, Response

router = APIRouter(
    prefix='/private',
    tags=['admin']
)

@router.get(
    '/users/', 
    response_model=PrivateUsersListResponseModel,
    responses = {
        400: {'model': ErrorResponseModel}
    }
)
def get_users(
    private: Private = Depends(),
    page: int = 0,
    size: int = 10,
    user: CurrentUserResponseModel = Depends(get_user),
):
    return private.get(page, size, user=user) 

@router.post(
    '/users', 
    response_model=PrivateDetailUserResponseModel,
    responses= {
        400: {'model': ErrorResponseModel}
    }
)
def create_user(
    create_user: PrivateCreateUserModel,
    user: CurrentUserResponseModel = Depends(get_user),
    private: Private = Depends()
):
    return private.create(create_user, user=user) 

@router.get('/users/{pk}', response_model=PrivateDetailUserResponseModel)
def get_user_by_id(
    pk: int,
    user: CurrentUserResponseModel = Depends(get_user),
    private: Private = Depends()
):
    return private.get_user_by_id(pk, user=user) 


@router.delete('/users/{pk}', status_code=204, response_class=Response)
def delete_user(
    pk: int,
    user: CurrentUserResponseModel = Depends(get_user),
    private: Private = Depends(),
):
    private.delete_user_by_id(pk, user=user) 

@router.patch('/users/{pk}', response_model=PrivateDetailUserResponseModel)
def update_user_by_id(
    pk: int,
    update_user: PrivateUpdateUserModel,
    user: CurrentUserResponseModel = Depends(get_user),
    private: Private = Depends()
):
    return private.update_user_by_id(pk, update_user, user=user) 


