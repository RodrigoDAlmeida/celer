import boto3
from boto3.dynamodb.conditions import Key


class CompanyRepository:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('celer-company')

    def put_item(self, company):
        response = self.table.put_item(
            Item={
                'id': company.id,
                'name': company.name,
                'abbreviation': company.abbreviation,
                'email': company.email
            }
        )
        return response

    def get(self, id):
        response = self.table.get_item(Key={
            'id': id
        })
        return response.get('Item')

    def get_by_abbreviation(self, abbreviation):
        return self.table.query(IndexName='abbreviation-index',
                                KeyConditionExpression=Key('abbreviation').eq(abbreviation)).get("Items")

    def scan(self):
        return self.table.scan().get('Items')

    def delete_item(self, id):
        response = self.table.delete_item(
            Key={
                'id': id
            })
        return response
