from datetime import datetime
from enum import Enum


class Status(Enum):
    OPEN = 'O'
    RUNNING = 'R'
    FINISHED = 'F'


class Order:
    def __init__(self, id, user_id, description, status=Status.OPEN, date=None) -> None:
        self.id = id
        self.user_id = user_id
        self.description = description
        self.date = datetime.now().isoformat() if date is None else date
        self.status = status

    def toDict(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "description": self.description,
                "status": self.status.name,
                "date": self.date}

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, d):
        if not d: raise Exception("user_id cannot be empty")
        self._user_id = d