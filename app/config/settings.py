""" all fastapi settings goes here that are coming from .env file """

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """get the data from the .env file"""

    DB_URL: str = Field(validation_alias="DB_URL")
    DB_NAME: str = Field(validation_alias="DB_NAME")
    OPENAI_API_KEY: str = Field(validation_alias="OPENAI_API_KEY")
    PINECONE_API_KEY: str = Field(validation_alias="PINECONE_API_KEY")
    PINECONE_INDEX_NAME: str = Field(validation_alias="PINECONE_INDEX_NAME")
    SENDGRID_API: str = Field(validation_alias="SENDGRID_API")
    FROM_EMAIL: str = Field(validation_alias="FROM_EMAIL")
    class Config:
        env_file = ".env"


""" initialize the settings """
settings = Settings()
