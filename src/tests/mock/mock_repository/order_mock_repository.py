class OrderRepository:
    def __init__(self):
        pass

    def put_item(self, order):
        if order.description == 'medicines':
            return {
                'ResponseMetadata':
                    {
                        'RequestId': 'N5VLFEGHQCBTQDE8T1NVH2TCANOIUAHSD987123OID',
                        'HTTPStatusCode': 500,
                        'RetryAttempts': 0
                    }
            }
        elif order.user_id == 'accf6846e29001f7f59440e68a7bccf6':
            return {
                'ResponseMetadata':
                    {
                        'RequestId': 'OIASD12983HSAD09AWJSDAWW',
                        'HTTPStatusCode': 500,
                        'RetryAttempts': 11
                    }
            }
        else:
            return {
                'ResponseMetadata':
                    {
                        'RequestId': 'NHJG1293IDS123954AD1230DOIASD12521as',
                        'HTTPStatusCode': 200,
                        'RetryAttempts': 2
                    }
            }

    def get(self, id):
        if id == 1:
            return {"id": 1, "description": "office party", "status": "O",
                    "date": "2022-10-11T11:07:18.934595", "user_id": "01ffaccf684640ef95bcc6e2904778a6"}
        elif id == 2:
            return {"id": 2, "description": "christmas ornaments", "status": "C",
                    "date": "2022-12-24T11:07:18.934595", "user_id": "01ffaccf684640ef95bcc6e2904778a6"}
        elif id == 3:
            return {"id": 3, "description": "end of year party buffet", "status": "R",
                    "date": "2022-12-30T11:07:18.934595", "user_id": "02ffcf6846c6e29c785bc047940efaa6"}
        else:
            return None

    def get_by_user_id(self, user_id):
        if user_id == '01ffaccf684640ef95bcc6e2904778a6':
            return [{"id": 1, "description": "office party", "status": "O",
                     "date": "2022-10-11T11:07:18.934595", "user_id": "01ffaccf684640ef95bcc6e2904778a6"},
                    {"id": 2, "description": "christmas ornaments ", "status": "F",
                     "date": "2022-10-11T11:07:18.934595", "user_id": "01ffaccf684640ef95bcc6e2904778a6"}]
        else:
            return None

    def scan(self):
        return [{"id": 1, "description": "office party", "status": "O",
                 "date": "2022-10-11T11:07:18.934595", "user_id": "01ffaccf684640ef95bcc6e2904778a6"},
                {"id": 2, "description": "christmas ornaments ", "status": "F",
                 "date": "2022-10-11T11:07:18.934595", "user_id": "01ffaccf684640ef95bcc6e2904778a6"},
                {"id": 3, "description": "end of year party buffet", "status": "R",
                 "date": "2022-12-30T11:07:18.934595", "user_id": "02ffcf6846c6e29c785bc047940efaa6"}
                ]

    def delete_item(self, id):
        if id == 1:
            return {
                'ResponseMetadata':
                    {
                        'RequestId': 'NHJG1293IDS123954AD1230DOIASD12521AS',
                        'HTTPStatusCode': 200,
                        'RetryAttempts': 0,
                    }
            }
        else:
            return {
                'ResponseMetadata':
                    {
                        'RequestId': 'OPIISDASDASD12521ASF2AS4FOAS9230123JA',
                        'HTTPStatusCode': 501,
                        'RetryAttempts': 0,
                    }
            }

    def get_biggest_id(self):
        return 3

    def get_next_id(self):
        return 3
