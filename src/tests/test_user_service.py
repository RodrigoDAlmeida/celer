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
    new_user = user_service.create('Jack', 'jack007', '56516asd15')

    assert 'Jack' == new_user.name
    assert 'jack007' == new_user.login
    assert '56516asd15' == new_user.password
    assert 32 == len(new_user.id)
    assert new_user.active
