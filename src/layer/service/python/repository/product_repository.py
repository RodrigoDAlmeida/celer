import boto3
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('celer-product')


def put_item(product):
    response = table.put_item(
        Item={
            'id': product.id,
            'name': product.name,
            'company_abbreviation': product.company_abbreviation
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


def get_by_company_abbreviation(company_abbreviation):
    return table.query(IndexName='company-abbreviation-index', KeyConditionExpression=Key('company_abbreviation').eq(company_abbreviation)).get("Items")



