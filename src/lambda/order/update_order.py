import json
import order_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    id = body.get('id')
    date = body.get('date')
    description = body.get('description')
    status = body.get('status')
    user_id = body.get('user_id')

    try:
        product_model = order_service.update(user_id, description, status, id, date)
        status_code = 200 if product_model is not None else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(product_model.toDict())
    }