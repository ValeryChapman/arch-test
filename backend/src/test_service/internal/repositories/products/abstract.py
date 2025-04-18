from abc import abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from internal.models import Product
from internal.schemas.fakestoreapi.product import FakeStoreAPIProductSchema


class ProductRepositoryAbstract:
    @abstractmethod
    async def bulk_insert(
        self,
        postgres_session: AsyncSession,
        parsed_products: list[FakeStoreAPIProductSchema],
    ) -> list[Product]:
        """
        Bulk inserts parsed products into the database.

        :param postgres_session: Async SQLAlchemy session for executing the insert.
        :param parsed_products: List of parsed product schemas to insert.
        :return: List of inserted Product instances.
        """

    @abstractmethod
    async def get_by_price_range(
        self,
        postgres_session: AsyncSession,
        min_price: float,
        max_price: float,
    ) -> list[Product]:
        """
        Retrieves products within the specified price range.

        :param postgres_session: Asynchronous Postgres session.
        :param min_price: Minimum price of products to fetch.
        :param max_price: Maximum price of products to fetch.
        :return: List of Product instances within the given price range.
        """
