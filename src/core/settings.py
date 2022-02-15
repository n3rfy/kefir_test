from pydantic import BaseSettings

class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = ''

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
 
settings = Settings()
