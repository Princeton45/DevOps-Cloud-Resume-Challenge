import json
import pytest
from moto import mock_aws
import boto3
from unittest.mock import patch
from lambda_function import lambda_handler, get_dynamodb_table
import warnings

@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    import os
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

@pytest.fixture(scope="function")
def dynamodb(aws_credentials):
    with mock_aws():
        yield boto3.resource('dynamodb', region_name='us-east-1')

@pytest.fixture(scope="function")
def dynamodb_table(dynamodb):
    table = dynamodb.create_table(
        TableName='VisitorCounter',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    yield table

@pytest.fixture(autouse=True)
def setup_dynamodb(dynamodb_table, monkeypatch):
    monkeypatch.setattr('lambda_function.get_dynamodb_table', lambda: dynamodb_table)

def test_lambda_handler_first_visit(dynamodb_table):
    event = {}
    context = {}
    
    response = lambda_handler(event, context)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['count'] == 1

def test_lambda_handler_subsequent_visit(dynamodb_table):
    lambda_handler({}, {})
    response = lambda_handler({}, {})
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['count'] == 2

def test_lambda_handler_error():
    with patch('lambda_function.get_dynamodb_table', side_effect=Exception('Mocked error')):
        response = lambda_handler({}, {})
    
    assert response['statusCode'] == 500
    assert 'error' in json.loads(response['body'])

# We use mock_aws from moto to mock DynamoDB, allowing us to test without accessing real AWS resources.
#test
'''The mock_aws decorator from the moto library creates a mock AWS 
environment for testing purposes. In this case, it's specifically mocking the DynamoDB service.
'''
# This environment mimics AWS services without actually connecting to real AWS resources.

# The dynamodb_table fixture sets up a mock DynamoDB table for each test.

# test_lambda_handler_first_visit checks if the counter starts at 1 for the first visit.

# test_lambda_handler_subsequent_visit verifies that the counter increments correctly.

# test_lambda_handler_error checks error handling by forcing an exception.

# To run the test you can do run "pytest test_lambda_function.py" in the terminal.

'''the lambda_function.py and test_lambda_function.py files are connected. The test file is designed to test the functionality of the lambda_handler function defined in the lambda_function.py file. Here's how they are connected:

In the test file, there's an import statement:

"from lambda_function import lambda_handler"

This imports the lambda_handler function from lambda_function.py, allowing the test file to call and test this function.
'''