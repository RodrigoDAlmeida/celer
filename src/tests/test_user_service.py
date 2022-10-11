import sys
import pytest
from _pytest import mark

sys.path.append(sys.path[0] + "\\src\\layer\\service\\python")
sys.path.append(sys.path[0] + "\\src\\tests")
from src.layer.service.python.user_service import UserService
from mock.mock_repository.user_mock_repository import UserRepository


@pytest.fixture()
def mock_repository():
    return UserRepository()


def test_create_user_successfully(mock_repository):
    user_service = UserService(mock_repository)
    new_user = user_service.create('Natan', 'ntndrake', '56516asd15')
    assert 'Natan' == new_user.name
    assert 'ntndrake' == new_user.login
    assert '56516asd15' == new_user.password
    assert 32 == len(new_user.id)
    assert new_user.active

def test_create_user_failed(mock_repository):
    user_service = UserService(mock_repository)
    output = user_service.create('Jack', 'jack99', 'asdasf31')
    assert 500 == output.get('ResponseMetadata').get('HTTPStatusCode') == 500


def test_get_user_successfully(mock_repository):
    user_service = UserService(mock_repository)
    user = user_service.get_by_id('01ffaccf684640ef95bcc6e2904778a6')
    assert user == {"active": True, "password": "horseee", "login": "joel",
                    "last_login": "2022-10-11T11:07:18.934595", "id": "01ffaccf684640ef95bcc6e2904778a6",
                    "name": "Joel"}


def test_get_user_failed(mock_repository):
    user_service = UserService(mock_repository)
    user = user_service.get_by_id('xyznmpbq-132983217')
    assert user is None


def test_list_users(mock_repository):
    user_service = UserService(mock_repository)
    users = user_service.get_all()
    assert 2 == len(users)
    assert users[0].get('name') == 'Joel'
    assert users[1].get('name') == 'Rodrigo'


def test_get_by_login_successfully(mock_repository):
    user_service = UserService(mock_repository)
    user = user_service.get_by_login('abby9')
    assert 'Abby' == user.get('name')
    assert 'abby9' == user.get('login')
    assert 'oldcoins' == user.get('password')
    assert 32 == len(user.get('id'))
    assert not user.get('active')


def test_get_by_login_failed(mock_repository):
    user_service = UserService(mock_repository)
    user = user_service.get_by_login('aloy')
    assert user is None


def test_delete_user_successfully(mock_repository):
    user_service = UserService(mock_repository)
    response = user_service.remove('01ffaccf684640ef95bcc6e2904778a6')
    assert response


def test_delete_user_fail(mock_repository):
    user_service = UserService(mock_repository)
    with pytest.raises(Exception):
        user_service.remove('09isdjocf684640ef95bcc6e2904778a6')


def test_update_user_successfully(mock_repository):
    user_service = UserService(mock_repository)
    user = user_service.update("Sully", 'victorsully', 'treasures', "2021-04-12T11:07:18.934595", True, '01ffaccf684640ef95bcc6e2904778a6')
    assert 'Sully' == user.name
    assert 'victorsully' == user.login
    assert 'treasures' == user.password
    assert 32 == len(user.id)
    assert user.active



