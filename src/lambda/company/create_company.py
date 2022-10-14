import json
from company_service import CompanyService
from company_dynamo_repository import CompanyRepository



def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    name = body.get('name')
    abbreviation = body.get('abbreviation')
    email = body.get('email')

    company_repository = CompanyRepository()
    company_service = CompanyService(company_repository)

    try:
        new_company = company_service.create(name, abbreviation, email)
        status_code = 201 if new_company is not None else 500
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(new_company.toDict())
    }
