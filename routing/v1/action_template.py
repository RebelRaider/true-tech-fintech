import uuid
from typing import List

from fastapi import APIRouter, Depends

from schemas.action_template import (
    CreateRootActionRequest,
    ActionResponse,
    CreatNodeActionRequest,
)
from services.action_template import ActionTemplateService

router = APIRouter(prefix="/api/v1/action_template", tags=["action_template"])


@router.post(
    "/create_root",
    summary="создание корня для action",
)
async def create_root(
    action: CreateRootActionRequest, action_service: ActionTemplateService = Depends()
):
    await action_service.create_root_action(action.name)


@router.post(
    "/create_node",
    summary="создание ноды для action",
)
async def create_node(
    action: CreatNodeActionRequest, action_service: ActionTemplateService = Depends()
):
    await action_service.create_node_action(action.parent_id, action.name)


@router.get(
    "/root_actions",
    summary="получение всех корневых значений action",
    response_model=List[ActionResponse],
)
async def get_root_actions(action_service: ActionTemplateService = Depends()):
    return await action_service.get_root_actions()


@router.get(
    "/next_nodes/{id}",
    summary="получение всех детей action с глубиной 1",
    response_model=List[ActionResponse],
)
async def get_next_nodes(
    id: uuid.UUID, action_service: ActionTemplateService = Depends()
):
    return await action_service.get_next_nodes(id)
