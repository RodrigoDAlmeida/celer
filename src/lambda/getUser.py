import jsonpickle
from UserRepository import get


def lambda_handler(event, context):
    id = event.get('pathParameters').get('id')
    item = get(id)
    
    statusCode = 200
    if (item is None):
        statusCode = 404

    return {
    'statusCode': statusCode, 
    'body': jsonpickle.encode(item, unpicklable=False)
    }