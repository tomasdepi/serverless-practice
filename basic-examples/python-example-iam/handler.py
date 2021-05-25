import boto3

def hello(event, context):
    client = boto3.client('lambda')
    functions = client.list_functions()
    return functions
