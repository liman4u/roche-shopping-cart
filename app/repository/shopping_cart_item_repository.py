from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.model.shopping_cart_item import ShoppingCartItem
from app.repository.base_repository import BaseRepository


class ShoppingCartItemRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, ShoppingCartItem)
