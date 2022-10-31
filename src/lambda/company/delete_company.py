import responser
from company_service import CompanyService
from company_dynamo_repository import CompanyRepository


def lambda_handler(event, context):
    company_repository = CompanyRepository()
    company_service = CompanyService(company_repository)

    try:
        id = event.get('pathParameters').get('id')
        success = company_service.remove(id)
        status_code = 200 if success else 500
    except Exception as e:
        return responser.build(400, str(e))

    return responser.build(status_code, '')
