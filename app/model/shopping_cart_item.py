from sqlalchemy import Column, Float, Integer, String

from app.model.base_model import BaseModel


class ShoppingCartItem(BaseModel):
    __tablename__ = "shopping_cart_item"

    product_name = Column(String(length=100), nullable=False, unique=True, index=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    reservation_id = Column(Integer, nullable=True)
