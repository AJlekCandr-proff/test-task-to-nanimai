from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from test_app.domain.transaction.enums.status_transaction_enum import (
    StatusTransactionEnum,
)


@dataclass(frozen=True)
class TransactionModel:
    date_open: datetime
    status: StatusTransactionEnum
    date_close: datetime
    service_creator: str
    save_sum: Decimal
    user_uuid: UUID
