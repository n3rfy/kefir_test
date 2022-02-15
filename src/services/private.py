from ..database.tables import user
from ..database.database import get_database
from ..models.private import (
    PrivateCreateUserModel,
    PrivateDetailUserResponseModel,
    PrivateUsersListResponseModel,
    PrivateUsersListHintMetaModel,
    CitiesHintModel
)
from ..models.other import PaginatedMetaDataModel

from databases import Database
from fastapi import Depends, status, HTTPException


class Private:
    def __init__(self, database: Database = Depends(get_database)):
        self.database = database

    async def create(
        self,
        create_user: PrivateCreateUserModel
    ) -> PrivateDetailUserResponseModel:
        heshed_user = create_user.get_heshed() 
        query = user.insert().values(**heshed_user.dict())
        return PrivateDetailUserResponseModel(
            id = await self.database.execute(query),
            **heshed_user.dict()
        )

    async def get_user_by_id(
        self,
        pk: int
    ) -> PrivateDetailUserResponseModel:
        query = user.select().where(user.c.id==pk)
        userx = await self.database.fetch_one(query)
        if userx is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return PrivateDetailUserResponseModel.parse_obj(userx)

    async def get_all(
        self,
        page: int, 
        size: int
    ) -> PrivateUsersListResponseModel:
        query = user.select().limit(size).offset(page*10)
        users = await self.database.fetch_all(query)
        return PrivateUsersListResponseModel(
            data=users,
            meta={
                'pagination': PaginatedMetaDataModel(
                    total=len(users),
                    page=page,
                    size=size),
                'hint': PrivateUsersListHintMetaModel(
                    city = [
                        CitiesHintModel(id = 0,name ='moskow'),
                    ] 
                )

            }
        )
    
    async def delete_user_by_id(
        self,
        pk: int
    ):
        await self.get_user_by_id(pk)
        query = user.delete().where(user.c.id==pk)
        await self.database.execute(query)
