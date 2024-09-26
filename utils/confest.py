import pytest

@pytest.fixture
def valid_credentials():
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }