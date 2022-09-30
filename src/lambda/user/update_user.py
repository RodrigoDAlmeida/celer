import json
import user_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    user_id = body.get('id')
    name = body.get('name')
    login = body.get('login')
    password = body.get('password')
    active = body.get('active')
    last_login = body.get('lastLogin')

    try:
        user = user_service.update(name, login, password, last_login, active, user_id)
        status_code = 200 if user is not None else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(user.toDict())
    }
