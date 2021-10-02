import json
import requests
from typing import Optional, Union
from dataclasses import dataclass, asdict
from hashlib import sha256
from time import time
from urllib.parse import urlparse


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
    proof_of_work: int
    prev_block_hash: str

class Blockchain:
    def __init__(self):
        self.nodes: set = set()
        self.chain: list[Block] = []
        self.current_transactions: list[Transaction] = []
        self.new_block(0, '0') # genesis block

    def __len__(self) -> int:
        return len(self.chain)

    def new_block(
        self, 
        proof_of_work: int,
        prev_block_hash: Optional[str] = None,
    ) -> None:
        '''Creates a new block and add it to the chain.'''
        # create new block and reset current transactions
        block = Block(
            index=len(self.chain) + 1,
            timestamp=time(),
            transactions=self.current_transactions,
            proof_of_work=proof_of_work,
            prev_block_hash=prev_block_hash or self.hash(self.last_block)
        )
        self.current_transactions: list = []

        # append new block to chain and return it
        self.chain.append(block)
        return block

    def new_transaction(self, transaction: Union[dict, Transaction]) -> int:
        '''
        Add a new transction to list of current transactions.
        Returns index of block that will hold this transaction.
        '''
        if not isinstance(transaction, Transaction):
            transaction = Transaction(**transaction)
        self.current_transactions.append(transaction)
        return len(self.chain) + 1

    def hash(self, block: Block) -> str:
        '''Get SHA256 hash of a block.'''
        serialized: str  = json.dumps(
            asdict(block),
            sort_keys=True
        )
        return sha256(serialized.encode()).hexdigest()

    @property
    def last_block(self) -> Block:
        '''Returns last block in the chain.'''
        # there will always be at least 1 block (genesis block)
        return self.chain[-1]

    def proof_of_work(self) -> int:
        '''
        Proof of work algorithm which finds a value x such that
        hash(prev_hash + previous_proof + x) starts with 3 0s
        '''
        last_proof: int = self.last_block.proof_of_work
        prev_hash: str = self.hash(self.last_block)
        proof: int = 0

        # brute force search for valid proof of work
        while not self.is_valid_proof(proof, last_proof, prev_hash):
            proof += 1
        return proof

    def is_valid_proof(
        self, 
        proof: int, 
        last_proof: int, 
        prev_hash: str
    ) -> bool:
        '''
        Validates the proof of work:
        
        hash(prev_block_hash + last_block_proof + curr_block_proof)

        must start with 3 0s
        '''
        guess_str = f'{prev_hash}{last_proof}{proof}'
        guess_hash = sha256(guess_str.encode()).hexdigest()
        return guess_hash[:3] == '000'
        
    def is_valid_chain(self) -> bool:
        '''
        Validate the entire blockchain.

        - Each block's "prev hash" must be correct hash of previous block
        - Each block's "proof of work" must be valid for that block

        '''
        for i in range(1, len(self.chain)):
            curr_block: Block = self.chain[i]
            last_block: Block = self.chain[i-1]

            # check prev hash
            if curr_block.prev_block_hash != self.hash(last_block):
                print(curr_block.prev_block_hash, '!=', self.hash(last_block))
                return False

            # check proof of work
            if not self.is_valid_proof(
                curr_block.proof_of_work,
                last_block.proof_of_work, 
                self.hash(last_block)
            ):
                print('invalid proof of work', curr_block.proof_of_work, 'for block', curr_block.index)
                return False
        return True

    def add_node(self, node_address: str) -> None:
        '''
        Add new node address to nodes in network.
        '''
        url_obj = urlparse(node_address)
        # validate requirements: scheme, url/IP, port number
        if not all([url_obj.scheme, url_obj.netloc, url_obj.port]):
            raise ValueError(f'Invalid node address: {node_address}')
        self.nodes.add(node_address)
    
    def consensus(self) -> Optional[list[Block]]:
        # consensus is to use the longest chain in the network
        replaced = False
        for node in self.nodes:
            res = requests.get(f'{node}/chain')
            node_chain = res.json()
            if len(node_chain) > len(self.chain):
                self.chain = [Block(**block) for block in node_chain]
                replaced = True        
        if replaced:
            return self.chain
