import os
import sys
import gc
import psutil
from dotenv import load_dotenv
from datetime import datetime

# Adicionar o caminho do diretório raiz ao sys.path
load_dotenv()
ROOT = os.getenv('ROOT')
USUARIO = os.getenv('USERNAME')
sys.path.append(ROOT)

# Importar o módulo principal de contratos
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

    # SharePoint
    buscar_arquivos_sharepoint()

    # Configurar o WebDriver
    driver = configurar_webdriver()

    # Empresas
    main_info_empresas(driver)
    log = logear(log, 'info_empresas')

    # Unidades Embrapii
    main_info_unidades(driver)
    log = logear(log, 'info_unidades')

    # Projetos
    main_projetos_contratados(driver)
    log = logear(log, 'projetos_contratados')

    main_projetos_empresas()
    log = logear(log, 'projetos_empresas')

    main_contratos(driver)
    log = logear(log, 'contratos')

    main_projetos(driver)
    log = logear(log, 'projetos')
    
    main_estudantes(driver)
    log = logear(log, 'estudantes')
    
    main_pedidos_pi(driver)
    log = logear(log, 'pedidos_pi')

    main_macroentregas(driver)
    log = logear(log, 'macroentregas')

    encerrar_webdriver(driver)

    main_classificacao_projeto()
    log = logear(log, 'classificacao_projetos')

    main_portfolio()
    log = logear(log, 'portfolio')

    registrar_log(log)

    # SharePoint
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

def logear(log, entidade):
    log.append([datetime.now().strftime('%d/%m/%Y %H:%M:%S'), USUARIO, entidade])
    return log

if __name__ == "__main__":
    main_pipeline_srinfo()
