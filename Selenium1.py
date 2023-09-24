from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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


today = datetime.datetime.today()
short_time = today.strftime('__stamp%H%M%S')
screen_name = 'screen' + short_time + '.png'
driver.get_screenshot_as_file(screen_name)



time.sleep(5)