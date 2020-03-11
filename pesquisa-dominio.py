#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def openDriver(url):
    # The version of the chromedriver binary needs to be compatible with the google chrome version.
    driver = webdriver.Chrome('/Users/romarioarruda/Desktop/pesquisa-dominio/chromedriver_80')

    driver.get(url)
    
    return driver


def closeDriver(driver):
    print("#####################")
    print("Finishing...")

    time.sleep(1)
    driver.close()


def readDomain():
    dominios = open('base-dominio.txt', 'r')
    
    return dominios


def run():
    print("Starting automation...\n")

    driver = openDriver('https://registro.br/')

    dominios = readDomain()
    
    lista_salva = open('resultado.txt', 'w')

    for dominio in dominios:
        pesquisa = driver.find_element_by_id('is-avail-field')
        pesquisa.clear()
        
        pesquisa.send_keys(dominio)
        pesquisa.send_keys(Keys.RETURN)
        
        time.sleep(1) #Waiting for page loading

        resultado = driver.find_element_by_css_selector('p.font-3 strong')

        texto = f"Domínio {dominio} {resultado.text}"
        texto = texto.replace('\n', '') + '\n'
        
        print(texto)
        
        lista_salva.write(texto)


    lista_salva.close()

    closeDriver(driver)


if __name__ == "__main__":
    run()
