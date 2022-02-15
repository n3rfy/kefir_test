from fastapi import APIRouter, Depends
from ..services.private import Private

from ..models.private import (
    PrivateDetailUserResponseModel,
    PrivateCreateUserModel,
    PrivateUsersListResponseModel
)

router = APIRouter(
    prefix='/private',
    tags=['admin']
)

@router.post('/users', response_model=PrivateDetailUserResponseModel)
async def create_user(
    create_user: PrivateCreateUserModel,
    private: Private = Depends()
):
    return await private.create(create_user) 

@router.post('/users/{pk}', response_model=PrivateDetailUserResponseModel)
async def get_user_by_id(
    pk: int,
    private: Private = Depends()
):
    return await private.get_user_by_id(pk) 

@router.get('/users/', response_model=PrivateUsersListResponseModel)
async def get_users(
    private: Private = Depends(),
    page: int = 0,
    size: int = 10
):
    return await private.get_all(page, size) 

@router.delete('/users/{pk}', status_code=204)
async def delete_user(
    pk: int,
    private: Private = Depends(),
):
    await private.delete_user_by_id(pk) 


