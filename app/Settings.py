from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    redis_url: str
    rate_limit: int
    time_window: int
    secret_key: str = Field(alias="jwt_secret")
    algorithm: str = Field(alias="jwt_algorithm")
    access_token_expire_minutes: int = Field(alias="jwt_access_token_expire_minutes")
    db_user: str = Field(alias="db_user")
    db_password: str = Field(alias="db_password")
    db_host: str = Field(alias="db_host")
    db_port: int = Field(alias="db_port")
    db_name: str = Field(alias="db_name")

    @property
    def db_url(self):
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}" f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )
