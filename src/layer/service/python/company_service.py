from model.Company import Company


class CompanyService:
    def __init__(self, company_repository):
        self.company_repository = company_repository

    def create(self, name, abbreviation, email):
        new_company = Company(name, abbreviation, email)
        self.check_abbreviation(new_company)
        self.company_repository.put_item(new_company)
        return new_company

    def get_by_id(self, company_id):
        return self.company_repository.get(company_id)

    def get_by_abbreviation(self, abbreviation):
        return self.company_repository.get_by_abbreviation(abbreviation)

    def get_all(self):
        return self.company_repository.scan()

    def remove(self, company_id):
        self.check_exists(company_id)
        response = self.company_repository.delete_item(company_id)
        return response.get('ResponseMetadata').get('HTTPStatusCode') == 200

    def update(self, name, abbreviation, email, company_id):
        self.check_exists(company_id)
        company = Company(name, abbreviation, email, company_id)
        self.check_abbreviation(company)
        response = self.company_repository.put_item(company)
        return company if response.get('ResponseMetadata').get('HTTPStatusCode') == 200 else response

    def check_exists(self, company_id):
        if not self.get_by_id(company_id):
            raise Exception('item {} not found'.format(company_id))

    def check_abbreviation(self, company):
        company_abbreviation = self.get_by_abbreviation(company.abbreviation)
        if company_abbreviation and company.id != company_abbreviation[0].get('id'):
            raise Exception("abbreviation {} is already in use".format(company.abbreviation))
