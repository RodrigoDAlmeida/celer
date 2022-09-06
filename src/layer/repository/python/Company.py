from datetime import datetime
import uuid


class Company:
    def __init__(self, name, login, password, last_login=None, active=True, id=uuid.uuid4().hex) -> None:
        self.id = id
        self.name = name
        self.login = login
        self.password = password
        self.active = active
        self.last_login = datetime.now().isoformat() if last_login is None else last_login