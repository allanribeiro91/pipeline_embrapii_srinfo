import os
import sys
from dotenv import load_dotenv

#carregar .env
load_dotenv()
ROOT = os.getenv('ROOT')

#Definição dos caminhos
PATH_ROOT = os.path.abspath(os.path.join(ROOT))
SCRIPTS_PUBLIC_PATH = os.path.abspath(os.path.join(ROOT, 'scripts_public'))
CURRENT_DIR = os.path.abspath(os.path.join(ROOT, 'projeto', 'projetos_empresas'))
SCRIPTS_PATH = os.path.abspath(os.path.join(CURRENT_DIR, 'scripts'))

#Adicionar caminhos ao sys.path
sys.path.append(PATH_ROOT)
sys.path.append(SCRIPTS_PUBLIC_PATH)
sys.path.append(SCRIPTS_PATH)

#Importar módulos necessários
from scripts_public.copiar_e_renomear_arquivos import copiar_e_renomear_arquivos
from criar_tabela_projetos_empresas import criar_tabela_projetos_empresas 

#definir variáveis de copiar_e_renomear_arquivos
origens = {
        'projetos_contratados': os.path.join(ROOT, 'analises_relatorios', 'projetos_contratados', 'step_1_data_raw', 'raw_relatorio_projetos_contratados.xlsx'),
    }

# Define o caminho relativo da pasta de destino
destino = os.path.join(CURRENT_DIR, 'step_1_data_raw')

# Renomeia os arquivos ao copiar
renomeios = {
    'projetos_contratados': 'raw_projetos_contratados.xlsx',
}


def main_projetos_empresas():
    copiar_e_renomear_arquivos(origens, destino, renomeios)
    criar_tabela_projetos_empresas()
    print('Tabela projetos_empresas criada com sucesso!')

if __name__ == "__main__":
    main_projetos_empresas()