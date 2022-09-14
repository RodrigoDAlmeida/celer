import jsonpickle
import company_service


def lambda_handler(event, context):
    try:
        items = company_service.get_all()
        status_code = 200 if items is not None else 204
    except Exception as e:
        return{'statusCode': 400, 'body': str(e)}

    return {
            'statusCode': status_code,
            'body': jsonpickle.encode(items, unpicklable=False)
        }