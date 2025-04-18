from abc import abstractmethod
from io import StringIO

from internal.models import Product
from internal.schemas.fakestoreapi.product import FakeStoreAPIProductSchema


class ProductServiceAbstract:
    @staticmethod
    @abstractmethod
    async def parse_products() -> list[FakeStoreAPIProductSchema]:
        """
        Fetches and parses products from the FakeStoreAPI.

        :return: List of products parsed into FakeStoreAPIProductSchema instances.
        :raises: aiohttp.ClientResponseError if the API response status is not successful.
        """

    @abstractmethod
    async def bulk_insert(
        self, parsed_products: list[FakeStoreAPIProductSchema]
    ) -> list[Product]:
        """
        Inserts a list of parsed products into the database in bulk.

        :param parsed_products: List of parsed product data from FakeStoreAPI.
        :return: List of inserted Product instances.
        """

    @abstractmethod
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

    @staticmethod
    @abstractmethod
    async def process_csv(products: list[Product]) -> StringIO:
        """
        Converts a list of Product objects into CSV format.

        :param products: List of Product instances to be converted to CSV.
        :return: StringIO object containing the CSV data.
        """
