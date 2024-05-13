from pydantic import BaseModel
from fastapi import UploadFile
import uuid


class MlRequest(BaseModel):
    action_id: uuid.UUID
    voice: UploadFile


class MlResponse(BaseModel):
    command: str
