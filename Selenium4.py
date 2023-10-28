from selenium import webdriver
from Selenium3OBIEKTOWKA import LoginPage
from Selenium3OBIEKTOWKA import make_screenshot
import time
import datetime

driver = webdriver.Chrome()
page = LoginPage(driver)
page.open()
page.enter_username('standard_user')
page.enter_password('secret_sauce')
page.click_login()
time.sleep(2)

try:
    assert driver.current_url == 'https://www.saucedemo.com/inventory.htmll',make_screenshot(driver)
    print("Adres jest poprawny")
except AssertionError:
    print("Błąd, adres URL sie nie zgadza")
    raise
finally:
    print("Koniec programu")
    driver.quit()
