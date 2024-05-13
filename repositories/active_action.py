import uuid
from datetime import datetime
from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from configs.Database import get_db_connection
from errors.errors import ErrBadRequest, ErrEntityNotFound
from models.active_action import ActiveAction
from schemas.active_action import (
    CreateActiveActionRepoOpts,
    ActiveActionPath,
)
from services.action_template import ActionTemplateService
from utils.utils import string_path_to_json


class ActiveActionRepository:
    def __init__(
        self,
        db: AsyncSession = Depends(get_db_connection),
        action_template: ActionTemplateService = Depends(),
    ):
        self._db = db
        self._action_template = action_template

    async def create_active_action(
        self, opts: CreateActiveActionRepoOpts
    ) -> ActiveAction:
        node = await self._action_template.get_node_by_id(opts.action_id)

        if not node.is_head:
            raise ErrBadRequest("the node for active action must be an head")

        active_action = ActiveAction(
            id=uuid.uuid4(),
            user_id=opts.user_id,
            action_id=opts.action_id,
            path=[
                ActiveActionPath(
                    node_id=opts.action_id, value=datetime.now().__str__(), order=0
                ).model_dump_json()
            ],
        )

        self._db.add(active_action)
        await self._db.commit()

        return active_action

    async def get_by_id(self, id: uuid.UUID) -> ActiveAction | None:
        query = select(ActiveAction).where(ActiveAction.id == id)

        row = await self._db.execute(query)

        result = row.scalar()

        if result is None:
            raise ErrEntityNotFound(f"there is no active action with id {id}")

        return result

    async def update_active_path(
        self, id: uuid.UUID, fields: List[ActiveActionPath]
    ) -> None:
        active_action = await self.get_by_id(id)

        active_action.path = string_path_to_json(active_action.path)

        active_action.path = active_action.path + [
            field.model_dump_json() for field in fields
        ]

        await self._db.commit()
