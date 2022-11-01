import json
import product_model_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    name = body.get('name')
    product_id = body.get('product_id')
    purchase_price = body.get('purchase_price')

    try:
        new_product_model = product_model_service.create(name, product_id, purchase_price)
        status_code = 201 if new_product_model is not None else 500
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(new_product_model.toDict())
    }
