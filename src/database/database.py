from databases import Database
from sqlalchemy import create_engine, MetaData

from ..core.settings import settings 

metadata = MetaData()
database = Database(settings.database_url)
engine = create_engine(
    settings.database_url
)


def get_database() -> Database:
    return database
