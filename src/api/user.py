from fastapi import APIRouter, Depends
from ..services.user import User

from ..models.user import (
    UsersListResponseModel,
)

router = APIRouter(
    prefix='/users',
    tags=['user']
)

@router.get('/', response_model=UsersListResponseModel)
async def get_users(
    user: User = Depends(),
    page: int = 0,
    size: int = 10
):
    return await user.get_all(page, size) 


