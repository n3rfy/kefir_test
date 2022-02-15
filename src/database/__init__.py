from .tables import (
    User,
    City,
    Base
)
from .database import engine


Base.metadata.create_all(engine)
