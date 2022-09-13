import json
import jsonpickle
import user_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    user_login = body.get('login')
    user_password = body.get('password')

    try:
        user = user_service.do_login(user_login, user_password)
        status_code = 200 if user is not None else 500
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': jsonpickle.encode(user, unpicklable=False)
    }
