from decimal import Decimal
from uuid import UUID

from fastapi import status
from fastapi.responses import ORJSONResponse

from test_app.domain.user.model import UserModel


# Не успеваю сделать сервисы для юзера и транзакции:((
class BalanceInteractor:
    def __init__(self, user_service, transaction_service) -> None:
        self.user_service = user_service
        self.transaction_service = transaction_service

    async def set_max_balance(
        self, user: UserModel, save_sum: Decimal
    ) -> ORJSONResponse:
        if (user.max_balance > 0) and (user.max_balance - save_sum > 0):
            await self.transaction_service.open(save_sum=save_sum, user=user)

            return ORJSONResponse(
                status_code=status.HTTP_200_OK, content="Transaction successful open!"
            )

    async def set_balance(self, user: UserModel, save_sum: Decimal) -> ORJSONResponse:
        if (user.max_balance > 0) and (user.max_balance - save_sum > 0):
            await self.transaction_service.open(save_sum=save_sum, user=user)

            return ORJSONResponse(
                status_code=status.HTTP_200_OK, content="Transaction successful open!"
            )

    async def confirm_transaction(
        self, transaction_uuid: UUID, token: str
    ) -> ORJSONResponse:
        if transaction := await self.transaction_service.get_transaction(
            transaction_uuid=transaction_uuid
        ):
            if transaction.service_creator == token:
                await self.transaction_service.close(transaction_uuid=transaction_uuid)

                await self.user_service.set_balance(save_sum=transaction.save_sum)

                return ORJSONResponse(
                    status_code=status.HTTP_200_OK,
                    content="Transaction successful close!",
                )

    async def cancel_transaction(self, transaction_uuid: UUID) -> None:
        if transaction := await self.transaction_service.get_transaction(
            transaction_uuid=transaction_uuid
        ):
            await self.user_service.transaction_cancel(transaction.uuid)
