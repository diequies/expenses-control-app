from dataclasses import dataclass
from datetime import datetime

from data_models.enums import TransactionType, AccountUser, AccountType, Bank, Currency, \
    CategoryLevelOne, CategoryLevelTwo, CategoryLevelThree


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
    transaction_type: TransactionType
    bank_account: BankAccount
    transaction_description: str
    transaction_quantity: float
    currency: Currency


@dataclass
class TransactionProcessed(TransactionBase):
    category_level_one: CategoryLevelOne
    category_level_two: CategoryLevelTwo
    category_level_three: CategoryLevelThree
