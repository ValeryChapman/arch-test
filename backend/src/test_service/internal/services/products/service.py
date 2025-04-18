import csv
from io import StringIO

import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from core.settings.settings import settings
from internal.common.exceptions.fakestoreapi import RequestFailed
from internal.models import Product
from internal.repositories.products.abstract import ProductRepositoryAbstract
from internal.schemas.fakestoreapi.product import FakeStoreAPIProductSchema
from internal.services.products.abstract import ProductServiceAbstract


class ProductService(ProductServiceAbstract):
    def __init__(
        self,
        repository: ProductRepositoryAbstract,
        postgres_session: AsyncSession | Session,
    ):
        """
        Initializes the ProductService.

        :param repository: Product repository instance.
        :param postgres_session: Asynchronous Postgres session.
        """
        self.repository = repository
        self.postgres_session = postgres_session

    @staticmethod
    async def parse_products() -> list[FakeStoreAPIProductSchema]:
        """
        Fetches and parses products from the FakeStoreAPI.

        :return: List of products parsed into FakeStoreAPIProductSchema instances.
        :raises: aiohttp.ClientResponseError if the API response status is not successful.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    url=settings.fakeStoreAPI.products_url
                ) as response:
                    response.raise_for_status()
                    raw_products = await response.json()

            return [FakeStoreAPIProductSchema(**product) for product in raw_products]
        except Exception as exc:
            raise RequestFailed("Bad request to FakeStoreAPI", exc)

    async def bulk_insert(
        self, parsed_products: list[FakeStoreAPIProductSchema]
    ) -> list[Product]:
        """
        Inserts a list of parsed products into the database in bulk.

        :param parsed_products: List of parsed product data from FakeStoreAPI.
        :return: List of inserted Product instances.
        """
        if not parsed_products:
            return []

        return await self.repository.bulk_insert(
            postgres_session=self.postgres_session, parsed_products=parsed_products
        )

    async def get_by_price_range(
        self,
        min_price: float,
        max_price: float,
    ) -> list[Product]:
        """
        Retrieves products within the specified price range.

        :param min_price: Minimum price of products to fetch.
        :param max_price: Maximum price of products to fetch.
        :return: List of Product instances within the given price range.
        """
        return await self.repository.get_by_price_range(
            postgres_session=self.postgres_session,
            min_price=min_price,
            max_price=max_price,
        )

    @staticmethod
    async def process_csv(products: list[Product]) -> StringIO:
        """
        Converts a list of Product objects into CSV format.

        :param products: List of Product instances to be converted to CSV.
        :return: StringIO object containing the CSV data.
        """
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["id", "title", "price", "category"])

        for product in products:
            writer.writerow(
                [product.id, product.title, product.price, product.category]
            )

        output.seek(0)
        return output
