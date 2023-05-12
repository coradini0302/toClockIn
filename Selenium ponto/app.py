from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
import schedule
import time
import pytz

def bater_ponto():
    options = Options()
    options.headless = False #executar de forma visivel

    navegador = webdriver.Firefox(options=options)

    link = "https://www.dimepkairos.com.br/Dimep/Account/LogOn?ReturnUrl=%2F"

    navegador.get(url=link)
    sleep(1)

    input_usario = navegador.find_element(by=By.ID,value="LogOnModel_UserName")
    input_usario.send_keys("gabriel.santos@lynxprocess.com")
    sleep(1)

    input_senha = navegador.find_element(by=By.ID,value="LogOnModel_Password")
    input_senha.send_keys("ohG:FY")
    sleep(1)

    button_login = navegador.find_element(by=By.ID,value="btnFormLogin")
    button_login.click()
    sleep(5)

    bater_ponto = navegador.find_element(by=By.XPATH,value='//input[@value="Salvar"]')
    bater_ponto.click()
    sleep(5)



