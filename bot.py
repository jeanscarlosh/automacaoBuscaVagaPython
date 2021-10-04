from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(r'.\chromedriver.exe')

browser.get("https://www.linkedin.com/login")

input_email = browser.find_element_by_id("username")
input_email.send_keys('***EMAIL***')

inpuy_senha = browser.find_element_by_id("password")
inpuy_senha.send_keys('***SENHA***')

btn_login = browser.find_element_by_xpath("//button[@type='submit']")
btn_login.click()

busca= browser.find_element_by_xpath("//input[@placeholder='Pesquisar']")
busca.send_keys("estagio rh")
busca.send_keys(Keys.RETURN)

time.sleep(3)

filtro_vagas =browser.find_element_by_xpath("//button[@aria-label='Vagas']")
filtro_vagas.click()


input('')
