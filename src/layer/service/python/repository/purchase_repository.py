import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('celer-purchase')


def put_item(purchase):
    response = table.put_item(
        Item={
            'id': purchase.id,
            "product_model_id": purchase.product_model_id,
            "order_id": purchase.order_id,
            "quantity": purchase.quantity,
            "date": purchase.date
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


def get_by_order_id(order_id):
    return table.query(IndexName='order-id-index', KeyConditionExpression=Key('order_id').eq(order_id)).get("Items")

