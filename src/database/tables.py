import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    email = sa.Column(sa.String, unique=True)
    is_admin = sa.Column(sa.Boolean)
    heshed_password = sa.Column(sa.String)
    other_name = sa.Column(sa.String, nullable=True)
    phone = sa.Column(sa.String, nullable=True)
    birthday = sa.Column(sa.Date, nullable=True)
    city = sa.Column(sa.Integer, sa.ForeignKey('city.id'), nullable=True)
    additional_info = sa.Column(sa.String, nullable=True)

class City(Base):
    __tablename__ = 'city'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, unique=True)
 

