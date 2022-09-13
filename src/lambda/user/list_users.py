import jsonpickle
import user_service


def lambda_handler(event, context):
    try:
        items = user_service.get_all()
        status_code = 200 if items is not None else 500
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
            'statusCode': status_code,
            'body': jsonpickle.encode(items, unpicklable=False)
        }
