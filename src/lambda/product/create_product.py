import json
import product_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    name = body.get('name')
    company_abbreviation = body.get('company_abbreviation')

    try:
        new_product = product_service.create(name, company_abbreviation)
        status_code = 201 if new_product is not None else 500
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(new_product.toDict())
    }
