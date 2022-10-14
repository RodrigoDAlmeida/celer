from order_service import OrderService
from order_dynamo_repository import OrderRepository


def lambda_handler(event, context):
    order_repository = OrderRepository()
    order_service = OrderService(order_repository, None)
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
