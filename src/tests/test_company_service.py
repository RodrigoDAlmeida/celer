import sys
import pytest

sys.path.append(sys.path[0] + "\\src\\layer\\service\\python")
sys.path.append(sys.path[0] + "\\src\\tests")
from src.layer.service.python.company_service import CompanyService
from mock.mock_repository.company_mock_repository import CompanyRepository


@pytest.fixture()
def company_service():
    return CompanyService(CompanyRepository())


def test_create_company_successfully(company_service):
    new_company = company_service.create('Microsoft', 'MS', 'partners@microsoft.com')
    assert new_company.name == 'Microsoft'
    assert new_company.abbreviation == 'MS'
    assert new_company.email == 'partners@microsoft.com'
    assert len(new_company.id) == 32


def test_create_company_failed(company_service):
    output = company_service.create('Gamespot', 'GP', 'bb@gamespot.com')
    assert output.get('ResponseMetadata').get('HTTPStatusCode') == 500


def test_create_company_fail_abbreviation_already_in_use(company_service):
    with pytest.raises(Exception):
        company_service.create('Dallas', 'DL', 'buy@dallas.com')


def test_get_company_successfully(company_service):
    company = company_service.get_by_id('01ffaccf684640ef95bcc6e2904778a6')
    assert company == {"id": "01ffaccf684640ef95bcc6e2904778a6",
                       "name": "Apple", "abbreviation": "AP", "email": "pd@apple.com"}


def test_get_company_failed(company_service):
    company = company_service.get_by_id('xyznmpbq-132983217')
    assert company is None


def test_list_companys(company_service):
    companys = company_service.get_all()
    assert 2 == len(companys)
    assert companys[0].get('name') == 'Apple'
    assert companys[1].get('name') == 'Google'


def test_get_by_abbreviation_successfully(company_service):
    company = company_service.get_by_abbreviation('DL')
    assert company.get('name') == 'Dell'
    assert company.get('abbreviation') == 'DL'
    assert company.get('email') == 'buying@dell.com'
    assert company.get('id') == "03f6846cfc72a6f6ec9c940efa04785b"


def test_get_by_abbreviation_failed(company_service):
    company = company_service.get_by_abbreviation('CC')
    assert company is None


def test_delete_company_successfully(company_service):
    response = company_service.remove('01ffaccf684640ef95bcc6e2904778a6')
    assert response


def test_delete_company_fail(company_service):
    with pytest.raises(Exception):
        company_service.remove('09isdjocf684640ef95bcc6e2904778a6')


def test_update_company_successfully(company_service):
    company = company_service.update("Apple", 'AL', 'purchases@apple.com', '01ffaccf684640ef95bcc6e2904778a6')
    assert company.name == 'Apple'
    assert company.abbreviation == 'AL'
    assert company.email == 'purchases@apple.com'
    assert company.id == "01ffaccf684640ef95bcc6e2904778a6"


def test_update_company_failed_with_exception(company_service):
    with pytest.raises(Exception):
        company_service.update("Apple", 'AL', 'purchases@apple.com', '999xxccf684640ef95bcc6e2904778a6')


def test_update_company_failed(company_service):
    response = company_service.update("Gamespot", 'GP', 'bb@gamespot.com', 'f68464001fe290ef9547faccbcc678a6')
    assert response.get('ResponseMetadata').get('HTTPStatusCode') == 500
