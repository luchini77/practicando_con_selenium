from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


url = 'https://josecodetech.es/cursos.php'

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

driver.get(url)

#obtener el titulo
titulo = driver.title
print(titulo)
print('*'*50)
#obtener tarjetas
tarjetas = driver.find_elements(by=By.CLASS_NAME, value='card')
for tarjeta in tarjetas:
    print(tarjeta.text)
print('*'*50)
#obtener enlaces
tarjeta = driver.find_element(by=By.CLASS_NAME, value='card')
#print(tarjeta.text)
enlace = driver.find_element(by=By.XPATH, value='/html/body/div[1]/a')
#print(enlace)
print('Cambiamos de pagina...')
driver.implicitly_wait(0.2)
enlace.click()
driver.implicitly_wait(0.2)
print('Vuelvo a pagina inicial...')
driver.back()

#sleep(3)

