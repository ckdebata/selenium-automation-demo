from pages.login_page import LoginPage
import time

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    time.sleep(2)
    assert "inventory" in driver.current_url
