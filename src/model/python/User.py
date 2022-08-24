from datetime import datetime
import uuid

class User:
    def __init__(self, name, login, password) -> None:
        self.id = uuid.uuid4().hex
        self.name = name
        self.login = login
        self.password = password
        self.lastLogin = datetime.now().isoformat()
        self.active = True