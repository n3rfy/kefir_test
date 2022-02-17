from ..services.private import Private
from ..models.private import (
    PrivateDetailUserResponseModel,
    PrivateCreateUserModel,
    PrivateUsersListResponseModel,
    PrivateUpdateUserModel
)
from ..models.other import CitiesHintModel, CitiesCreate
from ..core.exc_class import ErrorResponseModel
from ..services.auth import get_user_email

from fastapi import APIRouter, Depends, Response
from pydantic import conint

router = APIRouter(
    prefix='/private',
    tags=['admin']
)

@router.get(
    '/users/', 
    response_model=PrivateUsersListResponseModel,
    description='Краткая информация (включая city) о всех пользователях (admin)',
    responses = {
        400: {'model': ErrorResponseModel},
        401: {'model': str},
        403: {'model': str}
    }
)
def get_users(
    page: conint(gt=-1) = 0,
    size: conint(gt=0,lt=11) = 10,
    private: Private = Depends(),
    email: str = Depends(get_user_email)
):
    return private.get(page, size, email=email) 

@router.post(
    '/users', 
    response_model=PrivateDetailUserResponseModel,
    description='Добавление нового пользователя (admin)',
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
    description='Полная информация о пользователе (admin)',
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
    description='Удаление пользователя (admin)',
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
    description='Изменение данных любого пользователя (admin)',
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

@router.post(
    '/city', 
    response_model=CitiesHintModel,
    description='Добавление нового города (admin)',
    responses= {
        400: {'model': ErrorResponseModel},
        401: {'model': str},
        403: {'model': str}
    }
)
def create_city(
    city: CitiesCreate,
    email: str = Depends(get_user_email),
    private: Private = Depends()
):
    return private.create_city(city, email=email) 

@router.delete(
    '/city/{pk}', 
    status_code=204, 
    description='Удаление города (admin)',
    response_class=Response,
    responses= {
        401: {'model': str},
        403: {'model': str},
        404: {'model': str}
    }
)
def delete_city(
    pk: int,
    email: str = Depends(get_user_email),
    private: Private = Depends(),
):
    private.delete_city_by_id(pk, email=email) 
