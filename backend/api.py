import json

from flask import jsonify, request

from backend import app, local_chain, node_identifier
from backend.blockchain import Transaction


# allow cross-origin from react frontend
@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response


@app.route("/chain", methods=["GET"])
def get_chain():
    return jsonify(local_chain.chain), 200


@app.route("/nodes", methods=["GET"])
def get_nodes():
    return jsonify(list(local_chain.nodes)), 200


@app.route("/nodes/register", methods=["POST"])
def add_a_node():
    nodes = request.get_json()
    for node in nodes:
        local_chain.add_node(node)
    return jsonify(list(local_chain.nodes)), 200


@app.route("/nodes/consensus", methods=["GET"])
def consensus():
    replaced = local_chain.consensus()
    if replaced:
        response = {"message": "Our chain was replaced", "new_chain": local_chain.chain}
    else:
        response = {"message": "Our chain is authoritative", "chain": local_chain.chain}
    return jsonify(response), 200


@app.route("/mine", methods=["GET"])
def mine():
    # compute the proof of work
    last_block = local_chain.last_block
    proof = local_chain.proof_of_work()

    # receive a reward for finding the proof
    local_chain.new_transaction(
        Transaction(sender="0", recipient=node_identifier, amount=1)
    )

    # link the new block to the chain
    previous_hash = local_chain.hash(last_block)
    block = local_chain.new_block(proof, previous_hash)

    response = {
        "message": "New block created",
        "index": block.index,
        "transactions": block.transactions,
        "proof": block.proof_of_work,
        "previous_hash": block.prev_block_hash,
    }
    return jsonify(response), 200


@app.route("/transactions/new", methods=["POST"])
def new_transaction():
    values = json.loads(request.get_data())
    required = ["sender", "recipient", "amount"]

    if not all(k in values for k in required):
        return "Missing values", 400

    txn = Transaction(
        sender=values["sender"],
        recipient=values["recipient"],
        amount=float(values["amount"]),
    )
    index = local_chain.new_transaction(txn)
    response = {"message": f"Transaction will be added to Block {index}"}
    return jsonify(response), 200


@app.route("/transactions", methods=["GET"])
def get_transactions():
    return jsonify(local_chain.current_transactions), 200
