from selenium.webdriver.common.by import By
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
        return self.driver.find_element(*self.cart_badge).text
