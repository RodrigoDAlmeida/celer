import json
import boto3
#function definition
def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    #table name
    table = dynamodb.Table('celer-user')
    #inserting values into table
    response = table.put_item(
       Item={
            'id': '1',
            'name':'Test'
            
        }
    )
    return response