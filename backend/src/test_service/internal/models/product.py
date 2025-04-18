from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from internal.models.base import BaseModel


class Product(BaseModel):
    __tablename__ = "products"
    __table_args__ = {"schema": "public"}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    category: Mapped[str | None] = mapped_column(String(100))

    def __repr__(self) -> str:
        return f"<Product(id={self.id}, title={self.title[:20]}...)>"
