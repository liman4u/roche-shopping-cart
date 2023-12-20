from dependency_injector import containers, providers

from app.core.database import Database
from app.core.settings import settings
from app.repository.shopping_cart_item_repository import ShoppingCartItemRepository
from app.service.shopping_cart_item_service import ShoppingCartItemService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoints.shopping_cart_item",
        ]
    )

    db = providers.Singleton(Database, db_url=settings.DATABASE_URI)

    # Repositories
    shopping_cart_item_repository = providers.Factory(
        ShoppingCartItemRepository, session_factory=db.provided.session
    )

    # Services
    shopping_cart_item_service = providers.Factory(
        ShoppingCartItemService,
        shopping_cart_item_repository=shopping_cart_item_repository,
    )
