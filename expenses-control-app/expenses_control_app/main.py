from os import listdir
from os.path import isfile, join

from data_ingestion.data_ingestor import DataIngestor
from data_models.data_classes import BankAccount
from data_models.enums import Bank, AccountUser, AccountType, Currency
from data_processing.data_processor import process_transactions
from utils.aws_helper import get_raw_transactions

if __name__ == '__main__':

    # my_path = "../data/raw"
    #
    # onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    #
    # for file_name in onlyfiles:
    #     divided_name = file_name.split(".")[0].split("_")
    #     bank = Bank.get_account_bank_string(divided_name[0])
    #     account_user = AccountUser.get_account_user_from_string(divided_name[1])
    #     account_type = AccountType.get_account_type_from_string(divided_name[2])
    #     currency_name = Currency.get_currency_from_string(divided_name[3])
    #
    #     bank_account = BankAccount(
    #         bank=bank,
    #         account_user=account_user,
    #         account_type=account_type,
    #         currency=currency_name
    #     )
    #
    #     ingestor = DataIngestor(bank_account=bank_account)
    #     ingestor.load_transactions(f"../data/raw/{file_name}")
    #     ingestor.save_transactions()
    #
    #     print(file_name)
    #
    # transactions = get_raw_transactions()

    process_transactions()
    i=1
