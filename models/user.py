import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.BaseModel import EntityMeta
from models.bank_account import BankAccount


class User(EntityMeta):
    __tablename__ = "user"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str] = mapped_column(unique=True)

    bank_account: Mapped[list["BankAccount"]] = relationship()
