import jsonpickle
from UserRepository import delete


def lambda_handler(event, context):
    id = event.get('pathParameters').get('id')
    response = delete(id)

    status_code = 200
    if response is None:
        status_code = 404

    return {
        'statusCode': status_code,
        'body': jsonpickle.encode(response, unpicklable=False)
    }
