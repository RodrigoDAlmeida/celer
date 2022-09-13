import jsonpickle
import user_service


def lambda_handler(event, context):
    try:
        id = event.get('pathParameters').get('id')
        response = user_service.remove(id)
        status_code = 200 if response.get('ResponseMetadata').get('HTTPStatusCode') == 200 is not None else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': ''
    }
