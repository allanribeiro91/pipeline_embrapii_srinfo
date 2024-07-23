import os
import sys
from dotenv import load_dotenv

#Adicionar o caminho do diretório raiz ao sys.path
load_dotenv()
ROOT = os.getenv('ROOT')
sys.path.append(ROOT)

#Importar o módulo principal de contratos
from scripts_public.buscar_arquivos_sharepoint import buscar_arquivos_sharepoint
from projeto.contratos.main_contratos import main_contratos
from projeto.projetos.main_projetos import main_projetos
from projeto.classificacao_projeto.main_classificacao_projeto import main_classificacao_projeto
from projeto.projetos_empresas.main_projetos_empresas import main_projetos_empresas
from projeto.estudantes.main_estudantes import main_estudantes
from projeto.pedidos_pi.main_pedidos_pi import main_pedidos_pi
from projeto.macroentregas.main_macroentregas import main_macroentregas

def main_pipeline_srinfo():
    buscar_arquivos_sharepoint()
    main_contratos()
    main_projetos()
    main_classificacao_projeto()
    main_projetos_empresas()
    main_estudantes()
    main_pedidos_pi()
    main_macroentregas()

if __name__ == "__main__":
    main_pipeline_srinfo()
