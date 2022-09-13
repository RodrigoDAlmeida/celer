import json
import jsonpickle
import company_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    name = body.get('name')
    abbreviation = body.get('abbreviation')
    email = body.get('email')

    try:
        new_company = company_service.create(name, abbreviation, email)
        status_code = 201 if new_company is not None else 500
    except Exception as e:
        return{'statusCode': 404, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': jsonpickle.encode(new_company, unpicklable=False)
    }
