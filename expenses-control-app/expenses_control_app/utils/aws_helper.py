import os
from typing import List

import boto3

from utils.constants import S3_BUCKET


def get_raw_transactions() -> List[str]:

    session = get_aws_session()
    s3_client = session.client('s3')
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=S3_BUCKET,
                               Prefix='raw_transactions/')

    return [
        obj['Key'].split('/')[-1].split('.')[0]
        for page in pages
        for obj in page.get('Contents', {})
        if obj.get('Key', '').endswith('json')
    ]


def get_aws_session():

    return boto3.Session(aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                         aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
                         region_name=os.environ.get("AWS_REGION"))
