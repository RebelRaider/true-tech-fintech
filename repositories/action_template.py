import uuid
from typing import Sequence

from fastapi import Depends
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_utils import Ltree

from configs.Database import get_db_connection
from errors.errors import ErrBadRequest
from models.action_template import ActionTemplate
from models.active_action import ActiveAction
from utils.utils import nlevel, uuid_to_ltree


class ActionTemplateRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_connection)):
        self._db = db

    async def create_root_action(self, name: str):
        action_id = uuid.uuid4()
        root = ActionTemplate(
            id=action_id,
            name=name,
            is_head=True,
            path=uuid_to_ltree(action_id),
        )

        self._db.add(root)
        await self._db.commit()

    async def create_node_action(self, name: str, path: Ltree):
        actions = await self.get_next_nodes(path)

        nodes = [action.name for action in actions]

        if name in nodes:
            raise ErrBadRequest(f"the node {name} is already in path {path}")

        node = ActionTemplate(
            id=uuid.uuid4(),
            name=name,
            path=path + uuid_to_ltree(uuid.uuid4()),
            is_head=False,
        )

        self._db.add(node)
        await self._db.commit()

    async def get_next_nodes(self, path: Ltree) -> Sequence[ActionTemplate]:
        query = select(ActionTemplate).filter(
            ActionTemplate.path.descendant_of(path),
            func.nlevel(ActionTemplate.path) == nlevel(path) + 5,
        )

        result = await self._db.execute(query)

        return result.scalars().all()

    async def get_node_by_id(self, id: uuid.UUID) -> ActionTemplate:
        query = select(ActionTemplate).where(ActionTemplate.id == id)

        result = await self._db.execute(query)

        return result.scalar()

    async def get_root_actions(self) -> Sequence[ActionTemplate]:
        flag = True
        query = select(ActionTemplate).where(ActionTemplate.is_head == flag)

        result = await self._db.execute(query)

        return result.scalars().all()

    async def get_node_by_path(self, path: Ltree) -> ActionTemplate:
        query = select(ActiveAction).where(ActiveAction.path == path)

        row = await self._db.execute(query)

        return row.scalar()
