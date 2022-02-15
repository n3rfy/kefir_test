from fastapi import APIRouter, Depends
from ..services.private import Private

from ..models.private import (
    PrivateDetailUserResponseModel,
    PrivateCreateUserModel
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
async def get_user(
    pk: int,
    private: Private = Depends()
):
    return await private.get_user_by_id(pk) 
