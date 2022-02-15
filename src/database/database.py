from databases import Database
from sqlalchemy import create_engine

from ..core.settings import settings 

database = Database(settings.database_url)
engine = create_engine(
    settings.database_url
)
