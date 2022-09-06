import json
import jsonpickle
from User import User
from UserRepository import create


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    name = body.get('name')
    login = body.get('login')
    password = body.get('password')

    try:
        new_user = User(name, login, password)
        output = create(new_user).get('ResponseMetadata')
        status_code = 201 if output.get('HTTPStatusCode') == 200 else int(output.get('HTTPStatusCode'))
    except Exception as e:
        return{'statusCode': 404, 'body': str(e)}


    return {
        'statusCode': status_code,
        'body': jsonpickle.encode(new_user, unpicklable=False)
    }
