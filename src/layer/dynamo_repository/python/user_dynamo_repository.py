import boto3
from boto3.dynamodb.conditions import Key


class UserRepository:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('celer-user')

    def put_item(self, user):
        response = self.table.put_item(
            Item={
                'id': user.id,
                'name': user.name,
                'login': user.login,
                'password': user.password,
                'last_login': user.last_login,
                'active': user.active
            }
        )
        return response

    def get(self, id):
        response = self.table.get_item(Key={
            'id': id
        })
        return response.get('Item')

    def scan(self):
        return self.table.scan().get('Items')

    def delete_item(self, id):
        response = self.table.delete_item(
            Key={
                'id': id
            })
        return response

    def get_by_login(self, login):
        response = self.table.query(IndexName='login-index', KeyConditionExpression=Key('login').eq(login)).get("Items")
        return response[0] if response else None
