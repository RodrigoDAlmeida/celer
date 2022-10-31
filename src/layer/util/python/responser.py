def build(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
        },
        'body': body
    }
