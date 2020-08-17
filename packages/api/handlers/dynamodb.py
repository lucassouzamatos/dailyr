from functools import lru_cache
import os

import boto3


# TODO define a maxsize
@lru_cache(None)
def resource():
    """
    Get a new instance of DynamoDB client.
    """

    # may apply to connecting locally
    dynamo_cfg = {
        'region_name': 'localhost',
        'endpoint_url': f"http://localhost:{os.environ['DYNAMODB_DEV_PORT']}",

        # we MUST have creds!
        'aws_access_key_id': 'bar', 
        'aws_secret_access_key': 'foo',
        'aws_session_token': 'baz',
    }

    # get a custom dynamodb resource
    return boto3.resource('dynamodb', **dynamo_cfg)