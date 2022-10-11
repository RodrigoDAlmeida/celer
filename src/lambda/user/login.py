import json
from user_service import UserService
from user_dynamo_repository import UserRepository


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    user_login = body.get('login')
    user_password = body.get('password')

    user_repository = UserRepository()
    user_service = UserService(user_repository)

    try:
        user = user_service.do_login(user_login, user_password)
        status_code = 200 if user else 500
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(user.toDict())
    }
