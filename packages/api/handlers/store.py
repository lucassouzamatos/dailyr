import json
import os
import uuid

from . import dynamodb


def create(event, context):
    # get the post payload
    data = json.loads(event['body'])
    name, email = data.get('name'), data.get('email')

    # validate
    if not all((name, email)):
        error = 'missing arguments'
        return {
            'statusCode': 400,
            'body': json.dumps(dict(error=error))
        }

    # we can proceed, so load the table
    table = dynamodb.resource().Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': uuid.uuid4().hex,
        'name': name,
        'email': email,
    }

    # store the item
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 201,
        "body": json.dumps(item)
    }

    return response
