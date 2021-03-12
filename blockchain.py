from hashlib import sha256

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        '''Creates a new block and add it to the chain.'''
        pass

    def new_transaction(self):
        '''Add a new transction to list of current transactions.'''
        pass

    @staticmethod
    def hash(self):
        '''Get SHA256 hash of current block.'''
        pass

    @property
    def last_block(self):
        '''Returns last block in the chain.'''
        pass

