import json
import sys

sys.path.append('../model')
from model.User import User
#function definition
def lambda_handler(event,context):
    #body = event.get('body')

    name = json.loads(body).get('name'),
    login = json.loads(body).get('login'),
    password = json.loads(body).get('password'),

    new_user = User(1, name, login, password)
    return new_user


    #return {'statusCode': 200, 'body': new_user}