from datetime import datetime
import uuid


class User:
    def __init__(self, name, login, password, last_login=None, active=True, id=None) -> None:
        self.id = id if id else uuid.uuid4().hex
        self.name = name
        self.login = login
        self.password = password
        self.active = active
        self.last_login = datetime.now().isoformat() if last_login is None else last_login

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, d):
        if not d: raise Exception("name cannot be empty")
        self._name = d

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, d):
        if not d: raise Exception("login cannot be empty")
        self._login = d

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, d):
        if not len(d) > 6: raise Exception("password must be at least 6 characters")
        self._password = d
