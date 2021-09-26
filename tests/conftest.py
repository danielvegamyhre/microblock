import pytest
import random
from time import time
from microblock.blockchain import Blockchain, Transaction, Block


@pytest.fixture
def new_blockchain():
    return Blockchain()

def random_transaction():
    # 3 parties: a, b, c -> choose 2 at random (must be different)
    sender = random.choice(['a','b','c'])
    recipient = sender
    while recipient == sender:
        recipient = random.choice(['a','b','c'])
    
    # random amount
    amount = float(random.randrange(1,100))

    return Transaction(
        sender=sender,
        recipient=recipient,
        amount=amount
    )
