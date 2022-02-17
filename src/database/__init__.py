from .tables import (
    User,
    City,
    Base
)
from .database import engine, Session
from ..core.secure import generate_password_hash
from ..core.settings import settings

Base.metadata.create_all(engine)
session = Session()
user = tables.User(
    first_name = 'admin',
    last_name = 'admin',
    email = 'admin@admin.com',
    is_admin = True,
    password_hash = generate_password_hash(settings.admin_password)
)
try:
    session.add(user)
    session.commit()
except Exception:
    pass
session.close()
