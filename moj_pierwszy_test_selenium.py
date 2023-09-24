from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Inicjalizacje przegladarki Chrome
driver = webdriver.Chrome()

# Otwarcie danej strony w przegladarce
driver.get('https://www.google.pl')

# Jesli nie znajdziesz danego elementu to poczekaj na niego 10s a jak znajdziesz to lec dalej
# Definiujemy raz na caly projekt
driver.implicitly_wait(10)


# Maksymalizacja okna
driver.maximize_window()
# Ustawiamy wymiar okna
driver.set_window_size(1900,1000)


# Poczekaj iles sekund z nawiasu, zeby zobaczyc
# Sleep tylko do celow debugowych, nauczania, testowych
time.sleep(2)

# znalezienie i klikniecie przycisku "Zaakceptuj wszystkie" po xpath
# accept to poprostu nazwa zmiennej czyli przycisk ktory chcemy kliknac
accept = driver.find_element('xpath','//*[@id="L2AGLb"]/div')
accept.click()

time.sleep(3)
# Znajdowanie elementu by name - drugi sposob
# Mozna tez wyszukac po ID i zamist name wpisujemy 'id' i nazwe id
serch_box = driver.find_element('name','q')

# Wprowadzanie hasla do pola wyszukiwania
serch_box.send_keys('Pogoda Łódź')

# Akcja wciskania entera
serch_box.send_keys(Keys.ENTER)  # Aby skorzystac z Keys.ENTER trzeba zaimportowac na gorze kodu "from selenium.webdriver.common.keys import Keys'


time.sleep(3)
#driver.quit() # zamyka wszystkie okna przegladarki
driver.close() # zamknie dane okno przegladarki