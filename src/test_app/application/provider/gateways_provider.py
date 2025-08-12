from dishka import Provider, provide, Scope

from test_app.gateways.alchemy_gateway import AlchemyGateway
from test_app.application.config import settings


class GatewaysProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_sqlalchemy_adapter(self) -> AlchemyGateway:
        return AlchemyGateway(
            dialect=settings.DATABASE.DIALECT,
            host=settings.DATABASE.HOST,
            user=settings.DATABASE.USER,
            password=settings.DATABASE.PASSWORD,
            port=settings.DATABASE.PORT,
            database=settings.DATABASE.DATABASE,
        )
