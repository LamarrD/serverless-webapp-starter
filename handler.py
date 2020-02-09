import json
import boto3  # Boto3 is the aws python sdk (how you interact with aws resources from python)


def hello(event, context):
    # Get item from dynamodb with pk 1
    dynamo = boto3.resource("dynamodb")
    table = dynamo.Table("test-table")
    message = table.get_item(Key={"pk": "1"})

    # Build and return response
    body = message["Item"]
    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
    }
    return response
