from model.User import User
from datetime import datetime


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create(self, name, login, password):
        new_user = User(name, login, password)
        self.check_login(new_user)
        response = self.user_repository.put_item(new_user)
        return new_user if response.get('ResponseMetadata').get('HTTPStatusCode') == 200 else response

    def get_by_id(self, user_id):
        return self.user_repository.get(user_id)

    def get_by_login(self, login):
        return self.user_repository.get_by_login(login)

    def get_all(self):
        return self.user_repository.scan()

    def remove(self, user_id):
        self.check_exists(user_id)
        response = self.user_repository.delete_item(user_id)
        return response.get('ResponseMetadata').get('HTTPStatusCode') == 200

    def update(self, name, login, password, last_login, active, user_id):
        self.check_exists(user_id)
        user = User(name, login, password, last_login, active, user_id)
        self.check_login(user)
        response = self.user_repository.put_item(user)
        return user if response.get('ResponseMetadata').get('HTTPStatusCode') == 200 else response

    def do_login(self, username, password):
        user = self.user_repository.get_by_login(username)
        if not (user is None):
            user_password = user.get('password')
            if user_password == password:
                u = User(**user)
                u.last_login = datetime.now().isoformat()
                self.user_repository.put_item(u)
                return u

        return None

    def check_exists(self, user_id):
        if not self.get_by_id(user_id):
            raise Exception('item {} not found'.format(user_id))

    def check_login(self, user):
        user_login = self.get_by_login(user.login)
        if user_login and user.id != user_login.get('id'):
            raise Exception("login {} is already in use".format(user.login))
