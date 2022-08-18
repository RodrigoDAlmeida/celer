import json

def lambda_handler(event, context):
    body = event.get('body')
    name = json.loads(body).get('name'),
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Mr. %s!'% name)
    }
