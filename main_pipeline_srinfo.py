import os
import sys
import gc
from dotenv import load_dotenv
from datetime import datetime

#Adicionar o caminho do diretório raiz ao sys.path
load_dotenv()
ROOT = os.getenv('ROOT')
sys.path.append(ROOT)

#Importar o módulo principal de contratos
from scripts_public.buscar_arquivos_sharepoint import buscar_arquivos_sharepoint
from scripts_public.webdriver import configurar_webdriver
from empresa.info_empresas.main_info_empresas import main_info_empresas
from unidade_embrapii.info_unidades.main_info_unidades import main_info_unidades
from projeto.contratos.main_contratos import main_contratos
from projeto.projetos.main_projetos import main_projetos
from projeto.projetos_empresas.main_projetos_empresas import main_projetos_empresas
from projeto.estudantes.main_estudantes import main_estudantes
from projeto.pedidos_pi.main_pedidos_pi import main_pedidos_pi
from projeto.macroentregas.main_macroentregas import main_macroentregas
from projeto.classificacao_projeto.main_classificacao_projeto import main_classificacao_projeto
from projeto.portfolio.main_portfolio import main_portfolio
from scripts_public.levar_arquivos_sharepoint import levar_arquivos_sharepoint

def main_pipeline_srinfo():

    print('Início: ', datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

    #sharepoint
    # buscar_arquivos_sharepoint()

    #configurar o webdriver
    driver = configurar_webdriver()

    #empresas
    # main_info_empresas(driver)
    
    #unidades embrapii
    # main_info_unidades(driver)

    #projetos
    # main_contratos(driver)
    # main_projetos(driver)
    # main_projetos_empresas()
    main_estudantes(driver)
    # main_pedidos_pi(driver)
    # main_macroentregas(driver)
    # main_classificacao_projeto()
    # main_portfolio()

    driver.quit()

    #sharepoint
    # levar_arquivos_sharepoint()

    print('Fim: ', datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    
if __name__ == "__main__":
    main_pipeline_srinfo()
