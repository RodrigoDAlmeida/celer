import json
import product_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    product_id = body.get('id')
    name = body.get('name')
    company_abbreviation = body.get('company_abbreviation')

    try:
        product = product_service.update(name, company_abbreviation, product_id)
        status_code = 200 if product is not None else 500
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(product.toDict())
    }
