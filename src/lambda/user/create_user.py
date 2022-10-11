import json
from user_service import UserService
from user_dynamo_repository import UserRepository


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    name = body.get('name')
    login = body.get('login')
    password = body.get('password')

    user_repository = UserRepository()
    user_service = UserService(user_repository)

    try:
        new_user = user_service.create(name, login, password)
        status_code = 201 if new_user is not None else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(new_user.toDict())
    }
