from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack_add_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bike_add_btn = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.backpack_add_btn).click()
        time.sleep(1)

    def add_bike_light_to_cart(self):
        self.driver.find_element(*self.bike_add_btn).click()
        time.sleep(1)

    def get_cart_count(self):
        # Wait for the cart badge to appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.cart_badge)
        )
        return self.driver.find_element(*self.cart_badge).text
