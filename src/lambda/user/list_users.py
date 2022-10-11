import json
from user_service import UserService
from user_dynamo_repository import UserRepository


def lambda_handler(event, context):
    user_repository = UserRepository()
    user_service = UserService(user_repository)

    try:
        items = user_service.get_all()
        status_code = 200 if items is not None else 204
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
            'statusCode': status_code,
            'body': json.dumps(items)
        }
