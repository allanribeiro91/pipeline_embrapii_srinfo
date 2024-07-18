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

def baixar_projetos():

    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    # Configurar o WebDriver usando webdriver-manager
    edge_service = EdgeService(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')

    driver = webdriver.Edge(service=edge_service, options=options)
    
    try:
        # 1. Fazer login
        driver.get('https://srinfo.embrapii.org.br/users/login/')
        time.sleep(5)
        
        #1.1. Inserir credenciais
        username_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'id_username'))
        )
        username_field.send_keys(username)
        
        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'password'))
        )
        password_field.send_keys(password)


        # 1.2. Logar
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))
        )
        login_button.click()

        #Esperar 3 segundos
        time.sleep(3)

        #2. Ir para o link da lista de pessoas
        driver.get('https://srinfo.embrapii.org.br/projects/list/')
        
        #3. Selecionar "9999" no dropdown
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'form-control.input-sm'))
        )
        dropdown.click()
        option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[@value='9999']"))
        )
        option.click()

        #4. Esperar 90 segundos para carregar
        time.sleep(2)
        print('Esperando carregar dados...')
        WebDriverWait(driver, 90).until(
            EC.invisibility_of_element_located((By.ID, 'object-list_processing'))
        )
        time.sleep(2)

        # 7. Clicar em "buttons-excel"
        excel_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'buttons-excel'))
        )
        excel_button.click()

        # 8. Esperar 3 segundos
        time.sleep(3)

        print("Download de dados concluído!")
        time.sleep(3)
    finally:
        driver.quit()

if __name__ == "__main__":
    baixar_projetos()