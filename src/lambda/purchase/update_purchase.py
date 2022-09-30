import json
import purchase_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    id = body.get('id')
    product_model_id = body.get('product_model_id')
    order_id = int(body.get('order_id'))
    quantity = int(body.get('quantity'))
    date = body.get('date')

    try:
        product_model = purchase_service.update(id, product_model_id, order_id, quantity, date)
        status_code = 200 if product_model is not None else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(product_model.toDict())
    }