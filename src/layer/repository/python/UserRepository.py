import boto3
from boto3.dynamodb.conditions import Key
from User import User

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('celer-user')


def create(user):
    if(get_by_login(user.login) is not None):
        raise Exception("login "+user.login+" is already in use")
        return None
    
    response = table.put_item(
        Item={
            'id': user.id,
            'name': user.name,
            'login': user.login,
            'password': user.password,
            'lastLogin': user.last_login,
            'active': user.active
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


def get_by_login(login):
    return table.query(IndexName='login-index', KeyConditionExpression=Key('login').eq(login)).get("Items")[0]


def login(username, password):
    user = get_by_login(username)
    if not (user is None):
        user_password = user.get('password')
        if user_password == password:
            u = User(**user)
            create(u)
            return u

    return None
