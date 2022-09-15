from repository import product_repository
from repository import company_repository
from model.Product import Product


def create(name, purchase_price, sale_price, company_abbreviation):
    check_company_abbreviation(company_abbreviation)
    new_product = Product(name, purchase_price, sale_price, company_abbreviation, company_abbreviation)
    product_repository.put_item(new_product)
    return new_product


def get_by_id(product_id):
    return product_repository.get(product_id)


def get_by_company_id(company_id):
    return product_repository.get_by_company_id(company_id)


def get_all():
    return product_repository.scan()


def remove(product_id):
    check_exists(product_id)
    response = product_repository.delete_item(product_id)
    return response.get('ResponseMetadata').get('HTTPStatusCode') == 200


def update(name, login, password, last_login, active, product_id):
    check_exists(product_id)
    product = Product(name, login, password, last_login, active, product_id)

    response = product_repository.put_item(product)
    return product if response.get('ResponseMetadata').get('HTTPStatusCode') == 200 else response


def check_exists(product_id):
    if not get_by_id(product_id):
        raise Exception('item {} not found'.format(product_id))


def check_company_abbreviation(company_abbreviation):
    company = company_repository.get_by_abbreviation(company_abbreviation)
    if company:
        raise Exception("company abbreviation {} not found".format(company_abbreviation))
    return company

