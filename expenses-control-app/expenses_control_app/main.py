from data_ingestion.data_ingestor import DataIngestor
from data_models.data_classes import BankAccount
from data_models.enums import Bank, AccountUser, AccountType, Currency

if __name__ == '__main__':

    bank_account = BankAccount(
        bank=Bank.LLOYDS,
        account_user=AccountUser.DIEGO,
        account_type=AccountType.PERSONAL,
        currency=Currency.POUNDS
    )

    ingestor = DataIngestor(bank_account=bank_account)
    ingestor.load_transactions("../data/data_temp.csv")
