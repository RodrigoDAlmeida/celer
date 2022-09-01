from datetime import datetime
import uuid

class User:
    def __init__(self, name, login, password, lastLogin=None, active=True, id=uuid.uuid4().hex) -> None:
        self.id = id
        self.name = name
        self.login = login
        self.password = password
        self.lastLogin = datetime.now().isoformat()
        self.active = active