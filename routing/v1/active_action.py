import uuid
from typing import List

from fastapi import APIRouter, Depends

from schemas.action_template import ActionTemplateResponse
from schemas.active_action import (
    CreateActiveActionRequest,
    CreateActiveActionServiceOpts,
    ActiveActionPath,
    AddActiveActionPathRequest,
    DoAllRequest,
    ActiveActionResponse,
)
from services.action_template import ActionTemplateService
from services.active_action import ActiveActionService
from utils.utils import import_func

router = APIRouter(prefix="/api/v1/active_action", tags=["active_action"])


@router.post(
    "/", summary="создание пустого active action", response_model=ActiveActionResponse
)
async def create_root(
    action: CreateActiveActionRequest, action_service: ActiveActionService = Depends()
):
    return await action_service.create_active_action(
        CreateActiveActionServiceOpts(
            user_id=action.user_id,
            action_id=action.action_id,
        )
    )


@router.patch(
    "/fields/{id}",
    summary="добавление нового значения в поле",
)
async def update_field(
    action_path: List[AddActiveActionPathRequest],
    id: uuid.UUID,
    action_service: ActiveActionService = Depends(),
):
    await action_service.update_path(id, action_path)


@router.get(
    "/next_tasks/{id}",
    summary="Получение следующих таксок по active action",
    response_model=List[ActionTemplateResponse],
)
async def get_next_tasks(
    id: uuid.UUID, action_service: ActiveActionService = Depends()
):
    return await action_service.get_next_tasks(id)


@router.post(
    "/do_all/{action_id}",
    summary="делает все",
    response_model=List[ActionTemplateResponse],
)
async def do_all(
    action_id: uuid.UUID,
    req: DoAllRequest,
    active_action_service: ActiveActionService = Depends(),
    action_template: ActionTemplateService = Depends(),
):
    active_action = await active_action_service.get_by_id(action_id)

    repo_paths = [
        ActiveActionPath(
            node_id=uuid.UUID(path["node_id"]),
            value=path["value"],
            order=path["order"],
        )
        for path in active_action.path
    ]

    repo_paths.sort(key=lambda x: x.order)

    await active_action_service.update_path(
        action_id,
        [AddActiveActionPathRequest(node_id=req.next_node_id, value=req.value)],
    )

    next_tasks = await active_action_service.get_next_tasks(action_id)

    if len(next_tasks) == 0:
        template = await action_template.get_node_by_id(repo_paths[0].node_id)

        func = import_func(template.import_path, template.import_func)

        answer = await func(repo_paths)

        return [ActionTemplateResponse(id=None, name=answer)]

    return next_tasks
