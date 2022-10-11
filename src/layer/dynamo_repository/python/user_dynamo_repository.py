import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('celer-user')


class UserRepository:
    def __init__(self):
        pass

    def put_item(self, user):
        response = table.put_item(
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
        response = table.get_item(Key={
            'id': id
        })
        return response.get('Item')

    def scan(self):
        return table.scan().get('Items')

    def delete_item(self, id):
        response = table.delete_item(
            Key={
                'id': id
            })
        return response

    def get_by_login(self, login):
        response = table.query(IndexName='login-index', KeyConditionExpression=Key('login').eq(login)).get("Items")
        return response[0] if response else None
