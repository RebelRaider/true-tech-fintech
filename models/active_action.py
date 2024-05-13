import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from models.BaseModel import EntityMeta


class ActiveAction(EntityMeta):
    __tablename__ = "active_action"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
    action_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("action_template.id"), nullable=False
    )
    path = mapped_column(JSONB, nullable=True)
