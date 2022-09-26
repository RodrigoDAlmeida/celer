import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('celer-order')


def put_item(order):
    response = table.put_item(
        Item={
            'id': order.id,
            'user_id': order.user_id,
            'description': order.description,
            'status': order.status,
            'date': order.date
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


def get_by_user_id(user_id):
    return table.query(IndexName='product-id-index', KeyConditionExpression=Key('user_id').eq(user_id)).get("Items")


def get_table_count():
    return table.item_count



