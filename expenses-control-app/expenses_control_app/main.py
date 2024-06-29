from data_ingestion.data_ingestor import DataIngestor
from data_models.data_classes import BankAccount
from data_models.enums import Bank, AccountUser, AccountType, Currency
from utils.aws_helper import get_raw_transactions

if __name__ == '__main__':

    bank_account = BankAccount(
        bank=Bank.MONZO,
        account_user=AccountUser.DIEGO,
        account_type=AccountType.DEBIT,
        currency=Currency.POUNDS
    )

    ingestor = DataIngestor(bank_account=bank_account)
    ingestor.load_transactions("../data/monzo.csv")
    ingestor.save_transactions()

    transactions = get_raw_transactions()
