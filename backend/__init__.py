from flask import Flask

from backend.blockchain import Blockchain

# set up local instance of blockchain
local_chain = Blockchain()

# set up node
app = Flask(__name__)
from backend import api  # noqa: F401,E402
