import pytest

from backend import app, local_chain
from backend.blockchain import Blockchain


@pytest.fixture
def app_test_client():
    with app.app_context():
        with app.test_client() as client:
            yield client, local_chain


@pytest.fixture
def new_blockchain():
    return Blockchain()
