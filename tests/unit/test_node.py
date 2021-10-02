import pytest

def test_register_node(app_test_client):
    client, chain = app_test_client
    node_address = 'http://192.168.1.2:5000'
    res = client.post('/nodes/register', json=[node_address])
    assert res.status_code == 200
    assert node_address in chain.nodes


def test_get_nodes(app_test_client):
    client, chain = app_test_client
    # register test node
    node_address = 'http://192.168.1.2:5000'
    res = client.post('/nodes/register', json=[node_address])
    assert res.status_code == 200
    assert node_address in chain.nodes

    # check /nodes returns nodes in json format
    res = client.get('/nodes')
    assert node_address in res.get_json()


def test_get_chain(app_test_client):
    client, chain = app_test_client

    # /chain should return genesis block in json format
    res = client.get('/chain')
    returned_chain = res.get_json()
    assert len(chain) == len(returned_chain)
    assert chain.last_block.index == returned_chain[0]['index']
    assert chain.last_block.prev_block_hash == returned_chain[0]['prev_block_hash']
    assert chain.last_block.timestamp == returned_chain[0]['timestamp']
    assert chain.last_block.proof_of_work == returned_chain[0]['proof_of_work']