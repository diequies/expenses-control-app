from data_ingestion.data_ingestor import DataIngestor
from data_models.data_classes import BankAccount
from data_models.enums import Bank, AccountUser, AccountType, Currency
from utils.aws_helper import get_raw_transactions

if __name__ == '__main__':

    bank_account = BankAccount(
        bank=Bank.MONZO,
        account_user=AccountUser.MARIA,
        account_type=AccountType.DEBIT,
        currency=Currency.POUNDS
    )
    for i in range(1):
        ingestor = DataIngestor(bank_account=bank_account)
        ingestor.load_transactions(f"../data/monzo_maria.csv")
        ingestor.save_transactions()

        print(len(ingestor.transactions))

    # transactions = get_raw_transactions()
    i=1
