import os
import sys
import gc
import psutil
from dotenv import load_dotenv
from datetime import datetime

#Adicionar o caminho do diretório raiz ao sys.path
load_dotenv()
ROOT = os.getenv('ROOT')
USUARIO = os.getenv('USERNAME')
sys.path.append(ROOT)

#Importar o módulo principal de contratos
from scripts_public.buscar_arquivos_sharepoint import buscar_arquivos_sharepoint
from scripts_public.webdriver import configurar_webdriver
from empresa.info_empresas.main_info_empresas import main_info_empresas
from unidade_embrapii.info_unidades.main_info_unidades import main_info_unidades
from analises_relatorios.projetos_contratados.main_projetos_contratados import main_projetos_contratados
from projeto.contratos.main_contratos import main_contratos
from projeto.projetos.main_projetos import main_projetos
from projeto.projetos_empresas.main_projetos_empresas import main_projetos_empresas
from projeto.estudantes.main_estudantes import main_estudantes
from projeto.pedidos_pi.main_pedidos_pi import main_pedidos_pi
from projeto.macroentregas.main_macroentregas import main_macroentregas
from projeto.classificacao_projeto.main_classificacao_projeto import main_classificacao_projeto
from projeto.portfolio.main_portfolio import main_portfolio
from scripts_public.registrar_log import registrar_log
from scripts_public.levar_arquivos_sharepoint import levar_arquivos_sharepoint

def main_pipeline_srinfo():

    print('Início: ', datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

    log = []

    #sharepoint
    buscar_arquivos_sharepoint()

    #configurar o webdriver
    driver = configurar_webdriver()

    #empresas
    main_info_empresas(driver)
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    log.append([current_datetime, USUARIO, 'info_empresas'])
    driver.delete_all_cookies()
    gc.collect()
    

    #unidades embrapii
    main_info_unidades(driver)
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    log.append([current_datetime, USUARIO, 'info_unidades'])
    driver.delete_all_cookies()
    gc.collect()

    # #projetos
    main_projetos_contratados(driver)
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    log.append([current_datetime, USUARIO, 'projetos_contratados'])
    main_projetos_empresas()
    
    main_contratos(driver)
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    log.append([current_datetime, USUARIO, 'contratos'])
    driver.delete_all_cookies()
    gc.collect()

    main_projetos(driver)
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    log.append([current_datetime, USUARIO, 'projetos'])
    driver.delete_all_cookies()
    gc.collect()
    
    main_estudantes(driver)
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    log.append([current_datetime, USUARIO, 'estudantes'])
    driver.delete_all_cookies()
    gc.collect()
    
    main_pedidos_pi(driver)
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    log.append([current_datetime, USUARIO, 'pedidos_pi'])
    driver.delete_all_cookies()
    gc.collect()

    main_macroentregas(driver)
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    log.append([current_datetime, USUARIO, 'macroentregas'])
    encerrar_webdriver(driver)

    main_classificacao_projeto()
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    log.append([current_datetime, USUARIO, 'classificacao_projetos'])

    main_portfolio()
    current_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    log.append([current_datetime, USUARIO, 'portfolio'])

    registrar_log(log)

    #sharepoint
    levar_arquivos_sharepoint()

    print('Fim: ', datetime.now().strftime('%d/%m/%Y %H:%M:%S'))


def encerrar_webdriver(driver):
    driver.quit()
    for proc in psutil.process_iter():
        try:
            # Verificar se o processo corresponde ao WebDriver (por exemplo, msedgedriver)
            if proc.name().lower() == "msedgedriver":
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    gc.collect()


if __name__ == "__main__":
    main_pipeline_srinfo()
