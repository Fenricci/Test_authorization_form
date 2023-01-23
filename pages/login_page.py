from .locators import *
from selenium.common.exceptions import NoSuchElementException

class LoginPage():
    def __init__(self, browser, url, timeout=8):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_authorization_text(self):
        assert self.is_element_present(*LoginPageLocators.AUTHORIZATION_TEXT), "Authorization text is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def user_login(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_STRING).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_STRING).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()