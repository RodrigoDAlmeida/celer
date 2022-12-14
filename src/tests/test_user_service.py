import sys
import pytest
from datetime import datetime, timedelta

sys.path.append(sys.path[0] + "\\src\\layer\\service\\python")
sys.path.append(sys.path[0] + "\\src\\tests")
from src.layer.service.python.user_service import UserService
from mock.mock_repository.user_mock_repository import UserRepository


@pytest.fixture()
def user_service():
    return UserService(UserRepository())


def test_create_user_successfully(user_service):
    date_yesterday = datetime.now() + timedelta(days=-1)
    new_user = user_service.create('Natan', 'ntndrake', '56516asd15')
    assert 'Natan' == new_user.name
    assert 'ntndrake' == new_user.login
    assert '56516asd15' == new_user.password
    assert 32 == len(new_user.id)
    assert new_user.active
    assert datetime.fromisoformat(new_user.last_login) > date_yesterday


def test_create_user_failed(user_service):
    output = user_service.create('Jack', 'jack99', 'asdasf31')
    assert 500 == output.get('ResponseMetadata').get('HTTPStatusCode')


def test_delete_user_fail_login_already_in_use(user_service):
    with pytest.raises(Exception):
        user_service.create('Abigail', 'abby9', 'asdasf31')


def test_get_user_successfully(user_service):
    user = user_service.get_by_id('01ffaccf684640ef95bcc6e2904778a6')
    assert user == {"active": True, "password": "horseee", "login": "joel",
                    "last_login": "2022-10-11T11:07:18.934595", "id": "01ffaccf684640ef95bcc6e2904778a6",
                    "name": "Joel"}


def test_get_user_failed(user_service):
    user = user_service.get_by_id('xyznmpbq-132983217')
    assert user is None


def test_list_users(user_service):
    users = user_service.get_all()
    assert 2 == len(users)
    assert users[0].get('name') == 'Joel'
    assert users[1].get('name') == 'Rodrigo'


def test_get_by_login_successfully(user_service):
    user = user_service.get_by_login('abby9')
    assert user.get('name') == 'Abby'
    assert user.get('login') == 'abby9'
    assert user.get('password') == 'oldcoins'
    assert len(user.get('id')) == 32
    assert not user.get('active')
    assert user.get('last_login') == '2022-07-11T11:07:18.934595'


def test_get_by_login_failed(user_service):
    user = user_service.get_by_login('aloy')
    assert user is None


def test_delete_user_successfully(user_service):
    response = user_service.remove('01ffaccf684640ef95bcc6e2904778a6')
    assert response


def test_delete_user_fail(user_service):
    with pytest.raises(Exception):
        user_service.remove('09isdjocf684640ef95bcc6e2904778a6')


def test_update_user_successfully(user_service):
    user = user_service.update("Sully", 'victorsully', 'treasures', "2021-04-12T11:07:18.934595", True,
                               '01ffaccf684640ef95bcc6e2904778a6')
    assert user.name == 'Sully'
    assert user.login == 'victorsully'
    assert user.password == 'treasures'
    assert len(user.id) == 32
    assert user.active


def test_update_user_failed_with_exception(user_service):
    with pytest.raises(Exception):
        user_service.update("Ryan", 'ryan77', 'bladernr', "2022-01-22T11:07:18.934595", True,
                            '999xxccf684640ef95bcc6e2904778a6')


def test_update_user_failed(user_service):
    response = user_service.update("Elena", 'elena-jornal', 'crashban', "2022-02-01T11:07:18.934595", True,
                                   '02ffcf6846c6e29c785bc047940efaa6')
    assert response.get('ResponseMetadata').get('HTTPStatusCode') == 500


def test_login_successfully(user_service):
    date_yesterday = datetime.now() + timedelta(days=-1)
    user = user_service.do_login("abby9", 'oldcoins')
    assert user.name == 'Abby'
    assert user.login == 'abby9'
    assert user.password == 'oldcoins'
    assert len(user.id) == 32
    assert not user.active
    assert datetime.fromisoformat(user.last_login) > date_yesterday


def test_login_failed_not_found(user_service):
    user = user_service.do_login("sam_drake", 'avery88')
    assert not user
