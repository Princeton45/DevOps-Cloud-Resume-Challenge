# Import required libraries
import json                  # For handling JSON data
import boto3                 # AWS SDK for Python
from decimal import Decimal  # For handling decimal numbers from DynamoDB

# This class helps convert Decimal numbers (from DynamoDB) to regular numbers (for JSON)
# DynamoDB returns numbers as Decimal type, but JSON can't directly work with Decimals
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # Check if the object is a Decimal
        if isinstance(obj, Decimal):
            # Convert to int if it's a whole number, otherwise convert to float
            return int(obj) if obj % 1 == 0 else float(obj)
        # If not a Decimal, let the parent class handle it
        return super(DecimalEncoder, self).default(obj)

# Function to connect to DynamoDB and get the visitor counter table
def get_dynamodb_table():
    # Create a connection to DynamoDB service
    dynamodb = boto3.resource('dynamodb')
    # Return a reference to our specific table
    return dynamodb.Table('VisitorCounter')

# Main Lambda function that AWS will call
def lambda_handler(event, context):
    try:
        # Get the DynamoDB table
        table = get_dynamodb_table()
        
        # Update the visitor count in DynamoDB:
        # - If count doesn't exist, start at 0 and add 1
        # - If count exists, add 1 to current value
        response = table.update_item(
            Key={'id': 'visitors'},                                    # Identify the record to update
            UpdateExpression='SET #count = if_not_exists(#count, :start) + :inc',  # Update formula
            ExpressionAttributeNames={'#count': 'count'},              # Define #count as column name
            ExpressionAttributeValues={':inc': 1, ':start': 0},        # Define values used in formula
            ReturnValues="UPDATED_NEW"                                 # Return the new value
        )
        
        # Get the new count from the response
        count = response['Attributes']['count']
        
        # Return success response (200)
        # Include CORS headers to allow web browser access
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',          # Allow access from any domain
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            # Convert count to JSON, using our special DecimalEncoder
            'body': json.dumps({'count': count}, cls=DecimalEncoder)
        }
        
    # If anything goes wrong, handle the error
    except Exception as e:
        # Print error for debugging in CloudWatch logs
        print(e)
        # Return error response (500)
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            # Return error message in response
            'body': json.dumps({'error': str(e)})
        }