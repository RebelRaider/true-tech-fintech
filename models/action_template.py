import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import LtreeType

from models.BaseModel import EntityMeta


class ActionTemplate(EntityMeta):
    __tablename__ = "action_template"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    is_head: Mapped[bool]
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(server_default=None, nullable=True)
    path = mapped_column(LtreeType, nullable=False)
    import_path: Mapped[str] = mapped_column(nullable=True)
    import_func: Mapped[str] = mapped_column(nullable=True)
