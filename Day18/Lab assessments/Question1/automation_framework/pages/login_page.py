from selenium.webdriver.common.by import By
from automation_framework.pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    ERROR_MESSAGE = (By.ID, "error")

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
