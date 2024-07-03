import pickle

from data_models.data_classes import TransactionBase, TransactionProcessed
from data_models.enums import CategoryLevelThree, CategoryLevelTwo, CategoryLevelOne
from utils.aws_helper import get_raw_transactions, get_aws_session
from utils.constants import PROCESSED_TRANSACTIONS_PREFIX, S3_BUCKET


def process_transactions():

    raw_transactions = get_raw_transactions()
    for raw_transaction in raw_transactions:
        for category in CategoryLevelThree:
            for keyword in category.value.get('keywords'):
                if keyword.lower() in raw_transaction.transaction_description.lower():
                    processed_transaction = build_processed_transaction(
                        raw_transaction=raw_transaction,
                        category_three=category
                    )

                    save_processed_transaction(
                        processed_transaction=processed_transaction
                    )

    return raw_transactions


def build_processed_transaction(
        raw_transaction: TransactionBase,
        category_three: CategoryLevelThree) -> TransactionProcessed:

    category_two = CategoryLevelTwo.get_category_two_from_string(
        category_three.value.get('parent_category')
    )
    category_one = CategoryLevelOne.get_category_one_from_string(
        category_two.value.get('parent_category')
    )

    return TransactionProcessed.from_transaction_base(
        transaction_base=raw_transaction,
        category_level_three=category_three,
        category_level_two=category_two,
        category_level_one=category_one
    )


def save_processed_transaction(processed_transaction: TransactionProcessed) -> None:
    session = get_aws_session()
    s3_client = session.client('s3')
    pickle_file = pickle.dumps(processed_transaction)

    object_name = (PROCESSED_TRANSACTIONS_PREFIX
                   + processed_transaction.transaction_id + '.pkl')

    s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=object_name,
        Body=pickle_file,
    )
