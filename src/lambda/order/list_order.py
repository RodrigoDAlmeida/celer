import json
import encoder
from order_service import OrderService
from order_dynamo_repository import OrderRepository


def lambda_handler(event, context):
    user_id = event.get('pathParameters').get('user-id')

    order_repository = OrderRepository()
    order_service = OrderService(order_repository, None)

    try:
        items = order_service.get_all_by_user_id(user_id)
        status_code = 200 if items is not None else 204
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(items, cls=encoder.DecimalEncoder)
    }
