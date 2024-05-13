import uuid

from pydantic import BaseModel, field_validator


class CreateRootActionRequest(BaseModel):
    name: str
    description: str


class CreatNodeActionRequest(BaseModel):
    parent_id: uuid.UUID
    name: str
    description: str


class ActionTemplateResponse(BaseModel):
    id: uuid.UUID | None
    name: str


class ActionResponse(BaseModel):
    id: uuid.UUID
    name: str
    is_head: bool
    description: str
    path: str

    @field_validator("path", mode="before")
    def path_to_string(cls, value):
        # Convert the ltree value to a string, handling SQLAlchemy ltree type
        if isinstance(value, str):
            return value
        # Assuming value comes as an ltree object or something else
        return str(value)
