import json
import encoder
from order_service import OrderService
from order_dynamo_repository import OrderRepository


def lambda_handler(event, context):
    id = int(event.get('pathParameters').get('id'))

    order_repository = OrderRepository()
    order_service = OrderService(order_repository, None)

    try:
        item = order_service.get_by_id(id)
        status_code = 200 if item is not None else 204
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(item, cls=encoder.DecimalEncoder)
    }

