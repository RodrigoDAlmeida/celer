import json
import purchase_service
import encoder


def lambda_handler(event, context):
    order_id = int(event.get('pathParameters').get('id'))
    try:
        items = purchase_service.get_by_order_id(order_id)
        status_code = 200 if items is not None else 204
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(items, cls=encoder.DecimalEncoder)
    }
