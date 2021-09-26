import json
from dataclasses import dataclass, asdict
from hashlib import sha256
from time import time

@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float

@dataclass
class Block:
    index: int
    timestamp: float
    transactions: list[Transaction]
    proof_of_work: str
    prev_block_hash: str

class Blockchain:
    def __init__(self):
        self.chain: list[Block] = []
        self.current_transactions: list[Transaction] = []

    def new_block(
        self, 
        proof_of_work: str, 
        prev_block_hash: str
        ) -> None:
        '''Creates a new block and add it to the chain.'''

        # create new block and reset current transactions
        block = Block(
            index=len(self.chain) + 1,
            timestamp=time(),
            transactions=self.current_transactions,
            proof_of_work=proof_of_work,
            prev_block_hash=self.hash()
        )
        self.current_transactions = []

        # append new block to chain and return it
        self.chain.append(block)
        return block

    def new_transaction(self, transaction: Transaction) -> int:
        '''
        Add a new transction to list of current transactions.
        Returns index of block that will hold this transaction.
        '''
        self.current_transactions.append(transaction)
        return len(self.chain) + 1

    
    def hash(self, block: Block) -> str:
        '''Get SHA256 hash of a block.'''
        serialized:str  = json.dumps(
            asdict(block),
            sort_keys=True
        )
        return sha256(serialized).hexdigest()

    @property
    def last_block(self) -> Block:
        '''Returns last block in the chain.'''
        if not self.chain:
            return
        return self.chain[-1]

