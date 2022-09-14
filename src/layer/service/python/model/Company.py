import uuid


class Company:
    def __init__(self, name, abbreviation, email, id=uuid.uuid4().hex) -> None:
        self.id = id
        self.name = name
        self.abbreviation = abbreviation
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, d):
        if not d:
            raise Exception("name cannot be empty")
        self._name = d

    @property
    def abbreviation(self):
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, d):
        if not d:
            raise Exception("abbreviation cannot be empty")
        self._abbreviation = d