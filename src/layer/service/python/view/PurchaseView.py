

class PurchaseView:
    def __init__(self, purchase_id, product_model_id, order_id, quantity, date,
                 product_model_name, product_id, purchase_price, sale_price,
                 product_name, company_abbreviation) -> None:
        self.purchase_id = purchase_id
        self.product_model_id = product_model_id
        self.order_id = order_id
        self.quantity = quantity
        self.date = date
        self.product_model_name = product_model_name
        self.product_id = product_id
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.product_name = product_name
        self.company_abbreviation = company_abbreviation

    def toDict(self):
        return {
            "purchase_id": self.purchase_id,
            "product_model_id": self.product_model_id,
            "order_id": self.order_id,
            "quantity": self.quantity,
            "date": self.date,
            "product_model_name": self.product_model_name,
            "product_id": self.product_id,
            "purchase_price": self.purchase_price,
            "sale_price": self.sale_price,
            "product_name": self.product_name,
            "company_abbreviation": self.company_abbreviation
        }





