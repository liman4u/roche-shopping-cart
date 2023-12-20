from unittest import mock

import pytest

from app.client.reservation_service import emit_reserve_cart_item
from app.service.shopping_cart_item_service import ShoppingCartItemService


class TestReservationService:
    @pytest.mark.asyncio
    async def x_test_emit_reserve_cart_item(
        self,
        monkeypatch: pytest.MonkeyPatch,
        caplog: pytest.LogCaptureFixture,
    ):
        test_item = "test_item"
        test_reservation_id = 1

        async def mock_aiohttp_post(url, data={"item": test_item}):
            return {"reservation_id": test_reservation_id}, 200

        monkeypatch.setattr(
            "app.util.common.aiohttp_post",
            mock_aiohttp_post,
        )

        async def mock_update_cart_item(test_item, test_reservation_id):
            return True

        monkeypatch.setattr(
            "app.service.shopping_cart_item_service.ShoppingCartItemService.update_cart_item",
            mock_update_cart_item,
        )

        def mock_service():
            return mock.MagicMock(spec=ShoppingCartItemService)

        await emit_reserve_cart_item(test_item, mock_service())
        assert f"Item {test_item} reserved: {test_reservation_id}" in caplog.text

    @pytest.mark.asyncio
    async def x_test_emit_reserve_cart_item_error(
        self,
        monkeypatch: pytest.MonkeyPatch,
        caplog: pytest.LogCaptureFixture,
    ):
        test_item = "test_item"
        test_error_message = "Error occurred"

        async def mock_aiohttp_post(url, data={"item": test_item}):
            raise Exception(test_error_message)

        monkeypatch.setattr(
            "app.util.common.aiohttp_post",
            mock_aiohttp_post,
        )

        def mock_service():
            return mock.MagicMock(spec=ShoppingCartItemService)

        await emit_reserve_cart_item(test_item, mock_service())
        assert f"Could not reserve item: {test_error_message}" in caplog.text
