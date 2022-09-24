import uuid


class Product:
    def __init__(self, name, company_abbreviation, id=None) -> None:
        self.id = id if id else uuid.uuid4().hex
        self.name = name
        self.company_abbreviation = company_abbreviation

    def toDict(self):
        return {"id": self.id,
                "name": self.name,
                "company_abbreviation": self.company_abbreviation}

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
