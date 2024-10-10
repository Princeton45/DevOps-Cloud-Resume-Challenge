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

ALso make sure to upload the .ini file to github. The pipeline will automatically know to ignore errors 

When you set up a CI/CD pipeline (e.g., using GitHub Actions, Jenkins, CircleCI, etc.), it will typically clone your repository and run the tests.
Since pytest.ini is part of your repository, it will be used automatically when pytest runs.