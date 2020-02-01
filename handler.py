import json
import boto3


def hello(event, context):
    dynamo = boto3.resource("dynamodb")
    table = dynamo.Table("test-table")
    message = table.get_item(Key={"pk": "1"})

    body = message["Item"]

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        # "body": "Blah",
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
    }

    return response
