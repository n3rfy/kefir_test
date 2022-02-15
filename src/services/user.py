from ..database.tables import user
from ..database.database import get_database
from ..models.user import (
    UsersListElementModel,
)

from typing import List
from databases import Database
from fastapi import Depends


class User:
    def __init__(self, database: Database = Depends(get_database)):
        self.database = database
    async def get_all(
        self,
        page: int, 
        size: int
    ) -> List[UsersListElementModel]:
        query = user.select().limit(size).offset(page*10)
        return await self.database.fetch_all(query)
    

