import uuid

from pydantic import BaseModel


class ListBankAccountOpts(BaseModel):
    user_id: uuid.UUID | None = None
    number: int | None = None
    limit: int = 100
    offset: int = 0
