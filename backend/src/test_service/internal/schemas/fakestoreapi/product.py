from pydantic import BaseModel


class FakeStoreAPIProductRatingSchema(BaseModel):
    rate: float
    count: int


class FakeStoreAPIProductSchema(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: FakeStoreAPIProductRatingSchema
