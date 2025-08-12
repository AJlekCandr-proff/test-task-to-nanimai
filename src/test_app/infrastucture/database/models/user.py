from tokenize import String

from sqlalchemy.orm import Mapped, mapped_column

from test_app.infrastucture.database.models.base import Base


class User(Base):
    name: Mapped[str] = mapped_column(String, comment="Имя пользователя")

    balance: Mapped[str] = mapped_column(String, comment="Баланс пользователя")
    max_balance: Mapped[str] = mapped_column(
        String, comment="Максимально возможный баланс пользователя"
    )
