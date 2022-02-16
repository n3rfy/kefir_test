from pydantic import BaseSettings

class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = ''

    jwt_secret: str = ''
    jwt_algorithm: str = 'HS256'
    jwt_expires_s: int = 3600

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
 
settings = Settings()
