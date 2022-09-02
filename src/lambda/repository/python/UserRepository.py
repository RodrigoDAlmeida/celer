from urllib import response
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime
from User import User

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('celer-user')

def create(user):
    response = table.put_item(
       Item={
            'id': user.id,
            'name': user.name,
            'login': user.login,
            'password': user.password,
            'lastLogin': user.lastLogin,
            'active': user.active            
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

def delete(id):
    response = table.delete_item(
        Key={
            'id':id
        })
    return response

def login(login, password):
           
    user = table.query( IndexName='login-index', KeyConditionExpression=Key('login').eq(login)).get("Items")[0]

    if not (user is None):
        userPassword = user.get('password')
        if(userPassword == password):
            u = User(**user)
            create(u)
            return u
            
    return None


