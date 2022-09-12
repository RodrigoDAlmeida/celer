from repository import user_repository
from model.User import User


def create(name, login, password):
    new_user = User(name, login, password)
    user_repository.put_item(new_user)
    return new_user


def get_by_id(user_id):
    return user_repository.get(user_id)


def get_by_login(login):
    return user_repository.get_by_login(login)


def get_all():
    return user_repository.scan()


def remove(user_id):
    if not get_by_id(user_id):
        raise Exception('item {} not found'.format(user_id))
    return user_repository.delete_item(user_id)


def update(name, login, password, last_login, active, user_id):
    if not user_repository.get(user_id):
        raise Exception('item {} not found'.format(user_id))
    user = User(name, login, password, last_login, active, user_id)
    return user_repository.put_item(user)


def do_login(username, password):
    user = user_repository.get_by_login(username)
    if not (user is None):
        user_password = user.get('password')
        if user_password == password:
            u = User(**user)
            create(u)
            return u

    return None
