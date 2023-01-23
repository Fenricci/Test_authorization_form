from .pages.login_page import LoginPage
import time
from .pages.age_selection_page import AgePage


def test_user_can_see_login_page(browser):
    link = "http://u920152e.beget.tech/#"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_authorization_text()

def test_user_can_login(browser):
    link = "http://u920152e.beget.tech/#"
    email = str(time.time()) + "@fakemail.org"
    password = "12345"
    page = AgePage(browser, link)
    page.open()
    page.user_login(email, password)
    page.choose_radibutton_under_eighteen()

