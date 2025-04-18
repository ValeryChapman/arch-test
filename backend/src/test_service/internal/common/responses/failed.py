from pydantic import BaseModel


class DefaultErrorResponseSchema(BaseModel):
    status: bool = False
    message: str
