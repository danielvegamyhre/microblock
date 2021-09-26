from microblock.blockchain import Blockchain, Transaction, Block

def test_genesis_block():
    b = Blockchain()
    assert b.last_block is not None
    assert b.last_block.proof_of_work == 0
    assert b.last_block.prev_block_hash == '0'

