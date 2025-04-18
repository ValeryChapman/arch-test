from io import StringIO

from fastapi import APIRouter, Depends, Query
from starlette.responses import StreamingResponse

from internal.controllers.http.products.schemas import ParseProductsResponseSchema
from internal.di.authorization.token import api_key_authorization
from internal.di.products.service import get_product_service
from internal.models import Product
from internal.schemas.fakestoreapi.product import FakeStoreAPIProductSchema
from internal.schemas.product import ProductSchema
from internal.services.products.abstract import ProductServiceAbstract

router = APIRouter(prefix="/products", tags=["Products"])


@router.post(
    "/parse",
    response_model=ParseProductsResponseSchema,
    dependencies=[Depends(api_key_authorization)],
)
async def parse_products(
    product_service: ProductServiceAbstract = Depends(get_product_service),
):
    parsed_products: list[FakeStoreAPIProductSchema] = (
        await product_service.parse_products()
    )
    inserted_products: list[Product] = await product_service.bulk_insert(
        parsed_products=parsed_products
    )
    return ParseProductsResponseSchema(
        status=True,
        data=[
            ProductSchema(
                id=product.id,
                title=product.title,
                price=product.price,
                category=product.category,
            )
            for product in inserted_products
        ],
    )


@router.get("/csv", dependencies=[Depends(api_key_authorization)])
async def get_by_price_range_returning_csv(
    min_price: float = Query(0.0, ge=0.0, description="Minimum price"),
    max_price: float = Query(1000000.0, ge=0.0, description="Maximum price"),
    product_service: ProductServiceAbstract = Depends(get_product_service),
):
    filtered_products: list[Product] = await product_service.get_by_price_range(
        min_price, max_price
    )
    products_csv: StringIO = await product_service.process_csv(
        products=filtered_products
    )
    return StreamingResponse(
        products_csv,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=products.csv"},
    )
