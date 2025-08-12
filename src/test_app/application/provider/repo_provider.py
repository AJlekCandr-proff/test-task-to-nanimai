from dishka import FromDishka, Provider, Scope, provide

from test_app.gateways.alchemy_gateway import AlchemyGateway
from test_app.infrastucture.database.repo.transaction_repo import (
    TransactionWriteRepository,
    TransactionReadRepository,
)
from test_app.infrastucture.database.repo.user_repo import (
    UserWriteRepository,
    UserReadRepository,
)


class RepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_transaction_read_repo(
        self,
        gateway: FromDishka[AlchemyGateway],
    ) -> TransactionReadRepository:
        return TransactionReadRepository(gateway=gateway)

    @provide(scope=Scope.REQUEST)
    async def get_transaction_write_repo(
        self,
        gateway: FromDishka[AlchemyGateway],
    ) -> TransactionWriteRepository:
        return TransactionWriteRepository(gateway=gateway)

    @provide(scope=Scope.REQUEST)
    async def get_user_read_repo(
        self,
        gateway: FromDishka[AlchemyGateway],
    ) -> UserReadRepository:
        return UserReadRepository(gateway=gateway)

    @provide(scope=Scope.REQUEST)
    async def get_user_write_repo(
        self,
        gateway: FromDishka[AlchemyGateway],
    ) -> UserWriteRepository:
        return UserWriteRepository(gateway=gateway)
