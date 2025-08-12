import re
from uuid import uuid4

from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:  # noqa
        name = re.sub(
            r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "_", cls.__name__
        )

        return name.lower()

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        index=True,
        primary_key=True,
        default=uuid4,
        comment="Уникальный UUID записи",
    )
