import jsonpickle
from UserRepository import delete


def lambda_handler(event, context):
    id = event.get('pathParameters').get('id')
    response = delete(id)
    
    statusCode = 200
    if (response is None):
        statusCode = 404

    return {
    'statusCode': statusCode, 
    'body': jsonpickle.encode(response, unpicklable=False)
    }