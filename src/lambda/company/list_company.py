import json
from company_service import CompanyService
from company_dynamo_repository import CompanyRepository

def lambda_handler(event, context):
    company_repository = CompanyRepository()
    company_service = CompanyService(company_repository)

    try:
        items = company_service.get_all()
        status_code = 200 if items is not None else 204
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
            'statusCode': status_code,
            'body': json.dumps(items)
        }