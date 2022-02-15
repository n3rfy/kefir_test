import sqlalchemy as sa
from .database import metadata

user = sa.Table(
    'users',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('first_name', sa.String),
    sa.Column('last_name', sa.String),
    sa.Column('email', sa.String, unique=True),
    sa.Column('is_admin', sa.Boolean),
    sa.Column('heshed_password', sa.String),
    sa.Column('other_name', sa.String, nullable=True),
    sa.Column('phone', sa.String, nullable=True),
    sa.Column('birthday', sa.Date, nullable=True),
    sa.Column('city', sa.Integer, nullable=True),
    sa.Column('additional_info', sa.String, nullable=True)
)

city = sa.Table(
    'city',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String)
)

