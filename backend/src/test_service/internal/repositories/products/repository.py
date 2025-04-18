from sqlalchemy import text
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from internal.models import Product
from internal.repositories.products.abstract import ProductRepositoryAbstract
from internal.schemas.fakestoreapi.product import FakeStoreAPIProductSchema


class ProductRepository(ProductRepositoryAbstract):
    model = Product

    async def bulk_insert(
        self,
        postgres_session: AsyncSession,
        parsed_products: list[FakeStoreAPIProductSchema],
    ) -> list[Product]:
        """
        Bulk inserts or updates a list of products into the database.

        If a product with the same ID already exists, it will be updated with the new values.

        :param postgres_session: Asynchronous Postgres session.
        :param parsed_products: List of parsed products to insert or update.
        :return: List of inserted or updated Product instances.
        """
        if not parsed_products:
            return []

        stmt = (
            insert(self.model)
            .values(
                [
                    {
                        "id": product.id,
                        "title": product.title,
                        "price": product.price,
                        "category": product.category,
                    }
                    for product in parsed_products
                ]
            )
            .on_conflict_do_update(
                index_elements=["id"],
                set_={
                    "title": text("excluded.title"),
                    "price": text("excluded.price"),
                    "category": text("excluded.category"),
                },
            )
            .returning(self.model)
        )

        result = await postgres_session.execute(stmt)
        inserted_products = result.scalars().all()
        await postgres_session.commit()

        return inserted_products  # noqa

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
        stmt = select(self.model).where(
            self.model.price >= min_price, self.model.price <= max_price
        )
        result = await postgres_session.execute(stmt)
        return result.scalars().all()  # noqa
