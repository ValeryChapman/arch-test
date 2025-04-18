from pydantic import Field
from pydantic_settings import BaseSettings


class AuthorizationConfig(BaseSettings):
    """AuthorizationConfig holds the configuration for authorization tokens."""

    api_key: str = Field("...", alias="TEST_SERVICE_API_KEY")


class PostgresConfig(BaseSettings):
    """PostgresConfig holds the configuration for PostgreSQL database."""

    async_url: str = Field("...", alias="POSTGRES_URL_ASYNC")


class FakeStoreAPIConfig(BaseSettings):
    """FakeStoreAPIConfig holds the configuration for FakeStoreAPI service."""

    products_url: str = "https://fakestoreapi.com/products"


class ServiceConfig(BaseSettings):
    """ServiceConfig is the main class that holds all the configuration values for the application."""

    authorization: AuthorizationConfig = AuthorizationConfig.model_validate({})
    postgres: PostgresConfig = PostgresConfig.model_validate({})
    fakeStoreAPI: FakeStoreAPIConfig = FakeStoreAPIConfig.model_validate({})


settings: ServiceConfig = ServiceConfig.model_validate({})
