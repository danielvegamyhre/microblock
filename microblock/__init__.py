from flask import Flask
from microblock.blockchain import Blockchain

app = Flask(__name__)
local_chain = Blockchain()

from microblock import node

app.run(host='0.0.0.0', port=5000)