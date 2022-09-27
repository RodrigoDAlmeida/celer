from repository import product_model_repository
from repository import product_repository
from model.ProductModel import ProductModel


def create(name, product_id, purchase_price, sale_price):
    check_product_id(product_id)
    new_product_model = ProductModel(name, product_id, purchase_price, sale_price)
    product_model_repository.put_item(new_product_model)
    return new_product_model


def get_by_id(product_model_id):
    product_model = product_model_repository.get(product_model_id)
    if not product_model:
        raise Exception("product model {} not found".format(product_model_id))
    return product_model


def get_by_product_id(product_id):
    return product_model_repository.get_by_product_id(product_id)


def remove(product_model_id):
    check_exists(product_model_id)
    response = product_model_repository.delete_item(product_model_id)
    return response.get('ResponseMetadata').get('HTTPStatusCode') == 200


def update(name, product_id, purchase_price, sale_price, product_model_id):
    check_exists(product_model_id)
    check_product_id(product_id)
    product_model = ProductModel(name, product_id,  purchase_price, sale_price, product_model_id)
    response = product_model_repository.put_item(product_model)
    return product_model if response.get('ResponseMetadata').get('HTTPStatusCode') == 200 else response


def check_exists(product_model_id):
    if not get_by_id(product_model_id):
        raise Exception('product model {} not found'.format(product_model_id))


def check_product_id(product_id):
    product = product_repository.get(product_id)
    if not product:
        raise Exception("product {} not found".format(product_id))
