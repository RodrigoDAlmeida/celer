import boto3
from boto3.dynamodb.conditions import Key


class OrderRepository:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('celer-order')
        self.table_id_factory = self.dynamodb.Table('celer-id-factory')

    def put_item(self, order):
        response = self.table.put_item(
            Item={
                'id': order.id,
                'user_id': order.user_id,
                'description': order.description,
                'status': order.status.value,
                'date': order.date
            }
        )
        return response

    def get(self, id):
        response = self.table.get_item(Key={
            'id': id
        })
        return response.get('Item')

    def scan(self):
        return self.table.scan().get('Items')

    def delete_item(self, id):
        response = self.table.delete_item(
            Key={
                'id': id
            })
        return response

    def get_by_user_id(self, user_id):
        return self.table.query(IndexName='user-id-index', KeyConditionExpression=Key('user_id').eq(user_id)).get(
            "Items")

    def get_biggest_id(self):
        return max([item[1] for item in self.scan()])

    def get_next_id(self):
        last_id = self.table_id_factory.get_item(Key={
            'table': 'order'
        }).get('Item')

        if not last_id:
            next_id = 1
        else:
            next_id = last_id['id'] + 1

        self.table_id_factory.put_item(Item={'table': 'order', 'id': next_id})
        return int(next_id)
