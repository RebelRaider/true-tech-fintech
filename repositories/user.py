import uuid
from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.user import User
from configs.Database import get_async_session


class UserRepository:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def create_user(
        self, first_name: str, last_name: str, surname: str, email: str, phone: str
    ) -> User:
        new_user = User(
            id=uuid.uuid4(),
            first_name=first_name,
            last_name=last_name,
            surname=surname,
            email=email,
            phone=phone,
        )
        await self.session.add(new_user)
        await self.session.commit()
        return new_user

    async def get_user_by_id(self, user_id: uuid.UUID) -> User:
        statement = select(User).where(User.id == user_id)
        result = await self.session.execute(statement)
        user = result.scalars().first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        return user

    async def get_all_users(self) -> List[User]:
        statement = select(User)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def update_user(self, user_id: uuid.UUID, data: dict) -> User:
        user = await self.get_user_by_id(user_id)
        for key, value in data.items():
            setattr(user, key, value)
        await self.session.commit()
        return user

    async def delete_user(self, user_id: uuid.UUID):
        user = await self.get_user_by_id(user_id)
        await self.session.delete(user)
        await self.session.commit()
