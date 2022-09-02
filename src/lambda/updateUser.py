import json
import jsonpickle
from User import User
from UserRepository import update


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    id = body.get('id')
    name = body.get('name')
    login = body.get('login')
    password = body.get('password')
    active = body.get('active')
    last_login = body.get('lastLogin')

    new_user = User(name, login, password, last_login, active, id)
    output = update(new_user)
    status_code = 200
    if output is None:
        status_code = 204

    return {
        'statusCode': status_code,
        'body': jsonpickle.encode(output, unpicklable=False)
    }
