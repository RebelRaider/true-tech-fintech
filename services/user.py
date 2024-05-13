import uuid
from typing import List

from fastapi import Depends
from repositories.user import UserRepository
from models.user import User


class UserService:
    def __init__(self, user_repo: UserRepository = Depends()):
        self._user_repo = user_repo

    async def create_user(
        self, first_name: str, last_name: str, surname: str, email: str, phone: str
    ) -> User:
        return await self._user_repo.create_user(
            first_name, last_name, surname, email, phone
        )

    async def get_user_by_id(self, user_id: uuid.UUID) -> User:
        return await self._user_repo.get_user_by_id(user_id)

    async def get_all_users(self) -> List[User]:
        return await self._user_repo.get_all_users()

    async def update_user(self, user_id: uuid.UUID, data: dict) -> User:
        return await self._user_repo.update_user(user_id, data)

    async def delete_user(self, user_id: uuid.UUID):
        await self._user_repo.delete_user(user_id)
