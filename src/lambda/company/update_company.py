import json
import jsonpickle
import company_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    company_id = body.get('id')
    name = body.get('name')
    abbreviation = body.get('abbreviation')
    email = body.get('email')

    try:
        user = company_service.update(name, abbreviation, email, company_id)
        status_code = 200 if user is not None else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': jsonpickle.encode(user, unpicklable=False)
    }
