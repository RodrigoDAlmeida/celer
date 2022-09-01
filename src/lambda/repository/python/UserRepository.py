import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('celer-user')

def create(new_user):
    response = table.put_item(
       Item={
            'id': new_user.id,
            'name': new_user.name,
            'login': new_user.login,
            'password': new_user.password,
            'lastLogin': new_user.lastLogin,
            'active': new_user.active            
        }
    )
    return response

def get(id):
    response = table.get_item(Key={
        'id': id
    })
    return response.get('Item')

def listAll():
    return table.scan().get('Items')

def login(login, password):
           
    user = table.query( IndexName='login-index', KeyConditionExpression=Key('login').eq(login)).get("Items")[0]

    if not (user is None):
        userPassword = user.get('password')
        if(userPassword == password):
            return user
            
    return None


