import os
import pickle
from typing import List

import boto3

from data_models.data_classes import TransactionBase
from utils.constants import S3_BUCKET, RAW_TRANSACTIONS_PREFIX


def get_raw_transactions() -> List[TransactionBase]:
    """ Method to get any job list from S3 """

    transaction_to_load = get_raw_transactions_ids()

    session = get_aws_session()
    s3_client = session.client('s3')

    loaded_raw_transactions = []

    for transaction_id in transaction_to_load:
        key = f"{RAW_TRANSACTIONS_PREFIX}{transaction_id}.pkl"
        response = s3_client.get_object(Bucket=S3_BUCKET, Key=key)
        object_content = pickle.load(response['Body'])

        loaded_raw_transactions.append(object_content)

    return loaded_raw_transactions


def get_raw_transactions_ids() -> List[str]:

    session = get_aws_session()
    s3_client = session.client('s3')
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=S3_BUCKET,
                               Prefix=RAW_TRANSACTIONS_PREFIX)

    return [
        obj['Key'].split('/')[-1][:-4]
        for page in pages
        for obj in page.get('Contents', {})
        if obj.get('Key', '').endswith('pkl')
    ]


def get_aws_session():

    return boto3.Session(aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                         aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
                         region_name=os.environ.get("AWS_REGION"))
