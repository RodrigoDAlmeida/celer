from user_service import UserService
from user_dynamo_repository import UserRepository


def lambda_handler(event, context):
    id = event.get('pathParameters').get('id')
    user_repository = UserRepository()
    user_service = UserService(user_repository)

    try:

        success = user_service.remove(id)
        status_code = 200 if success else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': ''
    }
