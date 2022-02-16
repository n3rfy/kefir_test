from ..services.private import Private
from ..models.private import (
    PrivateDetailUserResponseModel,
    PrivateCreateUserModel,
    PrivateUsersListResponseModel,
    PrivateUpdateUserModel
)
from ..core.exceptions import ErrorResponseModel
from ..services.auth import check_admin 

from fastapi import APIRouter, Depends, Response

router = APIRouter(
    prefix='/private',
    tags=['admin']
)

@router.post(
    '/users', 
    response_model=PrivateDetailUserResponseModel,
    responses= {
        400: {'model': ErrorResponseModel}
    }
)
def create_user(
    create_user: PrivateCreateUserModel,
    is_admin: bool = Depends(check_admin),
    private: Private = Depends()
):
    return private.create(create_user, is_admin) 

@router.post('/users/{pk}', response_model=PrivateDetailUserResponseModel)
def get_user_by_id(
    pk: int,
    is_admin: bool = Depends(check_admin),
    private: Private = Depends()
):
    return private.get_user_by_id(pk, is_admin) 

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
    is_admin: bool = Depends(check_admin),
):
    return private.get(page, size, is_admin) 

@router.delete('/users/{pk}', status_code=204, response_class=Response)
def delete_user(
    pk: int,
    is_admin: bool = Depends(check_admin),
    private: Private = Depends(),
):
    private.delete_user_by_id(pk, is_admin) 

@router.patch('/users/{pk}', response_model=PrivateDetailUserResponseModel)
def update_user_by_id(
    pk: int,
    update_user: PrivateUpdateUserModel,
    is_admin: bool = Depends(check_admin),
    private: Private = Depends()
):
    return private.update_user_by_id(pk, update_user, is_admin) 


