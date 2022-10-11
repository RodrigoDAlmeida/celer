import json
from user_service import UserService
from user_dynamo_repository import UserRepository


def lambda_handler(event, context):
    id = event.get('pathParameters').get('id')
    user_repository = UserRepository()
    user_service = UserService(user_repository)
    try:
        item = user_service.get_by_id(id)
        status_code = 200 if item is not None else 204
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(item)
    }
