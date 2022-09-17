from repository import product_repository
from repository import company_repository
from model.Product import Product


def create(name, company_abbreviation):
    check_company_abbreviation(company_abbreviation)
    new_product = Product(name, company_abbreviation)
    product_repository.put_item(new_product)
    return new_product


def get_by_id(product_id):
    product = product_repository.get(product_id)
    if not product:
        raise Exception("product {} not found".format(product_id))
    return product


def get_by_company_abbreviation(company_abbreviation):
    return product_repository.get_by_company_abbreviation(company_abbreviation)


def get_all():
    return product_repository.scan()


def remove(product_id):
    check_exists(product_id)
    response = product_repository.delete_item(product_id)
    return response.get('ResponseMetadata').get('HTTPStatusCode') == 200


def update(name, company_abbreviation, product_id):
    check_exists(product_id)
    check_company_abbreviation(company_abbreviation)
    product = Product(name, company_abbreviation, product_id)
    response = product_repository.put_item(product)
    return product if response.get('ResponseMetadata').get('HTTPStatusCode') == 200 else response


def check_exists(product_id):
    if not get_by_id(product_id):
        raise Exception('item {} not found'.format(product_id))


def check_company_abbreviation(company_abbreviation):
    company = company_repository.get_by_abbreviation(company_abbreviation)
    if not company:
        raise Exception("company abbreviation {} not found".format(company_abbreviation))
