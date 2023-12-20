import structlog
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.responses import ORJSONResponse

from app.client.reservation_service import emit_reserve_cart_item
from app.core.container import Container
from app.schema.shopping_cart_item import ShoppingCartItemPayload
from app.service.shopping_cart_item_service import ShoppingCartItemService
from app.util.common import (
    client_side_error,
    internal_server_error,
    send_data,
    send_info,
)

router = APIRouter(
    prefix="/shopping_cart_item",
    tags=["Shopping Cart Item"],
)
log = structlog.get_logger()


@router.get("/", response_class=ORJSONResponse)
@inject
async def get_shopping_cart_items_handler(
    service: ShoppingCartItemService = Depends(
        Provide[Container.shopping_cart_item_service]
    ),
):
    try:
        cart_items = await service.get_cart_items()
        if not cart_items:
            return send_info(info="No shopping cart items found")
        return send_data(data=cart_items)
    except Exception as e:
        raise internal_server_error(
            detail=f"Could not retreive list of shopping cart items: {str(e)}"
        )


@router.post("/", response_class=ORJSONResponse)
@inject
async def add_shopping_cart_item_handler(
    payload: ShoppingCartItemPayload,
    background_tasks: BackgroundTasks,
    service: ShoppingCartItemService = Depends(
        Provide[Container.shopping_cart_item_service]
    ),
):
    try:
        success = await service.add_cart_item(payload)
        if success:
            # emit event to reservation service to run in background
            background_tasks.add_task(
                emit_reserve_cart_item, payload.product_name, service
            )
            return send_info(info="Cart item is being processed for reservation")
        return client_side_error(detail="Could not add item to shopping cart")
    except Exception as e:
        raise internal_server_error(
            detail=f"Could not add item to shopping cart: {str(e)}"
        )
