import json

from User import User
from UserRepository import create

def lambda_handler(event,context):
    
    body = json.loads(event.get('body'))
    name = body.get('name')
    login = body.get('login')
    password = body.get('password')

    new_user = User(name, login, password)

    output = create(new_user)

    return {'statusCode': 200, 'body': output}