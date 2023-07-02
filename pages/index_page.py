import pytest

from base.base_object import BaseObject
from base.locators import IndexPageLocators as In
from support.assertions import Assertions
import allure


class IndexPage(BaseObject, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Enter user name')
    def enter_user_name(self, name='correct_username'):
        self.type(In.USERNAME_FIELD, name)

    @allure.step('Enter password')
    def enter_password(self, password='correct_password'):
        self.type(In.PASSWORD_FIELD, password)

    @allure.step('Click on login button')
    def click_login_button(self):
        self.click(In.LOGIN_BUTTON)

    @allure.step('Check title display')
    def check_title(self, title_text='Log out'):
        self.assert_equal(self.get_text(In.TITLE_TEXT), title_text)

    # @allure.step('Enter invalid user name')
    # def enter_invalid_user_name(self):
    #     self.type(In.USERNAME_FIELD, 'invalid_username')

    @allure.step('Error message appeared')
    def check_error_message(self, title_text):
        self.assert_equal(self.get_text(In.ERROR_MESSAGE), title_text)
