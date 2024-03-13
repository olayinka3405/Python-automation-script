import time

import pytest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("test", "test"),
    ("test", "text"),
    ("test", "test")
    ])

def test_login(driver,  username, password):
    driver.get("https://trytestingthis.netlify.app/")
    username_field = driver.find_element(By.ID, "uname").send_keys(username)
    password_field = driver.find_element(By.ID, "pwd").send_keys(password)
    #password_field = driver.find_element(By.ID, "pwd").send_keys(Keys.RETURN)
    login_field = driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(6)

    assert "Successful" in driver.page_source


print("Test Completed")

# #def test_valid_login(driver):









