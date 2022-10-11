class UserRepository:
    def __init__(self):
        pass

    def put_item(self, user):
        if user.name == 'Jack':
            return {
                'ResponseMetadata':
                    {
                        'RequestId': 'N5VLFEGHQCBTQDE8T1NVH2TCANOIUAHSD987123OID',
                        'HTTPStatusCode': 200,
                        'RetryAttempts': 0,
                        'HTTPHeaders': {'server': 'Server',
                                        'date': 'Tue, 11 Oct 2022 11:21:13 GMT',
                                        'content-type': 'application/x-amz-json-1.0',
                                        'content-length': '2',
                                        'connection': 'keep-alive',
                                        'x-amzn-requestid': 'JDSOIOIAS7JDSOI6512SD9SDIOJ',
                                        'x-amz-crc32': '4745646764321'
                                        }

                    }
            }
        else:
            return {
                'ResponseMetadata':
                    {
                        'RequestId': 'NHJG1293IDS123954AD1230DOIASD12521as',
                        'HTTPStatusCode': 500,
                        'RetryAttempts': 2,
                        'HTTPHeaders': {'server': 'Server',
                                        'date': 'Tue, 11 Oct 2022 11:21:13 GMT',
                                        'content-type': 'application/x-amz-json-1.0',
                                        'content-length': '2',
                                        'connection': 'keep-alive',
                                        'x-amzn-requestid': 'DJFOSD01239DOSD2',
                                        'x-amz-crc32': '4745646764321'
                                        }

                    }
            }

    def get(self, id):
        pass

    def scan(self):
        pass

    def delete_item(self, id):
        pass

    def get_by_login(self, login):
        pass
