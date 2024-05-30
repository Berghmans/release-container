import boto3


session = boto3.Session()


def handler(event, context):
    """Lambda handler"""
    return {"statusCode": 200, "body": "Hello World"}
