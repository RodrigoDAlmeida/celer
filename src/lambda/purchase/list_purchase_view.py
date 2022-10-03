import json
import purchase_service
import encoder


def lambda_handler(event, context):
    order_id = int(event.get('pathParameters').get('order-id'))
    try:
        items = purchase_service.list_purchase_view_by_order_id(order_id)
        status_code = 200 if items is not None else 204
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(items, cls=encoder.DecimalEncoder, ensure_ascii=False).encode('utf8').decode()
    }
