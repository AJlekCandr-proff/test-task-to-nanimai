from sqlalchemy import Pool, AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from test_app.infrastucture.common.base_entities.singleton import Singleton


class AlchemyGateway:
    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        database: str,
        pool: Pool = AsyncAdaptedQueuePool,
        dialect: str = "asyncpg",
    ) -> None:
        self.dialect = dialect
        self.user = user
        self._password = password
        self.host = host
        self.port = port
        self.database = database

        self._engine = create_async_engine(
            url=self.get_url,
            poolclass=pool,
        )

        self._autocommit_session = self._engine.execution_options(
            isolation_level="AUTOCOMMIT"
        )

        self._transactional_session = async_sessionmaker(
            bind=self._engine,
            expire_on_commit=False,
        )

        self._async_session_factory = async_sessionmaker(self._autocommit_session)

    @property
    def get_url(self) -> str:
        return f"postgresql+{self.dialect}://{self.user}:{self._password}@{self.host}:{self.port}/{self.database}"

    @property
    def transactional_session(self) -> async_sessionmaker:
        return self._transactional_session

    @property
    def async_session_factory(self) -> async_sessionmaker:
        return self._async_session_factory
