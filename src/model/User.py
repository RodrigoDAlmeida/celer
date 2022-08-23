from datetime import datetime

class User:
    def __init__(self, id, name, login, password) -> None:
        self.id = id
        self.name = name
        self.login = login
        self.password = password
        self.lastLogin = datetime.now().isoformat()
        self.active = True