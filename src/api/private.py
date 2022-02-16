from ..services.private import Private
from ..models.private import (
    PrivateDetailUserResponseModel,
    PrivateCreateUserModel,
    PrivateUsersListResponseModel,
    PrivateUpdateUserModel
)
from ..models.other import CurrentUserResponseModel, Error_401
from ..core.exceptions import ErrorResponseModel
from ..services.auth import get_user_email

from fastapi import APIRouter, Depends, Response

router = APIRouter(
    prefix='/private',
    tags=['admin']
)

@router.get(
    '/users/', 
    response_model=PrivateUsersListResponseModel,
    responses = {
        400: {'model': ErrorResponseModel},
        401: {'model': str},
        403: {'model': str}

    }
)
def get_users(
    private: Private = Depends(),
    page: int = 0,
    size: int = 10,
    email: str = Depends(get_user_email),
):
    return private.get(page, size, email=email) 

@router.post(
    '/users', 
    response_model=PrivateDetailUserResponseModel,
    responses= {
        400: {'model': ErrorResponseModel},
        401: {'model': str},
        403: {'model': str}

    }
)
def create_user(
    create_user: PrivateCreateUserModel,
    email: str = Depends(get_user_email),
    private: Private = Depends()
):
    return private.create(create_user, email=email) 

@router.get(
    '/users/{pk}', 
    response_model=PrivateDetailUserResponseModel,
    responses= {
        400: {'model': ErrorResponseModel},
        401: {'model': str},
        403: {'model': str},
        404: {'model': str}
    }
)
def get_user_by_id(
    pk: int,
    email: str = Depends(get_user_email),
    private: Private = Depends()
):
    return private.get_user_by_id(pk, email=email) 


@router.delete(
    '/users/{pk}', 
    status_code=204, 
    response_class=Response,
    responses= {
        401: {'model': str},
        403: {'model': str},
        404: {'model': str}
    }
)
def delete_user(
    pk: int,
    email: str = Depends(get_user_email),
    private: Private = Depends(),
):
    private.delete_user_by_id(pk, email=email) 

@router.patch(
    '/users/{pk}', 
    response_model=PrivateDetailUserResponseModel,
    responses= {
        400: {'model': ErrorResponseModel},
        401: {'model': str},
        403: {'model': str},
        404: {'model': str}
    }
)
def update_user_by_id(
    pk: int,
    update_user: PrivateUpdateUserModel,
    email: str = Depends(get_user_email),
    private: Private = Depends()
):
    return private.update_user_by_id(pk, update_user, email=email) 


