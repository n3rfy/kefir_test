from ..database.tables import user
from ..database.database import get_database
from ..models.other import PaginatedMetaDataModel
from ..models.user import (
    UsersListResponseModel,
)

from databases import Database
from fastapi import Depends


class User:
    def __init__(self, database: Database = Depends(get_database)):
        self.database = database
    async def get_all(
        self,
        page: int, 
        size: int
    ) -> UsersListResponseModel:
        query = user.select().limit(size).offset(page*10)
        users = await self.database.fetch_all(query)
        return UsersListResponseModel(
            data=users,
            meta={
                'pagination': PaginatedMetaDataModel(
                    total=len(users),
                    page=page,
                    size=size
                )
            }
        )
    

