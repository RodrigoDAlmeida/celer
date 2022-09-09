from repository import user_repository
from model.User import User


def create(name, login, password):
    new_user = User(name, login, password)
    output = user_repository.create(new_user)
    return new_user


def do_login(username, password):
    user = user_repository.get_by_login(username)
    if not (user is None):
        user_password = user.get('password')
        if user_password == password:
            u = User(**user)
            create(u)
            return u

    return None
