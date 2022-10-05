import json
import purchase_service


def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    order_id = int(body.get('order_id'))
    product_id = body.get('product_id')
    product_name = body.get('product_name')
    company_abbreviation = body.get('company_abbreviation')
    purchases = body.get('purchases')

    try:
        output = purchase_service.create_purchase_batch(order_id, product_id, product_name,
                                                        company_abbreviation, purchases)
        status_code = 201 if output is not None else 500
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(output, ensure_ascii=False).encode('utf8').decode()
    }
