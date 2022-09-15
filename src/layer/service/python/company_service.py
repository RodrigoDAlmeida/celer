from repository import company_repository
from model.Company import Company


def create(name, abbreviation, email):
    new_company = Company(name, abbreviation, email)
    check_abbreviation(new_company)
    company_repository.put_item(new_company)
    return new_company


def get_by_id(company_id):
    return company_repository.get(company_id)


def get_by_abbreviation(abbreviation):
    return company_repository.get_by_abbreviation(abbreviation)


def get_all():
    return company_repository.scan()


def remove(company_id):
    check_exists(company_id)
    response = company_repository.delete_item(company_id)
    return response.get('ResponseMetadata').get('HTTPStatusCode') == 200


def update(name, abbreviation, email, company_id):
    check_exists(company_id)
    company = Company(name, abbreviation, email, company_id)
    check_abbreviation(company)
    response = company_repository.put_item(company)
    return company if response.get('ResponseMetadata').get('HTTPStatusCode') == 200 else response


def check_exists(company_id):
    if not get_by_id(company_id):
        raise Exception('item {} not found'.format(company_id))


def check_abbreviation(company):
    company_abbreviation = get_by_abbreviation(company.abbreviation)
    if company_abbreviation and company.id != company_abbreviation[0].get('id'):
        raise Exception("abbreviation {} is already in use".format(company.abbreviation))
