from fastapi import APIRouter

from app.api.v1.endpoints.health_check import router as health_check_router
from app.api.v1.endpoints.shopping_cart_item import router as shopping_cart_item_router

routers = APIRouter()
router_list = [health_check_router, shopping_cart_item_router]

for router in router_list:
    routers.include_router(router)
