from microblock.blockchain import Blockchain, Transaction, Block

def test_genesis_block(new_blockchain):
    assert new_blockchain.last_block is not None
    assert new_blockchain.last_block.proof_of_work == 0
    assert new_blockchain.last_block.prev_block_hash == '0'

