from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# Classe para configurar as configurações
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Configurações do projeto
    PROJECT_NAME: str = "Pizzaria API"
    VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1" 
    DEBUG: bool = True

    # configuraões do banco de dados
    DATABASE_URL: str = Field(init=False)
    SECRET_KEY: str = Field(init=False)


settings = Settings()