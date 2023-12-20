from pydantic import BaseModel


class ShoppingCartItemPayload(BaseModel):
    product_name: str
    quantity: int
    price: float


class ShoppingCartItemDBInput(BaseModel):
    product_name: str
    quantity: int
    price: float
    reservation_id: int

    class Config:
        orm_model = True


class ShoppingCartItemDBOutput(BaseModel):
    id: int
    product_name: str
    quantity: int
    price: float
    reservation_id: int

    class Config:
        orm_model = True
