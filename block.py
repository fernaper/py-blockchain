import json
import hashlib

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from transaction import Transaction


@dataclass
class Block():
    index: int
    timestamp: float
    transactions: List[Transaction]
    proof: float
    description: Optional[str] = None
    previous_hash: Optional[str] = None  # Genesis block does not have a hash

    @property
    def hash(self):
        block_str = json.dumps(self.asdict(), sort_keys=True).encode()
        return hashlib.sha256(block_str).hexdigest()


class Factory():

    @staticmethod
    def new_block(index: int, proof: float, transactions: List[Transaction] = [], description: Optional[str] = None, previous_hash: Optional[str] = None) -> Block:
        return Block(
            index=index,
            timestamp=datetime.utcnow().timestamp(),
            transactions=transactions,
            proof=proof,
            description=description,
            previous_hash=previous_hash
        )
