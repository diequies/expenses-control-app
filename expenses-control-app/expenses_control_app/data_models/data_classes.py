from dataclasses import dataclass
from datetime import datetime

from data_models.enums import TransactionSign, AccountUser, AccountType, Bank, Currency, \
    CategoryLevelOne, CategoryLevelTwo, CategoryLevelThree, TransactionType


@dataclass
class BankAccount:
    bank: Bank
    account_user: AccountUser
    account_type: AccountType
    currency: Currency


@dataclass
class TransactionBase:
    transaction_id: str
    date: datetime.date
    transaction_sign: TransactionSign
    bank_account: BankAccount
    transaction_description: str
    transaction_quantity: float
    currency: Currency
    transaction_type: TransactionType


@dataclass
class TransactionProcessed(TransactionBase):
    category_level_one: CategoryLevelOne
    category_level_two: CategoryLevelTwo
    category_level_three: CategoryLevelThree
