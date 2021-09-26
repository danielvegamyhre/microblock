import pytest
from microblock.blockchain import Blockchain


@pytest.fixture
def new_blockchain():
    return Blockchain()

