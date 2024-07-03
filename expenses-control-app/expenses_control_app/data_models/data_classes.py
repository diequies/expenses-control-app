from dataclasses import dataclass
from datetime import datetime

from data_models.enums import (TransactionSign, AccountUser, AccountType, Bank,
                               Currency, CategoryLevelOne, CategoryLevelTwo,
                               CategoryLevelThree, TransactionType)


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
    category_level_one: str
    category_level_two: str
    category_level_three: str

    @classmethod
    def from_transaction_base(
            cls,
            transaction_base: TransactionBase,
            category_level_one: CategoryLevelOne,
            category_level_two: CategoryLevelTwo,
            category_level_three: CategoryLevelThree
    ):
        return cls(
            transaction_id=transaction_base.transaction_id,
            date=transaction_base.date,
            transaction_sign=transaction_base.transaction_sign,
            bank_account=transaction_base.bank_account,
            transaction_description=transaction_base.transaction_description,
            transaction_quantity=transaction_base.transaction_quantity,
            currency=transaction_base.currency,
            transaction_type=transaction_base.transaction_type,
            category_level_one=category_level_one.value.get('name'),
            category_level_two=category_level_two.value.get('name'),
            category_level_three=category_level_three.value.get('name')
        )
