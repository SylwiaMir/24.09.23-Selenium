import pytest
from selenium import webdriver
from Selenium3OBIEKTOWKA import LoginPage
from Selenium3OBIEKTOWKA import make_screenshot
import time
import datetime

test_data = [
    ('standard_user', 'https://www.saucedemo.com/inventory.html','secret_sauce'),
    ('lock_out_user', 'https://www.saucedemo.com/','secret_sauce'),
    ('problem_user', 'https://www.saucedemo.com/inventory.html','secret_sauce'),
    ('performance_glitch_user', 'https://www.saucedemo.com/inventory.html','secret_sauce'),
    ('error_user', 'https://www.saucedemo.com/inventory.html','secret_sauce'),
    ('visual_user', 'https://www.saucedemo.com/inventory.html','secret_sauce')]
@pytest.mark.parametrize('username, url, password',test_data)
def test_login_page(username,url,password):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    time.sleep(2)

    try:
        assert driver.current_url == url, make_screenshot(driver)

    except AssertionError:
        print("Błąd, adres URL sie nie zgadza")
        raise
    else:
        print('ok')
    finally:
        print("Koniec programu")
        driver.quit()
