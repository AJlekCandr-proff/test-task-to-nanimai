from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass
class UserModel:
    uuid: UUID
    name: str
    max_balance: Decimal
    balance: Decimal
