import json
import jsonpickle
from UserRepository import login

def lambda_handler(event,context):
    body = json.loads(event.get('body'))
    userLogin = body.get('login')
    userPassword = body.get('password')
    user = login(userLogin, userPassword)
    
    statusCode = 200
    if (user is None):
        statusCode = 401

    return {
    'statusCode': statusCode, 
    'body': jsonpickle.encode(user, unpicklable=False)
    }