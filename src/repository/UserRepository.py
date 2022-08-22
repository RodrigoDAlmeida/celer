import boto3

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