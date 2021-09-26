import random
from time import time
from microblock.blockchain import Transaction

def random_transaction():
    # 3 parties: a, b, c -> choose 2 at random (must be different)
    sender: str = random.choice(['a','b','c'])
    recipient: str = sender
    while recipient == sender:
        recipient = random.choice(['a','b','c'])
    
    # random amount
    amount: float = float(random.randrange(1,100))

    return Transaction(
        sender=sender,
        recipient=recipient,
        amount=amount
    )