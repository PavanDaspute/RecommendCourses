import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pydantic_settings import BaseSettings

env_path = Path(".") /".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):

    #Database
    DATABASE_URL: str = 'sqlite:///C:/Users/PAVAN/OneDrive/Desktop/python programs/user_auth/user_auth/Fast_api_auth/demo.db'

    # JWT
    JWT_SECRET: str = os.getenv('JWT_SECRET', 'dummy_jwt_secret_1234567890')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM', 'HS256')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('JWT_TOKEN_EXPIRE_MINUTES', 60)
def get_settings() -> Settings:
    return Settings()

