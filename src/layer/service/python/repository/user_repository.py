import boto3
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('celer-user')


def put_item(user):
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


def get(id):
    response = table.get_item(Key={
        'id': id
    })
    return response.get('Item')


def scan():
    return table.scan().get('Items')


def delete_item(id):
    response = table.delete_item(
        Key={
            'id': id
        })
    return response


def get_by_login(login):
    response = table.query(IndexName='login-index', KeyConditionExpression=Key('login').eq(login)).get("Items")
    return response[0] if response else None



