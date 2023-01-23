from selenium.webdriver.common.by import By

class LoginPageLocators():
    EMAIL_STRING = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_STRING = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.form_auth_button")
    AUTHORIZATION_TEXT = (By.CSS_SELECTOR, "p.form_auth_block_head_text")

class AgeChooseLocators():
    UNDER_EIGHTEEN = (By.CSS_SELECTOR, 'input[value="18"]') # Меньше 18
    FROM_EIGHTEEN_TO_TWENTY_FOUR = (By.CSS_SELECTOR, 'input[value="18-24"]') # 18-24
    FROM_TWENTY_FIVE_TO_THIRTY_FIVE = (By.CSS_SELECTOR, 'input[value="25-34"]') # 25-35
    OVER_THIRTY_FIVE = (By.CSS_SELECTOR, 'input[value="35-50"]') # Больше 35