import json
from order_service import OrderService
from order_dynamo_repository import OrderRepository
from user_dynamo_repository import UserRepository


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    order_id = body.get('id')
    date = body.get('date')
    description = body.get('description')
    status = body.get('status')
    user_id = body.get('user_id')

    order_repository = OrderRepository()
    user_repository = UserRepository()
    order_service = OrderService(order_repository, user_repository)

    try:
        product_model = order_service.update(user_id, description, status, order_id, date)
        status_code = 200 if product_model is not None else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(product_model.toDict())
    }
