import boto3
from boto3.dynamodb.conditions import Key
from python.model.User import Company

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('celer-company')


def create(company):
    if get_by_login(company.abbreviation) is not None:
        raise Exception("company "+company.abbreviation+" is already in use")

    response = table.put_item(
        Item={
            'id': company.id,
            'name': company.name,
            'abbreviation': company.abbreviation,
            'email': company.email
        }
    )
    return response


def get(id):
    response = table.get_item(Key={
        'id': id
    })
    return response.get('Item')


def list_all():
    return table.scan().get('Items')


def delete(id):
    response = table.delete_item(
        Key={
            'id': id
        })
    return response


def update(user):
    if get(user.id) is None:
        return None
    return create(user)


def get_by_abbreviation(login):
    return table.query(IndexName='abbreviation-index', KeyConditionExpression=Key('abbreviation').eq(login)).get("Items")[0]