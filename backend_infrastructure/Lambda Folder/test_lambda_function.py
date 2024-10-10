import json
import pytest
from moto import mock_aws
import boto3
from lambda_function import lambda_handler
import warnings

@pytest.fixture
def dynamodb():
    with mock_aws():
        yield boto3.resource('dynamodb', region_name='us-east-1')

@pytest.fixture
def dynamodb_table(dynamodb):
    table = dynamodb.create_table(
        TableName='VisitorCounter',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    yield table

def test_lambda_handler_first_visit(dynamodb_table):
    event = {}
    context = {}
    
    response = lambda_handler(event, context)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['count'] == 1

def test_lambda_handler_subsequent_visit(dynamodb_table):
    # First visit
    lambda_handler({}, {})
    
    # Second visit
    response = lambda_handler({}, {})
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['count'] == 2

def test_lambda_handler_error(mocker):
    # Mock DynamoDB to raise an exception
    mocker.patch('boto3.resource', side_effect=Exception('Mocked error'))
    
    response = lambda_handler({}, {})
    
    assert response['statusCode'] == 500
    assert 'error' in json.loads(response['body'])

# We use mock_aws from moto to mock DynamoDB, allowing us to test without accessing real AWS resources.

'''The mock_aws decorator from the moto library creates a mock AWS 
environment for testing purposes. In this case, it's specifically mocking the DynamoDB service.
'''
# This environment mimics AWS services without actually connecting to real AWS resources.

# The dynamodb_table fixture sets up a mock DynamoDB table for each test.

# test_lambda_handler_first_visit checks if the counter starts at 1 for the first visit.

# test_lambda_handler_subsequent_visit verifies that the counter increments correctly.

# test_lambda_handler_error checks error handling by forcing an exception.

# To run the test you can do run "pytest test_lambda_function.py" in the terminal.