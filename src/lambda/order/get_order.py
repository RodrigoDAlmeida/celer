import json
import order_service
import encoder


def lambda_handler(event, context):
    id = int(event.get('pathParameters').get('id'))
    try:
        item = order_service.get_by_id(id)
        status_code = 200 if item is not None else 204
    except Exception as e:
        return {'statusCode': 400, 'body': str(e)}

    return {
        'statusCode': status_code,
        'body': json.dumps(item, cls=encoder.DecimalEncoder)
    }

