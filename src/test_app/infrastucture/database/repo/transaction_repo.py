from decimal import Decimal
from uuid import UUID

from sqlalchemy import select, update

from test_app.domain.protocols.repo.transaction_repo_protocol import (
    TransactionReadRepositoryProtocol,
    TransactionWriteRepositoryProtocol,
)
from test_app.domain.transaction.enums.status_transaction_enum import (
    StatusTransactionEnum,
)
from test_app.domain.transaction.model import TransactionModel
from test_app.gateways.alchemy_gateway import AlchemyGateway
from test_app.infrastucture.database.models import Transaction


class TransactionReadRepository(TransactionReadRepositoryProtocol):
    def __init__(self, gateway: AlchemyGateway) -> None:
        self.async_session = gateway.async_session_factory
        self.model = Transaction

    @staticmethod
    def _alchemy_to_model(data: Transaction | None) -> TransactionModel | None:
        try:
            return TransactionModel(
                user_uuid=data.user_uuid,
                uuid=data.uuid,
                date_open=data.date_open,
                status=data.status,
                date_close=data.date_close,
                service_creator=data.service_creator,
                save_sum=data.save_sum,
            )

        except ValueError:
            return None

    async def get_transaction(self, transaction_uuid: UUID) -> TransactionModel | None:
        async with self.async_session() as session:
            stmt = select(self.model).where(self.model.uuid == transaction_uuid)

            answer = await session.execute(stmt)

            result = answer.scalar_one_or_none()

            if result:
                return self._alchemy_to_model(result)

            return None


class TransactionWriteRepository(TransactionWriteRepositoryProtocol):
    def __init__(self, gateway: AlchemyGateway) -> None:
        self.async_session = gateway.transactional_session
        self.model = Transaction

    @staticmethod
    def _alchemy_to_model(data: Transaction | None) -> TransactionModel | None:
        try:
            return TransactionModel(
                user_uuid=data.user_uuid,
                uuid=data.uuid,
                date_open=data.date_open,
                status=data.status,
                date_close=data.date_close,
                service_creator=data.service_creator,
                save_sum=data.save_sum,
            )

        except ValueError:
            return None

    async def open_transaction(
        self, token: str, save_sum: Decimal, user_uuid: UUID
    ) -> TransactionModel:
        async with self.async_session() as session:
            stmt = (
                update(self.model)
                .values(service_creator=token, save_sum=save_sum)
                .where(self.model.user_uuid == user_uuid)
                .returning(self.model)
            )

            answer = await session.execute(stmt)

            result = answer.scalar_one_or_none()

            if result:
                return self._alchemy_to_model(result)

            return None

    async def close_transaction(self, transaction_uuid: UUID) -> TransactionModel:
        async with self.async_session() as session:
            stmt = (
                update(self.model)
                .values(status=StatusTransactionEnum.CLOSE)
                .where(self.model.uuid == transaction_uuid)
                .returning(self.model)
            )

            answer = await session.execute(stmt)

            result = answer.scalar_one_or_none()

            if result:
                return self._alchemy_to_model(result)

            return None

    async def cancel_transaction(self, transaction_uuid: UUID) -> TransactionModel:
        async with self.async_session() as session:
            stmt = (
                update(self.model)
                .values(status=StatusTransactionEnum.CANCEL)
                .where(self.model.uuid == transaction_uuid)
                .returning(self.model)
            )

            answer = await session.execute(stmt)

            result = answer.scalar_one_or_none()

            if result:
                return self._alchemy_to_model(result)

            return None
