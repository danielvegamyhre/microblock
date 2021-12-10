from uuid import uuid4

from flask import Flask

from backend.blockchain import Blockchain

# set up local instance of blockchain
local_chain = Blockchain()

# unique identifier for this node to send/receive coins
node_identifier = str(uuid4()).replace("-", "")

# set up node
app = Flask(__name__)
from backend import api  # noqa: F401,E402
