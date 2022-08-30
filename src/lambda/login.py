import json
import jsonpickle
from UserRepository import login

def lambda_handler(event,context):
    body = json.loads(event.get('body'))
    login = body.get('login')
    password = body.get('password')
    user = login(login, password)
    
    statusCode = 200
    if (item is None):
        statusCode = 401

    return {
    'statusCode': statusCode, 
    'body': jsonpickle.encode(user, unpicklable=False)
    }