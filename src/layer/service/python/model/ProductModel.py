import uuid


class ProductModel:
    def __init__(self, name, product_id, purchase_price, sale_price, id=uuid.uuid4().hex) -> None:
        self.id = id
        self.name = name
        self.product_id = product_id
        self.purchase_price = purchase_price
        self.sale_price = sale_price

    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, d):
        if d < 0:
            raise Exception("sale price must be greater than zero")
        self._sale_price = d

    @property
    def purchase_price(self):
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, d):
        if d < 0:
            raise Exception("purchase price must be greater than zero")
        self._purchase_price = d
