from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from test_app.infrastucture.database.models import Base

if TYPE_CHECKING:
    from test_app.infrastucture.database.models import Transaction


class User(Base):
    name: Mapped[str] = mapped_column(String, comment="Имя пользователя")

    balance: Mapped[str] = mapped_column(
        String, default="0", comment="Баланс пользователя"
    )

    max_balance: Mapped[str] = mapped_column(
        String, default="1000", comment="Максимально возможный баланс пользователя"
    )

    transactions: Mapped["Transaction"] = relationship(
        "Transaction", back_populates="user"
    )
