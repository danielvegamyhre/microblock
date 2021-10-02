import pytest

def test_genesis_block(new_blockchain):
    assert new_blockchain.last_block is not None
    assert new_blockchain.last_block.proof_of_work == 0
    assert new_blockchain.last_block.prev_block_hash == '0'

def test_add_valid_node(new_blockchain):
    valid_node: str = 'http://192.168.1.1:5000'
    assert new_blockchain.add_node(valid_node) is None

def test_add_invalid_node(new_blockchain):
    invalid_nodes: list[str] = [
        'http://192.168.1.1',
        '192.168.1.1:5000',
        '192.168.1.1',
    ]
    for invalid_node in invalid_nodes:
        with pytest.raises(ValueError):
            new_blockchain.add_node(invalid_node)
