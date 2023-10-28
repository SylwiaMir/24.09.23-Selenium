from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as excon
from Selenium1 import make_screenshot

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

#login_button = driver.find_element('id','login-button')
#login_button = driver.find_element(By.ID,'login-button')



def czekaj_na_id(element_id):
    timeout = 5 # tez moznaby wpisac bezposrednio do oczekiwatora
    timeout_message = (f'Element o ID {element_id} nie pojawil sie w czasie {timeout}')
    lokalizator = (By.ID, element_id) #tuple, tego mogloby nie byc
    znaleziono = excon.visibility_of_element_located(lokalizator)
    oczekiwator = WebDriverWait(driver,timeout) #poczekaj w tej przegladarce 5 sek, sprawdzamy czy element widoczny
    return oczekiwator.until(znaleziono, timeout_message) # zwrotka

"""
def czekaj_na_id(element_id):
    timeout_message = (f'Element o ID {element_id} nie pojawil sie w czasie 5 sek')
    znaleziono = excon.visibility_of_element_located(By.ID, element_id)
    oczekiwator = WebDriverWait(driver,5) #poczekaj w tej przegladarce 5 sek, sprawdzamy czy element widoczny
    return oczekiwator.until(znaleziono, timeout_message) # zwrotka
"""

try:       #zawsze zrobi try
    login_button = czekaj_na_id('login-button')
except:    # potem except jak blad lub else jak sie uda
    print('Nie znaleziono ID')
    raise  #podnies blad
else:      #to zrobi jezeli sie uda
    print('znaleziono')
finally:   #to zrobi zawsze na koncu
    print('i koniec')
    make_screenshot(driver)
    """today = datetime.datetime.today()
    short_time = today.strftime('__stamp%H%M%S')
    screen_name = 'E:\\Studia WSB - Tester oprogramowania\\23.09 - 24.09 selenium_robot framework\\Selenium\\screeny\\' + 'screen' + short_time + 'Selenium2.png'
    driver.get_screenshot_as_file(screen_name)"""
    driver.quit()