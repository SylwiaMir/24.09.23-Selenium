#headless mode
from selenium import webdriver
from Selenium3OBIEKTOWKA import LoginPage
import time
from Selenium3OBIEKTOWKA import make_screenshot

options = webdriver.ChromeOptions() #2 potem do opcji przypisujemy opcje webdrivera
options.add_argument('--headless=new') #3 potem dajemy argumenty jakie moze miec webdriver
driver = webdriver.Chrome(options=options) #1 najpierw tworzymy zmienna opcje
"""
--headless: Wykonuje przeglądarkę w trybie "bez głowy", co oznacza, że będzie działać w tle bez wyświetlania interfejsu użytkownika.
--disable-gpu: Wyłącza akcelerację GPU w przeglądarce.
--disable-infobars: Wyłącza informacje na pasku informacji w przeglądarce.
--start-maximized: Uruchamia przeglądarkę w trybie pełnoekranowym.
--incognito: Uruchamia przeglądarkę w trybie incognito (prywatnym).
--disable-extensions: Wyłącza rozszerzenia przeglądarki.
--disable-popup-blocking: Wyłącza blokowanie okienek pop-up.
--disable-notifications: Wyłącza powiadomienia przeglądarki.
--disable-web-security: Wyłącza ochronę przed atakami XSS.
--allow-file-access-from-files: Pozwala na dostęp do plików lokalnych.
--lang: Ustawia preferowany język przeglądarki.
--user-agent: Pozwala na dostosowanie nagłówka User-Agent przeglądarki.
--window-size=width,height: Ustala rozmiar okna przeglądarki.
--proxy-server=ip:port: Ustawia serwer proxy.
--disable-javascript: Wyłącza obsługę JavaScript w przeglądarce.
--disable-images: Wyłącza wczytywanie obrazów.
--remote-debugging-port=port: Ustawia port zdalnego debugowania.
--ignore-certificate-errors: Ignoruje błędy certyfikatów SSL.
--disable-logging: Wyłącza logowanie przeglądarki.
--disable-dev-shm-usage: Wyłącza /dev/shm w systemie (Linux).
--disable-setuid-sandbox: Wyłącza setuid sandbox (Linux).
--no-sandbox: Wyłącza sandbox (Linux).
--disable-software-rasterizer: Wyłącza oprogramowaniowy rasterizer.
"""
driver.maximize_window()
driver.get('https://www.w3schools.com/')

accept_button = driver.find_element('xpath','//*[@id="accept-choices"]')
accept_button.click()
time.sleep(1)
tutorials = driver.find_element('xpath','//*[@id="navbtn_tutorials"]')
HTMLtutorials = driver.find_element('xpath','//*[@id="tutorials_html_css_links_list"]/div[1]/a[2]')
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(tutorials).click().move_to_element(HTMLtutorials).click().perform()
# action chainy stosuje sie np do menu rozwijanych i chainujemy tu kilka akcji do wykonania przez driver
time.sleep(1)
HTMLformattributes = driver.find_element('xpath','//*[@id="leftmenuinnerinner"]/a[40]')
HTMLformattributes.click()

try_it_yourself = driver.find_element('xpath','//*[@id="main"]/div[4]/a')
try_it_yourself.click()

print(driver.title)
time.sleep(2)

currentWindowName = driver.current_window_handle
windowNames = driver.window_handles

print(currentWindowName)
print(windowNames)


#przejscie do drugiej karty

driver.switch_to.window(windowNames[1])

print(driver.current_url)
print(driver.title)

#petla bedzie ok do przypadku gdzie mamy wiecej otwieranych kart
# for okna in windowNames:
#     if okno != currentWindowName:
#         driver.switch_to.window(okno)

