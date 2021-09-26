from microblock.blockchain import Blockchain, Transaction, Block
from ..conftest import random_transaction

def test_proof_of_work(new_blockchain):
    # add a few random transactions
    for _ in range(5):
        txn = random_transaction()
        idx = new_blockchain.new_transaction(txn)
        print(txn, 'added to block', idx)

    # proof of work
    proof = new_blockchain.proof_of_work()
    print('found proof', proof)

    # add new block
    block = new_blockchain.new_block(proof)
    print('block', block.index, 'created')
    print(block)