import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    time.sleep(1)
    assert "inventory.html" in driver.current_url

def test_invalid_login(driver):
    login = LoginPage(driver)
    login.login("wrong_user", "wrong_pass")
    time.sleep(1)
    error = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username and password do not match" in error
