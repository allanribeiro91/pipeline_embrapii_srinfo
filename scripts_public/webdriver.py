import os
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

# Instalar o driver uma vez
edge_service = EdgeService(EdgeChromiumDriverManager().install())

def configurar_webdriver():
    options = webdriver.EdgeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    driver = webdriver.Edge(service=edge_service, options=options)
    return driver