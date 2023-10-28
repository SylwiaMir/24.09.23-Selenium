from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as excon

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    try:
        username = driver.find_element('xpath', '//*[@id="user-name"]')
        print('po Xpath')
    except NoSuchElementException:
        username = driver.find_element('id', 'user-name')
        print('po id')

    username.clear()
    username.send_keys("standard_user")

    # password = driver.find_element('xpath', '//*[@id="password"]')
    # password.send_keys('secret_sauce')
    try:
        password = driver.find_element(By.XPATH, '//*[@id="password"]') #szukanie elementow z uzyciem By
    except NoSuchElementException:
        print('Nie znaleziono pola z haslem')
        driver.quit()
        raise # raise podnosi blad mimo obslugi wyjatkow w sensie wyswietla komunikat z bledu

    password.clear()
    password.send_keys('secret_sauce')


    login_button = driver.find_element('xpath','//*[@id="login-button"]')
    if not login_button.get_attribute('disable'):
        login_button.click()
    else:
        print('przycisk nieaktywny')


    def make_screenshot(driver):
        today = datetime.datetime.today()
        short_date = today.strftime('_stamp%H%M%S')
        screen_name = 'E:\\Studia WSB - Tester oprogramowania\\23.09 - 24.09 selenium_robot framework\\Selenium\\screeny\\' + 'screen' + short_date + '.png'
        driver.get_screenshot_as_file(screen_name)

    """today = datetime.datetime.today()
    short_time = today.strftime('__stamp%H%M%S')
    screen_name = 'E:\\Studia WSB - Tester oprogramowania\\23.09 - 24.09 selenium_robot framework\\Selenium\\screeny\\' + 'screen' + short_time + '.png'
    driver.get_screenshot_as_file(screen_name)"""

    time.sleep(2)