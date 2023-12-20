def test_health(test_app):
    response = test_app.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Roche Shopping Cart",
        "version": "0.0.1",
        "status": "ok",
    }
