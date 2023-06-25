from base.base_object import BaseObject
from base.locators import IndexPageLocators as In
from support.assertions import Assertions


class IndexPage(BaseObject, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_user_name(self):
        self.type(In.USERNAME_FIELD, 'correct_username')

    def enter_password(self):
        self.type(In.PASSWORD_FIELD, 'correct_password')

    def click_login_button(self):
        self.click(In.LOGIN_BUTTON)

    def check_title(self):
        self.assert_equal(self.get_text(In.TITLE_TEXT), 'Log out')

    def enter_invalid_user_name(self):
        self.type(In.USERNAME_FIELD, 'invalid_username')

    def check_error_message(self):
        self.assert_equal(self.get_text(In.ERROR_MESSAGE), 'Password or username is incorrect')
