import json
import order_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    user_id = body.get('user_id')
    description = body.get('description')

    try:
        new_order = order_service.create(user_id, description)
        status_code = 201 if new_order is not None else 500
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(new_order.toDict())
    }
