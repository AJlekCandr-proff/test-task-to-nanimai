from decimal import Decimal
from uuid import UUID

from sqlalchemy import select, update

from test_app.domain.protocols.repo.user_repo_protocol import (
    UserReadRepositoryProtocol,
    UserWriteRepositoryProtocol,
)

from test_app.domain.user.model import UserModel
from test_app.gateways.alchemy_gateway import AlchemyGateway
from test_app.infrastucture.database.models import User


class UserReadRepository(UserReadRepositoryProtocol):
    def __init__(self, gateway: AlchemyGateway) -> None:
        self.async_session = gateway.async_session_factory
        self.model = User

    @staticmethod
    def _alchemy_to_model(data: User) -> UserModel | None:
        try:
            return UserModel(
                balance=data.balance,
                uuid=data.uuid,
                max_balance=data.balance,
                name=data.name,
            )

        except ValueError:
            return None

    async def get_user(self, user_uuid: UUID) -> UserModel | None:
        async with self.async_session() as session:
            stmt = select(self.model).where(self.model.uuid == user_uuid)

            answer = await session.execute(stmt)

            result = answer.scalar_one_or_none()

            if result:
                return self._alchemy_to_model(result)

            return None


class UserWriteRepository(UserWriteRepositoryProtocol):
    def __init__(self, gateway: AlchemyGateway) -> None:
        self.async_session = gateway.transactional_session
        self.model = User

    @staticmethod
    def _alchemy_to_model(data: User) -> UserModel | None:
        try:
            return UserModel(
                balance=data.balance,
                uuid=data.uuid,
                max_balance=data.balance,
                name=data.name,
            )

        except ValueError:
            return None

    async def set_current_balance_user(
        self, user_uuid: UUID, balance: Decimal
    ) -> UserModel:
        async with self.async_session() as session:
            stmt = (
                update(self.model)
                .values(balance=balance)
                .where(self.model.uuid == user_uuid)
                .returning(self.model)
            )

            answer = await session.execute(stmt)

            result = answer.scalar_one_or_none()

            if result:
                return self._alchemy_to_model(result)

            return None

    async def set_max_balance_user(
        self, user_uuid: UUID, max_balance: Decimal
    ) -> UserModel:
        async with self.async_session() as session:
            stmt = (
                update(self.model)
                .values(max_balance=max_balance)
                .where(self.model.uuid == user_uuid)
                .returning(self.model)
            )

            answer = await session.execute(stmt)

            result = answer.scalar_one_or_none()

            if result:
                return self._alchemy_to_model(result)

            return None
