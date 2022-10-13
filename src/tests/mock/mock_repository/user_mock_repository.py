class UserRepository:
    def __init__(self):
        pass

    def put_item(self, user):
        if user.name == 'Jack':
            return {
                'ResponseMetadata':
                    {
                        'RequestId': 'N5VLFEGHQCBTQDE8T1NVH2TCANOIUAHSD987123OID',
                        'HTTPStatusCode': 500,
                        'RetryAttempts': 0
                    }
            }
        elif user.name == 'Elena':
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
        if id == "01ffaccf684640ef95bcc6e2904778a6":
            return {"active": True, "password": "horseee", "login": "joel",
                    "last_login": "2022-10-11T11:07:18.934595", "id": "01ffaccf684640ef95bcc6e2904778a6",
                    "name": "Joel"}
        elif id == "02ffcf6846c6e29c785bc047940efaa6":
            return {"active": True, "password": "crashban", "login": "elena",
                    "last_login": "2022-10-11T11:07:18.934595", "id": "02ffcf6846c6e29c785bc047940efaa6",
                    "name": "Elena"}
        else:
            return None

    def scan(self):
        return [{"active": True, "password": "horseee", "login": "elliee", "last_login": "2022-10-11T11:07:18.934595",
                 "id": "54ffaccf684640ef95bcc6e2904778a6", "name": "Joel"},
                {"active": True, "password": "555555", "login": "rodrigo", "last_login": "2022-09-30T08:34:07.945081",
                 "id": "bf64924708334d9ca8f27d19e124079d", "name": "Rodrigo"}]

    def delete_item(self, id):
        if id == "01ffaccf684640ef95bcc6e2904778a6":
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

    def get_by_login(self, login):
        if login == "abby9":
            return {"active": False, "password": "oldcoins", "login": "abby9",
                    "last_login": "2022-07-11T11:07:18.934595", "id": "54ffaccf684640ef95bcc6e2904778a6",
                    "name": "Abby"}
        else:
            return None
