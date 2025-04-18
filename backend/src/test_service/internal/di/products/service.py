from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.postgres.async_session import get_async_postgres_session
from internal.di.products.repository import get_product_repository
from internal.repositories.products.abstract import ProductRepositoryAbstract
from internal.services.products.abstract import ProductServiceAbstract
from internal.services.products.service import ProductService


def get_product_service(
    product_repository: Annotated[
        ProductRepositoryAbstract, Depends(get_product_repository)
    ],
    postgres_session: Annotated[AsyncSession, Depends(get_async_postgres_session)],
) -> ProductServiceAbstract:
    """
    Returns an instance of the product service.

    :param product_repository: Dependency-injected ProductRepository instance.
    :param postgres_session: Dependency-injected asynchronous PostgreSQL session.
    :return: Instance of ProductServiceAbstract.
    """
    return ProductService(
        repository=product_repository, postgres_session=postgres_session
    )
