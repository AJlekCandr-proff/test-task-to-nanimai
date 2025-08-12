from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, func, Enum, String, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from test_app.domain.transaction.enums.status_transaction_enum import (
    StatusTransactionEnum,
)

from test_app.infrastucture.database.models import Base

if TYPE_CHECKING:
    from test_app.infrastucture.database.models import User


class Transaction(Base):
    date_open: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    status: Mapped[StatusTransactionEnum] = mapped_column(
        Enum(StatusTransactionEnum), default=StatusTransactionEnum.OPEN
    )

    date_close: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True, onupdate=func.now()
    )

    service_creator: Mapped[str] = mapped_column(
        String(35), comment="Токен для сервиса-создателя"
    )

    save_sum: Mapped[str] = mapped_column(
        String, comment="Сумма, которая была взята во время транзакции"
    )

    user_uuid: Mapped[UUID] = mapped_column(ForeignKey("users.uuid"))

    user: Mapped["User"] = relationship("User", back_populates="transactions")
