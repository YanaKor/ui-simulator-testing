from selenium.webdriver.common.by import By


class IndexPageLocators:
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-button")
    TITLE_TEXT = (By.CSS_SELECTOR, ".logout-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")

