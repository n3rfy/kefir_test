from .tables import user, city
from .database import metadata, engine

metadata.create_all(engine)
