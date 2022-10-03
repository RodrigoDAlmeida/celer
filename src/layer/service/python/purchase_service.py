from repository import purchase_repository
from repository import product_model_repository
from repository import product_repository
from view.PurchaseView import PurchaseView
from model.Purchase import Purchase


def create(purchase_model_id, order_id, quantity):
    new_purchase = Purchase(purchase_model_id, order_id, quantity)
    purchase_repository.put_item(new_purchase)
    return new_purchase


def get_by_id(purchase_id):
    purchase = purchase_repository.get(purchase_id)
    if not purchase:
        raise Exception("purchase {} not found".format(purchase_id))
    return purchase


def get_by_order_id(order_id):
    return purchase_repository.get_by_order_id(order_id)


def remove(purchase_id):
    response = purchase_repository.delete_item(purchase_id)
    return response.get('ResponseMetadata').get('HTTPStatusCode') == 200


def update(purchase_id, product_model_id, order_id, quantity, date):
    purchase = Purchase(product_model_id, order_id, quantity, date, purchase_id)
    response = purchase_repository.put_item(purchase)
    return purchase if response.get('ResponseMetadata').get('HTTPStatusCode') == 200 else response


def list_purchase_view_by_order_id(order_id):
    purchases = get_by_order_id(order_id)
    purchases_view = []

    for purchase in purchases:
        product_model = product_model_repository.get(purchase['product_model_id'])
        product = product_repository.get(product_model['product_id'])
        view = PurchaseView(purchase['id'],
                            purchase['product_model_id'],
                            purchase['order_id'],
                            purchase['quantity'],
                            purchase['date'],
                            product_model['name'],
                            product_model['product_id'],
                            product_model['purchase_price'],
                            product_model['sale_price'],
                            product['name'],
                            product['company_abbreviation'])
        purchases_view.append(view.toDict())

    return purchases_view
