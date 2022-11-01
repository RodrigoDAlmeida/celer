import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('celer-product-model')


def put_item(product_model):
    response = table.put_item(
        Item={
            'id': product_model.id,
            'name': product_model.name,
            'product_id': product_model.product_id,
            'purchase_price': Decimal(str(product_model.purchase_price))
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


def get_by_product_id(product_id):
    return table.query(IndexName='product-id-index', KeyConditionExpression=Key('product_id').eq(product_id)).get("Items")



