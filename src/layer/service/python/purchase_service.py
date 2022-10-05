from repository import purchase_repository
from repository import product_model_repository
from repository import product_repository
from view.PurchaseView import PurchaseView
from model.Purchase import Purchase
from model.Product import Product
from model.ProductModel import ProductModel


def create(product_model_id, order_id, quantity):
    new_purchase = Purchase(product_model_id, order_id, quantity)
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


def create_purchase_batch(order_id, product_id, product_name, company_abbreviation, purchases):
    included_product = ''
    included_products_models = []
    included_purchases = []

    if not product_id or product_id == '':
        new_product = Product(product_name, company_abbreviation)
        product_repository.put_item(new_product)
        included_product = new_product.toDict()
        product_id = new_product.id

    for purchase in purchases:
        product_model_id = purchase.get('product_model_id')
        if not product_model_id or product_model_id == '':
            new_product_model = ProductModel(purchase['product_model_name'],
                                             product_id,
                                             purchase['purchase_price'],
                                             purchase['sale_price'])
            product_model_repository.put_item(new_product_model)
            included_products_models.append(new_product_model.toDict())
            product_model_id = new_product_model.id

        new_purchase = Purchase(product_model_id, order_id, purchase['quantity'])
        purchase_repository.put_item(new_purchase)
        purchase_view = PurchaseView(new_purchase.id,
                                     new_purchase.product_model_id,
                                     new_purchase.order_id,
                                     new_purchase.quantity,
                                     new_purchase.date,
                                     purchase['product_model_name'],
                                     product_id,
                                     purchase['purchase_price'],
                                     purchase['sale_price'],
                                     product_name,
                                     company_abbreviation)

        included_purchases.append(purchase_view.toDict())

    return {"included_products": included_product,
            "included_product_models": included_products_models,
            "included_purchases:": included_purchases
            }
