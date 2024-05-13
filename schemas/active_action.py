import uuid
from typing import List, Dict

from pydantic import BaseModel


class CreateActiveActionRepoOpts(BaseModel):
    user_id: uuid.UUID
    action_id: uuid.UUID


class CreateActiveActionServiceOpts(BaseModel):
    user_id: uuid.UUID
    action_id: uuid.UUID


class AddActiveActionPathRequest(BaseModel):
    node_id: uuid.UUID
    value: str


class ActiveActionPath(BaseModel):
    node_id: uuid.UUID
    value: str
    order: int


class CreateActiveActionRequest(BaseModel):
    user_id: uuid.UUID
    action_id: uuid.UUID


class ActiveActionResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    action_id: uuid.UUID
    path: List | Dict


class DoAllRequest(BaseModel):
    next_node_id: uuid.UUID
    value: str
