import uuid
from typing import List, Sequence

from fastapi import Depends

from repositories.bank_account import BankAccountRepository
from models.bank_account import BankAccount
from schemas.bank_account import ListBankAccountOpts


class BankAccountService:
    def __init__(self, account_repo: BankAccountRepository = Depends()):
        self._account_repo = account_repo

    async def create_bank_account(
        self, user_id: uuid.UUID, number: int, balance: float
    ) -> BankAccount:
        return await self._account_repo.create_bank_account(user_id, number, balance)

    async def get_bank_account_by_id(self, account_id: uuid.UUID) -> BankAccount:
        return await self._account_repo.get_bank_account_by_id(account_id)

    async def get_bank_accounts_by_user_id(
        self, user_id: uuid.UUID
    ) -> List[BankAccount]:
        return await self._account_repo.get_bank_accounts_by_user_id(user_id)

    async def list(self, opts: ListBankAccountOpts) -> Sequence[BankAccount]:
        return await self._account_repo.list(opts)

    async def update_bank_account(
        self, account_id: uuid.UUID, data: dict
    ) -> BankAccount:
        return await self._account_repo.update_bank_account(account_id, data)

    async def delete_bank_account(self, account_id: uuid.UUID):
        await self._account_repo.delete_bank_account(account_id)
