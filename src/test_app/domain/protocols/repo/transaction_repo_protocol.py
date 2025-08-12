from decimal import Decimal
from typing import Protocol
from uuid import UUID

from test_app.domain.transaction.model import TransactionModel


class TransactionReadRepositoryProtocol(Protocol):
    async def get_transaction(self, transaction_uuid: UUID) -> TransactionModel | None:
        raise NotImplementedError()


class TransactionWriteRepositoryProtocol(Protocol):
    async def open_transaction(
        self, token: str, save_sum: Decimal, user_uuid: UUID
    ) -> TransactionModel:
        raise NotImplementedError()

    async def close_transaction(self, transaction_uuid: UUID) -> TransactionModel:
        raise NotImplementedError()

    async def cancel_transaction(self, transaction_uuid: UUID) -> TransactionModel:
        raise NotImplementedError()
