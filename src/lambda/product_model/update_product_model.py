import json
import encoder
import product_model_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    id = body.get('id')
    name = body.get('name')
    product_id = body.get('product_id')
    purchase_price = body.get('purchase_price')
    sale_price = body.get('sale_price')

    try:
        product_model = product_model_service.update(name, product_id, purchase_price, sale_price, id)
        status_code = 200 if product_model is not None else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(product_model.toDict())
    }