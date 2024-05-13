import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.BaseModel import EntityMeta


class BankAccount(EntityMeta):
    __tablename__ = "bank_account"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))
    number: Mapped[int]
    balance: Mapped[float]
