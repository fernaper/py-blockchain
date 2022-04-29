from dataclasses import dataclass


@dataclass
class Transaction:
    sender: str
    recipient: str
    data: int
