from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import String, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship

from test_app.infrastucture.database.models import Base

if TYPE_CHECKING:
    from test_app.infrastucture.database.models import Transaction


class User(Base):
    name: Mapped[str] = mapped_column(String, comment="Имя пользователя")

    balance: Mapped[Decimal] = mapped_column(
        DECIMAL(precision=10, scale=2),
        default=Decimal("0.00"),
        comment="Баланс пользователя",
    )

    max_balance: Mapped[Decimal] = mapped_column(
        DECIMAL(precision=10, scale=2),
        default=Decimal("1000.00"),
        comment="Максимально возможный баланс пользователя",
    )

    transactions: Mapped["Transaction"] = relationship(
        "Transaction", back_populates="user"
    )
