import asyncio
from datetime import datetime, timedelta

from test_app.application.interactors.balance_interactor import BalanceInteractor


async def check_expired_transactions(
    transaction_service, interactor_balance: BalanceInteractor
) -> None:
    while True:
        for transaction in await transaction_service.get_transactions():
            if datetime.now() > transaction.date_open + timedelta(hours=1):
                await interactor_balance.cancel_transaction(
                    transaction_uuid=transaction.uuid
                )

        await asyncio.sleep(120)
