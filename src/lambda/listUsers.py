import jsonpickle
from UserRepository import listAll


def lambda_handler(event, context):
    items = listAll()

    return {
    'statusCode': 200, 
    'body': jsonpickle.encode(items, unpicklable=False)
    }