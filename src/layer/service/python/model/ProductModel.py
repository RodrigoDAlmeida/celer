import uuid


class ProductModel:
    def __init__(self, name, product_id, purchase_price, id=None) -> None:
        self.id = id if id else uuid.uuid4().hex
        self.name = name
        self.product_id = product_id
        self.purchase_price = purchase_price

    def toDict(self):
        return {"id": self.id,
                "name": self.name,
                "product_id": self.product_id,
                "purchase_price": self.purchase_price}

    @property
    def purchase_price(self):
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, d):
        if d < 0:
            raise Exception("purchase price must be greater than zero")
        self._purchase_price = d
