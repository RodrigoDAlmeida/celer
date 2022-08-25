import json
from UserRepository import get

def lambda_handler(event,context):
    #body = json.loads(event.get('body'))
    id = event.get('id')
    item = get(id)

    statusCode = 200
    if(item is None):
        statusCode = 404

    return {
    'statusCode': statusCode, 
    'body': item
    }