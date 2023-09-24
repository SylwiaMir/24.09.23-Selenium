from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(10) #implicity wait lepszy niz sleep
# Explicity wait (lepszy niz implicity, dynamiczy)
# Trzeba pamietac o imporcie selenium.webdriver.support.wait --> WebDriverWait

wait = WebDriverWait (driver,10,0.5) # 10 sec czekania, funkcja sprawdza co 0.5 sec czy element pojawil sie na stronie
# uzywa sie tego poniewaz na stronach w zaleznosci od internetu w roznej predkosci sie laduja sie elementy
# ustawiamy zmienna a potem jej uzywamy w kodzie
driver.get('https://www.w3schools.com/')
driver.set_window_size(1900,1000)
print(driver.title)
accept = driver.find_element('xpath','//*[@id="accept-choices"]')
accept.click()

html_tut = driver.find_element('xpath','//*[@id="subtopnav"]/a[1]')
html_tut.click()


#explicity wait dziala tylko do danego elementu
#wait.until(expected_conditions.visibility_of_element_located(('xpath','//*[@id="leftmenuinnerinner"]/a[39]')))

# wait z wlasnym zdefiniowanym warunkiem(wykorzystujemy lambda i niezerowa dlugosc listy
wait.until(lambda x: len(x.find_elements('xpath','//*[@id="leftmenuinnerinner"]/a[39]')))

html_forms = driver.find_element('xpath','//*[@id="leftmenuinnerinner"]/a[39]')
html_forms.click()

try_it_button = driver.find_element('xpath','//*[@id="main"]/div[3]/a')
try_it_button.click()


# fname = driver.find_element('xpath', '//*[@id="fname"]')
# fname.clear()
# fname.send_keys('Sylwia')
#
# lname = driver.find_element('xpath', '//*[@id="lname"]')
# lname.clear()
# lname.send_keys('Mir...')
#
# submit = driver.find_element('xpath','/html/body/form/input[3]')
# submit.click()

time.sleep(500)

driver.quit()