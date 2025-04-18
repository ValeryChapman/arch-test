from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    title: str
    price: float
    category: str
