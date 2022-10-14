from model.Order import Order, Status


class OrderService:
    def __init__(self, order_repository, user_repository):
        self.order_repository = order_repository
        self.user_repository = user_repository

    def create(self, user_id, description):
        self.check_user_id(user_id)
        order_id = self.get_next_order_id()
        new_order = Order(order_id, user_id, description)
        self.order_repository.put_item(new_order)
        return new_order

    def get_by_id(self, order_id):
        order = self.order_repository.get(order_id)
        if not order:
            raise Exception("order {} not found".format(order_id))
        return order

    def get_by_user_id(self, user_id):
        return self.order_repository.get_by_user_id(user_id)

    def get_all(self):
        return self.order_repository.scan()

    def remove(self, order_id):
        self.check_exists(order_id)
        response = self.order_repository.delete_item(order_id)
        return response.get('ResponseMetadata').get('HTTPStatusCode') == 200

    def update(self, user_id, description, status, order_id, date):
        self.check_exists(order_id)
        self.check_user_id(user_id)
        order = Order(order_id, user_id, description, Status(status), date)
        response = self.order_repository.put_item(order)
        return order if response.get('ResponseMetadata').get('HTTPStatusCode') == 200 else response

    def get_all_by_user_id(self, user_id):
        return self.order_repository.get_by_user_id(user_id)

    def check_exists(self, order_id):
        if not self.get_by_id(order_id):
            raise Exception('product model {} not found'.format(order_id))

    def check_user_id(self, user_id):
        user = self.user_repository.get(user_id)
        if not user:
            raise Exception("user {} not found".format(user_id))

    def get_next_order_id(self):
        return self.order_repository.get_next_id()
