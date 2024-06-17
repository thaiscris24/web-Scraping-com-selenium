from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()

navegador.get('http://127.0.0.1/Portf%c3%b3lio%20Animado-Dark/')

sleep(3)

elemento = navegador.find_element_by_tag_name('input')

elemento.send_keys('data')