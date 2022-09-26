import order_service


def lambda_handler(event, context):
    try:
        order_id = event.get('pathParameters').get('id')
        success = order_service.remove(int(order_id))
        status_code = 200 if success else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': ''
    }
