from ..services.private import Private
from ..models.private import (
    PrivateDetailUserResponseModel,
    PrivateCreateUserModel,
    PrivateUsersListResponseModel,
    PrivateUpdateUserModel
)

from fastapi import APIRouter, Depends, Response

router = APIRouter(
    prefix='/private',
    tags=['admin']
)

@router.post('/users', response_model=PrivateDetailUserResponseModel)
def create_user(
    create_user: PrivateCreateUserModel,
    private: Private = Depends()
):
    return private.create(create_user) 

@router.post('/users/{pk}', response_model=PrivateDetailUserResponseModel)
def get_user_by_id(
    pk: int,
    private: Private = Depends()
):
    return private.get_user_by_id(pk) 

@router.get('/users/', response_model=PrivateUsersListResponseModel)
def get_users(
    private: Private = Depends(),
    page: int = 0,
    size: int = 10
):
    return private.get(page, size) 

@router.delete('/users/{pk}', status_code=204, response_class=Response)
def delete_user(
    pk: int,
    private: Private = Depends(),
):
    private.delete_user_by_id(pk) 

@router.patch('/users/{pk}', response_model=PrivateDetailUserResponseModel)
def update_user_by_id(
    pk: int,
    update_user: PrivateUpdateUserModel,
    private: Private = Depends()
):
    return private.update_user_by_id(pk, update_user) 


