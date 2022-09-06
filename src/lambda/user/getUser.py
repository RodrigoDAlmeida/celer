import jsonpickle
from UserRepository import get


def lambda_handler(event, context):
    id = event.get('pathParameters').get('id')
    item = get(id)

    status_code = 200 if item is None else 404

    return {
        'statusCode': status_code,
        'body': jsonpickle.encode(item, unpicklable=False)
    }
