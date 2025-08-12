from decimal import Decimal
from typing import Protocol
from uuid import UUID

from test_app.domain.user.model import UserModel


class UserReadRepositoryProtocol(Protocol):
    async def get_user(self, user_uuid: UUID) -> UserModel:
        raise NotImplementedError()


class UserWriteRepositoryProtocol(Protocol):
    async def set_current_balance_user(
        self, user_uuid: UUID, balance: Decimal
    ) -> UserModel:
        raise NotImplementedError()

    async def set_max_balance_user(
        self, user_uuid: UUID, max_balance: Decimal
    ) -> UserModel:
        raise NotImplementedError()
