from .locators import *
from .login_page import LoginPage

class AgePage(LoginPage):
    def choose_radibutton_under_eighteen(self):
        self.browser.find_element(*AgeChooseLocators.UNDER_EIGHTEEN).click()

    def choose_radibutton_from_eighteen_to_twenty_four(self):
        self.browser.find_element(*AgeChooseLocators.FROM_EIGHTEEN_TO_TWENTY_FOUR).click()

    def choose_radibutton_from_twenty_five_to_thirty_five(self):
        self.browser.find_element(*AgeChooseLocators.FROM_TWENTY_FIVE_TO_THIRTY_FIVE).click()

    def choose_radibutton_over_thirty_five(self):
        self.browser.find_element(*AgeChooseLocators.OVER_THIRTY_FIVE).click()