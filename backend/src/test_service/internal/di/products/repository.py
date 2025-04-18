from internal.repositories.products.abstract import ProductRepositoryAbstract
from internal.repositories.products.repository import ProductRepository


def get_product_repository() -> ProductRepositoryAbstract:
    """
    Returns an instance of the product repository.

    :return: Instance of ProductRepositoryAbstract.
    """
    return ProductRepository()
