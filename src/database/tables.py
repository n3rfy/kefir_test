from sqlalchemy import (
    Column,
    Date,
    Integer,
    String,
    ForeignKey,
    Boolean
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    is_admin = Column(Boolean)
    password_hash = Column(String)
    other_name = Column(String)
    phone = Column(String)
    birthday = Column(Date)
    city = Column(Integer, ForeignKey('city.id'), index=True)
    additional_info = Column(String)

    def get_dict(self):
        dict_t = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return dict_t


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def get_dict(self):
        dict_t = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return dict_t

