from typing import List

import pandas as pd
from pandas import DataFrame

from data_models.data_classes import BankAccount, TransactionBase
from data_models.enums import Bank, TransactionType
from utils.aws_helper import get_raw_transactions


class DataIngestor:
    """ Class to ingest the transaction from different sources """

    def __init__(
            self,
            bank_account: BankAccount,
    ):
        self.bank_account = bank_account
        self.transactions: List[TransactionBase] = []
        self.existing_transactions: List[str] = get_raw_transactions()

    def load_transactions(
            self,
            file_path: str
    ):
        df_raw = pd.read_csv(file_path)

        if self.bank_account.bank == Bank.LLOYDS:
            self._process_lloyds_data(df=df_raw)

    def _process_lloyds_data(
            self,
            df: DataFrame
    ) -> List[TransactionBase]:

        df['transaction_date'] = df['Transaction Date'].apply(
            lambda x: pd.to_datetime(x, format='%d/%m/%Y').date()
        )
        for index, row in df.iterrows():
            date = row['transaction_date']
            if pd.isna(row['Debit Amount']):
                transaction_type = TransactionType.CREDIT
                transaction_quantity = row['Credit Amount']
            else:
                transaction_type = TransactionType.DEBIT
                transaction_quantity = row ['Debit Amount']
            bank_account = self.bank_account
            transaction_description = row['Transaction Description']
            currency = self.bank_account.currency
            transaction_id = (f"{date}_{transaction_type}_{transaction_quantity}"
                              f"_{bank_account.bank}_{bank_account.account_type}"
                              f"_{bank_account.account_user}")
            if transaction_id in self.existing_transactions:
                continue
            self.transactions.append(
                TransactionBase(
                    transaction_id=transaction_id,
                    date=date,
                    transaction_type=transaction_type,
                    bank_account=bank_account,
                    transaction_description=transaction_description,
                    transaction_quantity=transaction_quantity,
                    currency=currency
                )
            )
        return self.transactions

    def save_transactions(self) -> None:
        pass
