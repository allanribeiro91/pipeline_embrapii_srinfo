import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def baixar_dados_srinfo(driver, link_listagem):

    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    # # Configurar o WebDriver usando webdriver-manager
    # edge_service = EdgeService(EdgeChromiumDriverManager().install())
    # options = webdriver.EdgeOptions()
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument('start-maximized')
    # options.add_argument('disable-infobars')
    # options.add_argument('--disable-extensions')

    # driver = webdriver.Edge(service=edge_service, options=options)
    
    try:
        #Acessar tela de login
        driver.get('https://srinfo.embrapii.org.br/users/login/')
        time.sleep(5)
        
        #Inserir credenciais
        username_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'id_username'))
        )
        username_field.send_keys(username)
        
        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'password'))
        )
        password_field.send_keys(password)


        #Logar
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))
        )
        login_button.click()

        #Esperar 3 segundos
        time.sleep(3)

        #Ir para a listagem
        driver.get(link_listagem)
        
        #Selecionar "9999" no dropdown
        time.sleep(5)
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'form-control.input-sm'))
        )
        dropdown.click()
        option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[@value='9999']"))
        )
        option.click()

        carregar_dados_e_fazer_download(driver=driver)
        numero_download = 1

        #Descobrir o número de páginas
        time.sleep(3)
        pagination = driver.find_elements(By.CSS_SELECTOR, 'ul.pagination li')
        num_pages = len(pagination) - 2

        #Se houver mais de uma página, repetir para as páginas seguintes
        if num_pages > 1:

            for page_number in range(2, num_pages + 1):
                #Clicar na página seguinte
                next_page = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"//*[@id='object-list_paginate']/ul/li[{page_number + 1}]/a"))
                )
                next_page.click()

                carregar_dados_e_fazer_download(driver=driver)
                numero_download += 1
    finally:
        # driver.quit()
        pass
    
    return numero_download

def carregar_dados_e_fazer_download(driver):
    #Esperar até 90 segundos para carregar
    time.sleep(2)
    WebDriverWait(driver, 90).until(
        EC.invisibility_of_element_located((By.ID, 'object-list_processing'))
    )
    time.sleep(2)

    #Fazer o download
    excel_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'buttons-excel'))
    )
    excel_button.click()
    time.sleep(3)