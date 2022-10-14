import sys
import pytest
from datetime import datetime, timedelta

sys.path.append(sys.path[0] + "\\src\\layer\\service\\python")
sys.path.append(sys.path[0] + "\\src\\tests")
from src.layer.service.python.order_service import OrderService
from src.layer.service.python.model.Order import Status
from mock.mock_repository.order_mock_repository import OrderRepository
from mock.mock_repository.user_mock_repository import UserRepository


@pytest.fixture()
def order_service():
    order_repository = OrderRepository()
    user_repository = UserRepository()
    return OrderService(order_repository, user_repository)


def test_create_order_successfully(order_service):
    date_yesterday = datetime.now() + timedelta(days=-1)
    new_order = order_service.create('01ffaccf684640ef95bcc6e2904778a6', 'office supplies')
    assert new_order.user_id == '01ffaccf684640ef95bcc6e2904778a6'
    assert new_order.description == 'office supplies'
    assert new_order.status.value == Status.OPEN.value
    assert new_order.id == 3
    assert datetime.fromisoformat(new_order.date) > date_yesterday


def test_create_order_failed(order_service):
    output = order_service.create('02ffcf6846c6e29c785bc047940efaa6', 'medicines')
    assert output.get('ResponseMetadata').get('HTTPStatusCode') == 500


def test_create_order_fail_user_not_found(order_service):
    with pytest.raises(Exception):
        order_service.create('faff004cfea6462296846ccc70e85b79', 'friday dinner')


def test_get_order_successfully(order_service):
    order = order_service.get_by_id(1)
    assert order == {"id": 1, "description": "office party", "status": "O",
                     "date": "2022-10-11T11:07:18.934595", "user_id": "01ffaccf684640ef95bcc6e2904778a6"}


def test_get_order_not_found(order_service):
    with pytest.raises(Exception):
        order_service.get_by_id(5)


def test_list_orders(order_service):
    orders = order_service.get_all()
    assert 3 == len(orders)
    assert orders[0].get('id') == 1
    assert orders[1].get('id') == 2
    assert orders[2].get('id') == 3


def test_get_by_user_id_successfully(order_service):
    orders = order_service.get_by_user_id('01ffaccf684640ef95bcc6e2904778a6')
    assert 2 == len(orders)
    assert orders[0].get('status') == 'O'
    assert orders[1].get('status') == 'F'


def test_get_by_abbreviation_not_found(order_service):
    orders = order_service.get_by_user_id('68460ef01ffccf95b04778acac64e296')
    assert orders is None


def test_delete_order_successfully(order_service):
    response = order_service.remove(1)
    assert response


def test_delete_order_fail(order_service):
    with pytest.raises(Exception):
        order_service.remove(8)


def test_update_order_successfully(order_service):
    order = order_service.update("01ffaccf684640ef95bcc6e2904778a6", 'office party', 'F', 1, '2022-10-11T11:18:18.934595')
    assert order.id == 1
    assert order.date == '2022-10-11T11:18:18.934595'
    assert order.status.name == Status.FINISHED.name
    assert order.user_id == "01ffaccf684640ef95bcc6e2904778a6"
    assert order.description == 'office party'


def test_update_order_failed_with_exception(order_service):
    with pytest.raises(Exception):
        order_service.update("01ffaccf684640ef95bcc6e2904778a6", 'office party', 'O', 45, '2022-10-11T11:18:18.934595')


def test_update_order_failed(order_service):
    response = order_service.update("01ffaccf684640ef95bcc6e2904778a6", 'medicines', 'F', 1, '2022-10-11T11:18:18.934595')
    assert response.get('ResponseMetadata').get('HTTPStatusCode') == 500
