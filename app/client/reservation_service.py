import structlog
from fastapi import status

from app.core.settings import get_settings
from app.service.shopping_cart_item_service import ShoppingCartItemService
from app.util.common import aiohttp_post

log = structlog.get_logger()


async def emit_reserve_cart_item(
    item: str, shopping_cart_item_service: ShoppingCartItemService
):
    """
    Sends a request to the reservation service to reserve a cart item.

    Args:
        item (str): The name of the product to be reserved.
        shopping_cart_item_service (ShoppingCartItemService): An instance of the ShoppingCartItemService class.

    Returns:
        None
    """
    reservation_service_url = f"{get_settings().RESERVATION_SERVICE_URL}/reserve"

    try:
        response, status_code = await aiohttp_post(
            url=reservation_service_url, data={"item": item}
        )
        if status_code == status.HTTP_200_OK:
            reservation_id = response.get("reservation_id")
            await shopping_cart_item_service.update_cart_item(
                product_name=item, reservation_id=reservation_id
            )
            log.info(f"Item {item} reserved: {reservation_id}")
        else:
            log.error(f"Could not reserve item: {response}")
    except Exception as e:
        log.error(f"Could not reserve item: {str(e)}")
