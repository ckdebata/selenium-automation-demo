from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():
    service = Service(r"C:\Users\91811\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    return driver
