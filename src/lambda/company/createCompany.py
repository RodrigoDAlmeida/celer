import json
import jsonpickle
from Company import User
from CompanyRepository import create


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    name = body.get('name')
    abbreviation = body.get('abbreviation')
    email = body.get('email')
    new_user = User(name, abbreviation, email)
    output = create(new_user)

    return {
        'statusCode': 201,
        'body': jsonpickle.encode(new_user, unpicklable=False)
    }
