import json
import purchase_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    purchase_model_id = body.get('purchase_model_id')
    order_id = body.get('order_id')
    quantity = body.get('quantity')

    try:
        new_purchase = purchase_service.create(purchase_model_id, order_id, quantity)
        status_code = 201 if new_purchase is not None else 500
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(new_purchase.toDict())
    }
