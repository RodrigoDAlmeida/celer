from repository import order_repository
from repository import user_repository
from model.Order import Order


def create(user_id, description):
    check_user_id(user_id)
    order_id = get_next_order_id()
    new_order = Order(order_id, user_id, description)
    order_repository.put_item(new_order)
    return new_order


def get_by_id(order_id):
    order = order_repository.get(order_id)
    if not order:
        raise Exception("order {} not found".format(order_id))
    return order


def get_by_user_id(user_id):
    return order_repository.get_by_user_id(user_id)


def get_all():
    return order_repository.scan()


def remove(order_id):
    check_exists(order_id)
    response = order_repository.delete_item(order_id)
    return response.get('ResponseMetadata').get('HTTPStatusCode') == 200


def update(user_id, description, status, order_id, date):
    check_exists(order_id)
    check_user_id(user_id)
    order = Order(order_id, user_id,  description, status, date)
    response = order_repository.put_item(order)
    return order if response.get('ResponseMetadata').get('HTTPStatusCode') == 200 else response


def check_exists(order_id):
    if not get_by_id(order_id):
        raise Exception('product model {} not found'.format(order_id))


def check_user_id(user_id):
    user = user_repository.get(user_id)
    if not user:
        raise Exception("user {} not found".format(user_id))


def get_next_order_id():
    return order_repository.get_next_id()

