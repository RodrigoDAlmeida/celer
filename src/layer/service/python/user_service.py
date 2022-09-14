from repository import user_repository
from model.User import User


def create(name, login, password):
    new_user = User(name, login, password)
    check_login(new_user)
    user_repository.put_item(new_user)
    return new_user


def get_by_id(user_id):
    return user_repository.get(user_id)


def get_by_login(login):
    return user_repository.get_by_login(login)


def get_all():
    return user_repository.scan()


def remove(user_id):
    check_exists(user_id)
    response = user_repository.delete_item(user_id)
    return response.get('ResponseMetadata').get('HTTPStatusCode') == 200


def update(name, login, password, last_login, active, user_id):
    check_exists(user_id)
    user = User(name, login, password, last_login, active, user_id)
    check_login(user)
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


def check_exists(user_id):
    if not get_by_id(user_id):
        raise Exception('item {} not found'.format(user_id))


def check_login(user):
    user_login = get_by_login(user.login)
    if user_login and user.id != user_login[0].get('id'):
        raise Exception("login {} is already in use".format(user.login))
