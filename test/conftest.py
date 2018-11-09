from burnafterme.app import create_app
import pytest

@pytest.fixture
def client():
    return create_app("DevProfile").test_client()
