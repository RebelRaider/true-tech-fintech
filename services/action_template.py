import uuid
from typing import Sequence

from fastapi import Depends
from sqlalchemy_utils import Ltree

from errors.errors import ErrBadRequest
from models.action_template import ActionTemplate
from repositories.action_template import ActionTemplateRepository


class ActionTemplateService:
    def __init__(self, repo: ActionTemplateRepository = Depends()):
        self._repo = repo

    async def create_root_action(self, name: str) -> None:
        await self._repo.create_root_action(name)

    async def create_node_action(self, id: uuid.UUID, name: str) -> None:
        node = await self._repo.get_node_by_id(id)

        await self._repo.create_node_action(name, node.path)

    async def get_root_actions(self) -> Sequence[ActionTemplate]:
        action = await self._repo.get_root_actions()

        return action

    async def get_next_nodes(self, id: uuid.UUID) -> Sequence[ActionTemplate]:
        node = await self._repo.get_node_by_id(id)
        if node is None:
            raise ErrBadRequest("Node not found")

        return await self._repo.get_next_nodes(node.path)

    async def get_node_by_id(self, id: uuid.UUID) -> ActionTemplate:
        result = await self._repo.get_node_by_id(id)
        return result

    async def get_by_path(self, path: Ltree) -> ActionTemplate:
        return await self._repo.get_node_by_path(path)
