
def test_app_returns_hello_world(client):
    assert client.get("/").data == b"Hello World"
