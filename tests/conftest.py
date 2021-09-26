import pytest
from time import time
from microblock.blockchain import Blockchain, Transaction, Block

@pytest.fixture
def new_blockchain():
    return Blockchain()

@pytest.fixture
def new_transaction():
    return Transaction(
        sender='a',
        recipient='b',
        amount=1.0
    )
