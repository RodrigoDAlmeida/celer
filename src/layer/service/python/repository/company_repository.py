import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('celer-company')


def put_item(company):
    if get_by_abbreviation(company.abbreviation):
        raise Exception("abbreviation "+company.abbreviation+" is already in use")

    response = table.put_item(
        Item={
            'id': company.id,
            'name': company.name,
            'abbreviation': company.abbreviation,
            'email': company.email
        }
    )
    return response


def get_by_id(id):
    response = table.get_item(Key={
        'id': id
    })
    return response.get('Item')


def get_by_abbreviation(abbreviation):
    return table.query(IndexName='abbreviation-index', KeyConditionExpression=Key('abbreviation').eq(abbreviation)).get("Items")


def scan():
    return table.scan().get('Items')


def delete_item(id):
    response = table.delete_item(
        Key={
            'id': id
        })
    return response



