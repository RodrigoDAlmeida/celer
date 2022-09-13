from repository import company_repository
from model.Company import Company


def create(name, abbreviation, email):
    new_company = Company(name, abbreviation, email)
    company_repository.put_item(new_company)
    return new_company


def get_by_id(user_id):
    return company_repository.get_by_id(user_id)


def get_by_abbreviation(abbreviation):
    return company_repository.get_by_abbreviation(abbreviation)


def get_all():
    return company_repository.scan()


def remove(company_id):
    if not get_by_id(company_id):
        raise Exception('item {} not found'.format(company_id))
    return company_repository.delete_item(company_id)


def update(name, abbreviation, email, company_id):
    if not company_repository.get(company_id):
        raise Exception('item {} not found'.format(company_id))
    company = Company(name, abbreviation, email, company_id)
    return company_repository.put_item(company)