from pydantic import BaseModel

class PaginatedMetaDataModel(BaseModel):
    total: int
    page: int
    size: int

