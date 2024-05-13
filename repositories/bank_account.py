import uuid
from typing import List, Sequence

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.bank_account import BankAccount
from configs.Database import get_db_connection
from schemas.bank_account import ListBankAccountOpts


class BankAccountRepository:
    def __init__(self, session: AsyncSession = Depends(get_db_connection)):
        self.session = session

    async def create_bank_account(
        self, user_id: uuid.UUID, number: int, balance: float
    ) -> BankAccount:
        new_bank_account = BankAccount(
            id=uuid.uuid4(), user_id=user_id, number=number, balance=balance
        )
        await self.session.add(new_bank_account)
        await self.session.commit()
        return new_bank_account

    async def get_bank_account_by_id(self, account_id: uuid.UUID) -> BankAccount:
        statement = select(BankAccount).where(BankAccount.id == account_id)
        result = await self.session.execute(statement)
        account = result.scalars().first()
        if not account:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Bank account not found"
            )
        return account

    async def list(self, opts: ListBankAccountOpts) -> Sequence[BankAccount]:
        query = select(BankAccount).limit(opts.limit).offset(opts.offset)

        if opts.number is not None:
            query = query.where(BankAccount.number == opts.number)

        if opts.user_id is not None:
            query = query.where(BankAccount.user_id == opts.user_id)

        result = await self.session.execute(query)

        return result.scalars().all()

    async def get_bank_accounts_by_user_id(
        self, user_id: uuid.UUID
    ) -> List[BankAccount]:
        statement = select(BankAccount).where(BankAccount.user_id == user_id)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def update_bank_account(
        self, account_id: uuid.UUID, data: dict
    ) -> BankAccount:
        account = await self.get_bank_account_by_id(account_id)
        for key, value in data.items():
            setattr(account, key, value)
        await self.session.commit()
        return account

    async def delete_bank_account(self, account_id: uuid.UUID):
        account = await self.get_bank_account_by_id(account_id)
        await self.session.delete(account)
        await self.session.commit()
