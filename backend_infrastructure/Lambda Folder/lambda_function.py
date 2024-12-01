import json
import boto3
from decimal import Decimal

# Helper class to convert Decimal to int/float for JSON serialization

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)

def get_dynamodb_table():
    dynamodb = boto3.resource('dynamodb')
    return dynamodb.Table('VisitorCounter')
lkklkl
def lambda_handler(event, context):
    try:
        table = get_dynamodb_table()
        response = table.update_item(
            Key={'id': 'visitors'},
            UpdateExpression='SET #count = if_not_exists(#count, :start) + :inc',
            ExpressionAttributeNames={'#count': 'count'},
            ExpressionAttributeValues={':inc': 1, ':start': 0},
            ReturnValues="UPDATED_NEW"
        )
        
        count = response['Attributes']['count']
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({'count': count}, cls=DecimalEncoder)
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({'error': str(e)})
        }
    