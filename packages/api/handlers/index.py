import json
import os

from . import dynamodb


def get(event, context):
    table = dynamodb.resource().Table(os.environ['DYNAMODB_TABLE'])

    # get all records
    records = table.scan()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(records['Items'])
    }

    return response
