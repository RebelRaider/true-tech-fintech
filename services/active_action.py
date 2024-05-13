import uuid
from typing import List, Sequence

from fastapi import Depends

from models.action_template import ActionTemplate
from models.active_action import ActiveAction
from repositories.active_action import ActiveActionRepository
from schemas.active_action import (
    CreateActiveActionServiceOpts,
    CreateActiveActionRepoOpts,
    ActiveActionPath,
    AddActiveActionPathRequest,
)
from services.action_template import ActionTemplateService
from utils.utils import string_path_to_json


class ActiveActionService:
    def __init__(
        self,
        repo: ActiveActionRepository = Depends(),
        action_template: ActionTemplateService = Depends(),
    ):
        self._repo = repo
        self._action_template = action_template

    async def create_active_action(
        self, opts: CreateActiveActionServiceOpts
    ) -> ActiveAction:
        return await self._repo.create_active_action(
            CreateActiveActionRepoOpts(user_id=opts.user_id, action_id=opts.action_id)
        )

    async def get_by_id(self, id: uuid.UUID) -> ActiveAction:
        result = await self._repo.get_by_id(id)

        result.path = string_path_to_json(result.path)

        return result

    async def update_path(
        self, id: uuid.UUID, user_paths: List[AddActiveActionPathRequest]
    ) -> None:
        active_task = await self._repo.get_by_id(id)

        active_task.path = string_path_to_json(active_task.path)

        repo_paths = [
            ActiveActionPath(
                node_id=uuid.UUID(path["node_id"]),
                value=path["value"],
                order=path["order"],
            )
            for path in active_task.path
        ]

        repo_paths.sort(key=lambda x: x.order)

        order = 0 if len(repo_paths) == 0 else repo_paths[-1].order + 1

        save_path = []

        for user_path in user_paths:
            save_path.append(
                ActiveActionPath(
                    node_id=user_path.node_id, value=user_path.value, order=order
                )
            )

        await self._repo.update_active_path(id, save_path)

    async def get_next_tasks(self, id: uuid.UUID) -> Sequence[ActionTemplate]:
        active_task = await self.get_by_id(id)

        path = [
            ActiveActionPath(
                node_id=path["node_id"],
                value=path["value"],
                order=path["order"],
            )
            for path in active_task.path
        ]

        path.sort(key=lambda x: x.order)

        template = await self._action_template.get_node_by_id(path[-1].node_id)

        next_nodes = await self._action_template.get_next_nodes(template.id)

        return next_nodes
