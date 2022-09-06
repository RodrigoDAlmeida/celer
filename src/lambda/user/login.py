import json
import jsonpickle
from UserRepository import login


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    user_login = body.get('login')
    user_password = body.get('password')
    user = login(user_login, user_password)

    status_code = 200 if user is None else 401

    return {
        'statusCode': status_code,
        'body': jsonpickle.encode(user, unpicklable=False)
    }
