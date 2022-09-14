import jsonpickle
import company_service


def lambda_handler(event, context):
    try:
        id = event.get('pathParameters').get('id')
        success = company_service.remove(id)
        status_code = 200 if success else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': ''
    }
