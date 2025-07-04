from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

        # 🛡️ Handle browser alert popup (if it exists)
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()  # or alert.accept()
        except NoAlertPresentException:
            pass