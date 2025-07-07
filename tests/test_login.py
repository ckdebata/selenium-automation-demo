import time
from selenium.common.exceptions import NoAlertPresentException
from pages.login_page import LoginPage

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)

    try:
        alert = driver.switch_to.alert
        print("Alert found:", alert.text)
        alert.accept()
    except NoAlertPresentException:
        print("No alert present, continuing...")

    time.sleep(2)
    assert "inventory" in driver.current_url  # ✅ crude assertion, can be improved
