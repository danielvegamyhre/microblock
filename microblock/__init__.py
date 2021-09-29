from flask import Flask
from microblock.blockchain import Blockchain

# set up local instance of blockchain
local_chain = Blockchain()

# set up node
app = Flask(__name__)
from microblock import node
