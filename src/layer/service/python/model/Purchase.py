import uuid
from datetime import datetime


class Purchase:
    def __init__(self, product_model_id, order_id, quantity, date=None, id=None) -> None:
        self.id = id if id else uuid.uuid4().hex
        self.product_model_id = product_model_id
        self.order_id = order_id
        self.quantity = quantity
        self.date = datetime.now().isoformat() if date is None else date

    def toDict(self):
        return {"id": self.id,
                "product_model_id": self.product_model_id,
                "order_id": self.order_id,
                "quantity": self.quantity,
                "date": self.date}

    @property
    def product_model_id(self):
        return self._product_model_id

    @product_model_id.setter
    def product_model_id(self, d):
        if not d:
            raise Exception("product_model_id cannot be empty")
        self._product_model_id = d

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, d):
        if not d:
            raise Exception("order_id cannot be empty")
        self._order_id = d

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, d):
        if not d > 0:
            raise Exception("quantity must be greater than zero")
        self._quantity = d
