from tests.test_utils import random_transaction


def test_chained_blocks(new_blockchain):
    # make 5 blocks with 5 transactions each
    for _block in range(5):
        # add 5 random transactions
        for _txn in range(5):
            txn = random_transaction()
            idx = new_blockchain.new_transaction(txn)
            print(txn, "added to block", idx)

        # proof of work
        proof = new_blockchain.proof_of_work()
        print("found proof", proof)

        # add new block
        block = new_blockchain.new_block(proof)
        print("block", block.index, "created")

    # validate chain
    print("validating chain...")
    assert new_blockchain.is_valid_chain() is True
    print("blockchain is valid!")
