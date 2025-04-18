from pydantic import BaseModel

from internal.schemas.product import ProductSchema


class ParseProductsResponseSchema(BaseModel):
    status: bool
    data: list[ProductSchema]
