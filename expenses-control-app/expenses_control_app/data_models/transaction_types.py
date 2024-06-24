from dataclasses import dataclass
from datetime import datetime

from data_models.enums import TransactionType, AccountUser, AccountType, Bank, Currency


@dataclass
class BankAccount:
    bank: Bank
    account_user: AccountUser
    account_type: AccountType
    account_number: str
    currency: Currency


@dataclass
class TransactionBase:
    date: datetime.date
    transaction_type: TransactionType
    bank_account: BankAccount
    transaction_description: str
    transaction_quantity: float
    currency: Currency
