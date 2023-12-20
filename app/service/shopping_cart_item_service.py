from sqlalchemy.exc import IntegrityError

from app.repository.shopping_cart_item_repository import ShoppingCartItemRepository
from app.schema.shopping_cart_item import ShoppingCartItemPayload


class ShoppingCartItemService:
    def __init__(self, shopping_cart_item_repository: ShoppingCartItemRepository):
        self.shopping_cart_item_repository = shopping_cart_item_repository

    async def get_cart_items(self) -> list:
        return self.shopping_cart_item_repository.read_all()

    async def add_cart_item(self, schema: ShoppingCartItemPayload):
        try:
            cart_item = self.shopping_cart_item_repository.create(schema)
            if cart_item:
                return True
            return False
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    async def update_cart_item(self, product_name: str, reservation_id: int):
        try:
            cart_item = self.shopping_cart_item_repository.update_by_product_name(
                product_name, reservation_id
            )
            if cart_item:
                return True
        except Exception as e:
            raise e
