from fastapi import status

test_request_payload = {
    "product_name": "test_product 1",
    "quantity": 1,
    "price": 1.0,
}


class TestShoppingCartItem:
    def test_get_shopping_cart_items_success(self, test_app, monkeypatch):
        test_data = [
            {
                "id": 1,
                "product_name": "test_product 1",
                "quantity": 1,
                "price": 1.0,
                "reservation_id": 123,
            },
            {
                "id": 2,
                "product_name": "test_product 2",
                "quantity": 1,
                "price": 1.0,
                "reservation_id": 124,
            },
        ]

        async def mock_get_cart_items(service):
            return test_data

        monkeypatch.setattr(
            "app.service.shopping_cart_item_service.ShoppingCartItemService.get_cart_items",
            mock_get_cart_items,
        )

        response = test_app.get("/api/v1/shopping_cart_item/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get("data") == test_data

    def test_get_shopping_cart_items_empty(self, test_app, monkeypatch):
        test_data = []

        async def mock_get_cart_items(service):
            return test_data

        monkeypatch.setattr(
            "app.service.shopping_cart_item_service.ShoppingCartItemService.get_cart_items",
            mock_get_cart_items,
        )

        response = test_app.get("/api/v1/shopping_cart_item/")
        assert response.status_code == 200
        assert response.json().get("info") == "No shopping cart items found"

    def test_get_shopping_cart_items_error(self, test_app, monkeypatch):
        async def mock_get_cart_items(service):
            raise Exception("mock exception")

        monkeypatch.setattr(
            "app.service.shopping_cart_item_service.ShoppingCartItemService.get_cart_items",
            mock_get_cart_items,
        )

        response = test_app.get("/api/v1/shopping_cart_item/")
        assert response.status_code == 500
        assert (
            response.json().get("detail")
            == "Could not retreive list of shopping cart items: mock exception"
        )

    def test_add_shopping_cart_item_success(self, test_app, monkeypatch):
        test_response_payload = {"info": "Cart item is being processed for reservation"}

        async def mock_add_cart_item(service, test_request_payload):
            return True

        monkeypatch.setattr(
            "app.service.shopping_cart_item_service.ShoppingCartItemService.add_cart_item",
            mock_add_cart_item,
        )

        response = test_app.post(
            "/api/v1/shopping_cart_item/",
            json=test_request_payload,
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == test_response_payload

    def test_add_shopping_cart_item_client_error(self, test_app, monkeypatch):
        test_response_payload = "Could not add item to shopping cart"

        async def mock_add_cart_item(service, test_request_payload):
            return False

        monkeypatch.setattr(
            "app.service.shopping_cart_item_service.ShoppingCartItemService.add_cart_item",
            mock_add_cart_item,
        )

        response = test_app.post(
            "/api/v1/shopping_cart_item/",
            json={},
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_add_shopping_cart_item_server_error(self, test_app, monkeypatch):
        test_response_payload = "Could not add item to shopping cart: mock exception"

        async def mock_add_cart_item(service, test_request_payload):
            raise Exception("mock exception")

        monkeypatch.setattr(
            "app.service.shopping_cart_item_service.ShoppingCartItemService.add_cart_item",
            mock_add_cart_item,
        )

        response = test_app.post(
            "/api/v1/shopping_cart_item/",
            json=test_request_payload,
        )
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.json().get("detail") == test_response_payload
