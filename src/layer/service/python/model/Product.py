import uuid


class Product:
    def __init__(self, name, purchase_price, sale_price, company_abbreviation, id=uuid.uuid4().hex) -> None:
        self.id = id
        self.name = name
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.company_abbreviation = company_abbreviation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, d):
        if not d:
            raise Exception("name cannot be empty")
        self._name = d

    @property
    def company_abbreviation(self):
        return self._company_abbreviation

    @company_abbreviation.setter
    def company_abbreviation(self, d):
        if not d:
            raise Exception("company_abbreviation cannot be empty")
        self._company_abbreviation = d