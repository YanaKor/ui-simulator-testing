import allure
import pytest
from test_data import data


@allure.description('Successful login')
@allure.label('owner', 'Yana')
@allure.title('Successful login')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_login(index_page):
    index_page.enter_user_name()
    index_page.enter_password()
    index_page.click_login_button()
    index_page.check_title()


@allure.description('Unsuccessful login')
@allure.label('owner', 'Yana')
@allure.title('Unsuccessful login')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('name, password, title_text', (data.case_2, data.case_3, data.case_4),
                         ids=['x', 'y', 'z'])
def test_unsuccessful_login(index_page, name, password, title_text):
    index_page.enter_user_name(name)
    index_page.enter_password(password)
    index_page.click_login_button()
    index_page.check_error_message(title_text)
