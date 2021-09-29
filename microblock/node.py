from flask import request, jsonify, Response
from microblock import app, local_chain
from dataclasses import asdict

@app.route('/nodes', methods=['GET'])
def get_nodes():
    return jsonify(list(local_chain.nodes)), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    if not request.json:
        return "Missing node information in JSON format", 400

    nodes = request.get_json()
    for node_address in nodes:
        local_chain.add_node(node_address)

    response = {
        'message': f'added {len(nodes)} new nodes',
        'total_nodes': f'{len(local_chain.nodes)}'
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify(local_chain.chain), 200

    
    


    

