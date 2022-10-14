class CompanyRepository:
    def __init__(self):
        pass

    def put_item(self, company):
        if company.name == 'Microsoft':
            return {
                'ResponseMetadata':
                    {
                        'RequestId': 'N5VLFEGHQCBTQDE8T1NVH2TCANOIUAHSD987123OID',
                        'HTTPStatusCode': 200,
                        'RetryAttempts': 0
                    }
            }
        elif company.name == 'Gamespot':
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
            return {"id": "01ffaccf684640ef95bcc6e2904778a6",
                    "name": "Apple", "abbreviation": "AP", "email": "pd@apple.com"}
        elif id == "02ffcf6846c6e29c785bc047940efaa6":
            return {"id": "02ffcf6846c6e29c785bc047940efaa6",
                    "name": "Google", "abbreviation": "GL", "email": "orders@google.com"}
        elif id == "f68464001fe290ef9547faccbcc678a6":
            return {"id": "f68464001fe290ef9547faccbcc678a6",
                    "name": "Gamespot", "abbreviation": "GP", "email": "buying@gamespot.com"}
        else:
            return None

    def scan(self):
        return [{"id": "01ffaccf684640ef95bcc6e2904778a6",
                 "name": "Apple", "abbreviation": "AP", "email": "pd@apple.com"},
                {"id": "02ffcf6846c6e29c785bc047940efaa6",
                 "name": "Google", "abbreviation": "GL", "email": "orders@google.com"}]

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

    def get_by_abbreviation(self, abbreviation):
        if abbreviation == "DL":
            return {"id": "03f6846cfc72a6f6ec9c940efa04785b",
                    "name": "Dell", "abbreviation": "DL", "email": "buying@dell.com"}
        else:
            return None
