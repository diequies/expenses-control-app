import pickle

from typing import List

import numpy as np
import pandas as pd
from pandas import DataFrame

from data_models.data_classes import BankAccount, TransactionBase
from data_models.enums import Bank, TransactionSign, AccountType, TransactionType
from utils.aws_helper import get_aws_session, get_raw_transactions_ids
from utils.constants import RAW_TRANSACTIONS_PREFIX, S3_BUCKET


class DataIngestor:
    """ Class to ingest the transaction from different sources """

    def __init__(
            self,
            bank_account: BankAccount,
    ):
        self.bank_account = bank_account
        self.transactions: List[TransactionBase] = []
        self.existing_transactions: List[str] = get_raw_transactions_ids()

    def load_transactions(
            self,
            file_path: str
    ):

        if self.bank_account.bank == Bank.LLOYDS:
            df_raw = pd.read_csv(file_path)
            if self.bank_account.account_type == AccountType.CREDIT:
                self._process_lloyds_credit_data(df=df_raw)
            else:
                self._process_lloyds_debit_data(df=df_raw)
        if self.bank_account.bank == Bank.NATIONWIDE:
            df_raw = pd.read_csv(file_path, header=3, encoding='unicode_escape')
            if self.bank_account.account_type == AccountType.DEBIT:
                self._process_nationwide_debit_data(df=df_raw)
            else:
                self._process_nationwide_credit_data(df=df_raw)
        if self.bank_account.bank == Bank.REVOLUT:
            df_raw = pd.read_csv(file_path)
            self._process_revolut_data(df=df_raw)
        if self.bank_account.bank == Bank.MONZO:
            df_raw = pd.read_csv(file_path)
            self._process_monzo_data(df=df_raw)

    def _process_lloyds_debit_data(
            self,
            df: DataFrame
    ) -> List[TransactionBase]:

        df['transaction_date'] = df['Transaction Date'].apply(
            lambda x: pd.to_datetime(x, format='%d/%m/%Y').date()
        )
        for index, row in df.iterrows():
            date = row['transaction_date']
            if pd.isna(row['Debit Amount']):
                transaction_sign = TransactionSign.CREDIT
                transaction_quantity = row['Credit Amount']
            else:
                transaction_sign = TransactionSign.DEBIT
                transaction_quantity = row ['Debit Amount']
            bank_account = self.bank_account
            transaction_description = row['Transaction Description']
            currency = self.bank_account.currency
            transaction_type = TransactionType.OTHER
            transaction_id = (f"{date}"
                              f"_{transaction_sign.value.get('name')}"
                              f"_{transaction_quantity}"
                              f"_{bank_account.bank.value}"
                              f"_{bank_account.account_type.value}"
                              f"_{bank_account.account_user.value}")
            if transaction_id in self.existing_transactions:
                continue
            self.transactions.append(
                TransactionBase(
                    transaction_id=transaction_id,
                    date=date,
                    transaction_sign=transaction_sign,
                    bank_account=bank_account,
                    transaction_description=transaction_description,
                    transaction_quantity=transaction_quantity,
                    currency=currency,
                    transaction_type=transaction_type
                )
            )
        return self.transactions

    def _process_lloyds_credit_data(
            self,
            df: DataFrame
    ) -> List[TransactionBase]:

        df['transaction_date'] = df['Date'].apply(
            lambda x: pd.to_datetime(x, format='%d/%m/%Y').date()
        )
        for index, row in df.iterrows():
            date = row['transaction_date']
            if row['Amount'] < 0:
                transaction_sign = TransactionSign.DEBIT
            else:
                transaction_sign = TransactionSign.CREDIT
            transaction_quantity = np.abs(row['Amount'])
            bank_account = self.bank_account
            transaction_description = row['Description']
            currency = self.bank_account.currency
            transaction_type = TransactionType.OTHER
            transaction_id = (f"{date}"
                              f"_{transaction_sign.value.get('name')}"
                              f"_{transaction_quantity}"
                              f"_{bank_account.bank.value}"
                              f"_{bank_account.account_type.value}"
                              f"_{bank_account.account_user.value}")
            if transaction_id in self.existing_transactions:
                continue
            self.transactions.append(
                TransactionBase(
                    transaction_id=transaction_id,
                    date=date,
                    transaction_sign=transaction_sign,
                    bank_account=bank_account,
                    transaction_description=transaction_description,
                    transaction_quantity=transaction_quantity,
                    currency=currency,
                    transaction_type=transaction_type
                )
            )
        return self.transactions

    def _process_nationwide_debit_data(
            self,
            df: DataFrame
    ) -> List[TransactionBase]:

        df['transaction_date'] = df['Date'].apply(
            lambda x: pd.to_datetime(x, format='%d %b %Y').date()
        )
        for index, row in df.iterrows():
            date = row['transaction_date']
            if pd.isna(row['Paid out']):
                transaction_sign = TransactionSign.CREDIT
                transaction_quantity = float(row['Paid in'][1:])
            else:
                transaction_sign = TransactionSign.DEBIT
                transaction_quantity = float(row['Paid out'][1:])
            bank_account = self.bank_account
            transaction_description = row['Description']
            currency = self.bank_account.currency
            transaction_type = self._get_transaction_type(row['Transaction type'])
            transaction_id = (f"{date}"
                              f"_{transaction_sign.value.get('name')}"
                              f"_{transaction_quantity}"
                              f"_{bank_account.bank.value}"
                              f"_{bank_account.account_type.value}"
                              f"_{bank_account.account_user.value}")
            if transaction_id in self.existing_transactions:
                continue
            self.transactions.append(
                TransactionBase(
                    transaction_id=transaction_id,
                    date=date,
                    transaction_sign=transaction_sign,
                    bank_account=bank_account,
                    transaction_description=transaction_description,
                    transaction_quantity=transaction_quantity,
                    currency=currency,
                    transaction_type=transaction_type
                )
            )
        return self.transactions

    def _process_nationwide_credit_data(
            self,
            df: DataFrame
    ) -> List[TransactionBase]:

        df['transaction_date'] = df['Date'].apply(
            lambda x: pd.to_datetime(x, format='%d %b %Y').date()
        )
        for index, row in df.iterrows():
            date = row['transaction_date']
            if pd.isna(row['Paid out']):
                transaction_sign = TransactionSign.CREDIT
                transaction_quantity = float(row['Paid in'][1:])
            else:
                transaction_sign = TransactionSign.DEBIT
                transaction_quantity = float(row['Paid out'][1:])
            bank_account = self.bank_account
            transaction_description = row['Transactions']
            currency = self.bank_account.currency
            transaction_type = TransactionType.OTHER
            transaction_id = (f"{date}"
                              f"_{transaction_sign.value.get('name')}"
                              f"_{transaction_quantity}"
                              f"_{bank_account.bank.value}"
                              f"_{bank_account.account_type.value}"
                              f"_{bank_account.account_user.value}")
            if transaction_id in self.existing_transactions:
                continue
            self.transactions.append(
                TransactionBase(
                    transaction_id=transaction_id,
                    date=date,
                    transaction_sign=transaction_sign,
                    bank_account=bank_account,
                    transaction_description=transaction_description,
                    transaction_quantity=transaction_quantity,
                    currency=currency,
                    transaction_type=transaction_type
                )
            )
        return self.transactions

    def _process_revolut_data(
            self,
            df: DataFrame
    ) -> List[TransactionBase]:

        df['transaction_date'] = df['Started Date'].apply(
            lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S').date()
        )
        for index, row in df.iterrows():
            date = row['transaction_date']
            if row['Amount'] < 0:
                transaction_sign = TransactionSign.DEBIT
            else:
                transaction_sign = TransactionSign.CREDIT
            transaction_quantity = np.abs(row['Amount']) + np.abs(row['Fee'])
            bank_account = self.bank_account
            transaction_description = row['Description']
            currency = self.bank_account.currency
            transaction_type = self._get_transaction_type(row['Type'])
            transaction_id = (f"{date}"
                              f"_{transaction_sign.value.get('name')}"
                              f"_{transaction_quantity}"
                              f"_{bank_account.bank.value}"
                              f"_{bank_account.account_type.value}"
                              f"_{bank_account.account_user.value}")
            if transaction_id in self.existing_transactions:
                continue
            self.transactions.append(
                TransactionBase(
                    transaction_id=transaction_id,
                    date=date,
                    transaction_sign=transaction_sign,
                    bank_account=bank_account,
                    transaction_description=transaction_description,
                    transaction_quantity=transaction_quantity,
                    currency=currency,
                    transaction_type=transaction_type
                )
            )
        return self.transactions

    def _process_monzo_data(
            self,
            df: DataFrame
    ) -> List[TransactionBase]:

        df['transaction_date'] = df['Date'].apply(
            lambda x: pd.to_datetime(x, format='%d/%m/%Y').date()
        )
        for index, row in df.iterrows():
            date = row['transaction_date']
            if row['Amount'] < 0:
                transaction_sign = TransactionSign.DEBIT
            else:
                transaction_sign = TransactionSign.CREDIT
            transaction_quantity = np.abs(row['Amount'])
            bank_account = self.bank_account
            transaction_description = (f"{row['Name']}. {row['Category']}. "
                                       f"{row['Notes and #tags']}. "
                                       f"{row['Description']}")
            currency = self.bank_account.currency
            transaction_type = self._get_transaction_type(row['Type'])
            transaction_id = (f"{date}"
                              f"_{transaction_sign.value.get('name')}"
                              f"_{transaction_quantity}"
                              f"_{bank_account.bank.value}"
                              f"_{bank_account.account_type.value}"
                              f"_{bank_account.account_user.value}")
            if transaction_id in self.existing_transactions:
                continue
            self.transactions.append(
                TransactionBase(
                    transaction_id=transaction_id,
                    date=date,
                    transaction_sign=transaction_sign,
                    bank_account=bank_account,
                    transaction_description=transaction_description,
                    transaction_quantity=transaction_quantity,
                    currency=currency,
                    transaction_type=transaction_type
                )
            )
        return self.transactions

    def _get_transaction_type(self, transaction_type_text: str) -> TransactionType:
        for transaction_type in TransactionType:
            for transaction_string \
                    in transaction_type.value.get(self.bank_account.bank.value, []):
                if transaction_string.lower() in transaction_type_text.lower():
                    return transaction_type
        return TransactionType.OTHER

    def save_transactions(self) -> None:
        session = get_aws_session()
        s3_client = session.client('s3')
        for transaction in self.transactions:
            pickle_file = pickle.dumps(transaction)

            object_name = RAW_TRANSACTIONS_PREFIX + transaction.transaction_id + '.pkl'

            s3_client.put_object(
                Bucket=S3_BUCKET,
                Key=object_name,
                Body=pickle_file,
            )
