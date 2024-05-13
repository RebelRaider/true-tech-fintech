import uuid
from typing import List


from configs.Database import async_session
from errors.errors import ErrEntityNotFound, ErrEntityConflict
from repositories.bank_account import BankAccountRepository
from schemas.active_action import ActiveActionPath
from schemas.bank_account import ListBankAccountOpts
from services.bank_account import BankAccountService
from utils.utils import get_path


async def check_balance(paths: List[ActiveActionPath]) -> str:
    uuid_task = uuid.UUID("d3bae2a5-a188-4418-a629-4374d7e66d39")
    balance_path = get_path(paths, uuid_task)

    if balance_path is None:
        raise ErrEntityConflict(f"there is no task with uuid {uuid_task}")

    number = balance_path.value

    db = async_session()

    bank_account_repo = BankAccountRepository(db)
    bank_account_service = BankAccountService(bank_account_repo)

    bank_accounts = await bank_account_service.list(
        ListBankAccountOpts(number=int(number), limit=100, offset=0)
    )

    if len(bank_accounts) == 0:
        raise ErrEntityNotFound("there is no such bank account")

    return f"На счету {number} сейчас находиться {bank_accounts[0].balance} рублей"
