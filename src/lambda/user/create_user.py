import json
import user_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    name = body.get('name')
    login = body.get('login')
    password = body.get('password')

    try:
        new_user = user_service.create(name, login, password)
        status_code = 201 if new_user is not None else 500
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(new_user.toDict())
    }
