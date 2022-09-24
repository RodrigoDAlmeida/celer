import json
import product_model_service
import encoder


def lambda_handler(event, context):
    product_id = event.get('pathParameters').get('product_id')
    try:
        items = product_model_service.get_by_product_id(product_id)
        status_code = 200 if items is not None else 204
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
            'statusCode': status_code,
            'body': json.dumps(items, cls=encoder.DecimalEncoder)
        }