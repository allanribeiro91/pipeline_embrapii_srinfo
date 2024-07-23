import os
import sys
from dotenv import load_dotenv

#carregar .env
load_dotenv()
ROOT = os.getenv('ROOT')

#Definição dos caminhos
PATH_ROOT = os.path.abspath(os.path.join(ROOT))
SCRIPTS_PUBLIC_PATH = os.path.abspath(os.path.join(ROOT, 'scripts_public'))
CURRENT_DIR = os.path.abspath(os.path.join(ROOT, 'projeto', 'classificacao_projeto'))
SCRIPTS_PATH = os.path.abspath(os.path.join(CURRENT_DIR, 'scripts'))
DIRETORIO_ARQUIVOS_FINALIZADOS = os.path.abspath(os.path.join(CURRENT_DIR, 'step_3_data_processed'))

#Adicionar caminhos ao sys.path
sys.path.append(PATH_ROOT)
sys.path.append(SCRIPTS_PUBLIC_PATH)
sys.path.append(SCRIPTS_PATH)

#Importar módulos necessários
from scripts_public.copiar_e_renomear_arquivos import copiar_e_renomear_arquivos
from scripts_public.copiar_arquivos_finalizados_para_dwpii import copiar_arquivos_finalizados_para_dwpii
from new_classificacao_projeto import new_classificacao_projeto
from atualizacao_classificacao_projeto import atualizacao_classificao_projeto

#definir variáveis de copiar_e_renomear_arquivos
origens = {
        'empresas': os.path.join(ROOT, 'empresa', 'info_empresas', 'step_2_stage_area', 'info_empresas.xlsx'),
        'projetos': os.path.join(ROOT, 'projeto', 'projetos', 'step_2_stage_area', 'projetos.xlsx'),
        'unidades_embrapiis': os.path.join(ROOT, 'unidade_embrapii', 'info_unidades', 'step_2_stage_area', 'info_unidades_embrapii.xlsx'),
        'classificacao_projeto': os.path.join(ROOT, 'DWPII_copy', 'classificacao_projeto.xlsx')
    }

# Define o caminho relativo da pasta de destino
destino = os.path.join(ROOT, 'projeto', 'classificacao_projeto', 'step_1_data_raw')

# Renomeia os arquivos ao copiar
renomeios = {
    'empresas': 'raw_empresas.xlsx',
    'projetos': 'raw_projetos.xlsx',
    'unidades_embrapiis': 'raw_unidades_embrapiis.xlsx',
    'classificacao_projeto': 'atual_classificacao_projeto.xlsx'
}


def main_classificacao_projeto():
    copiar_e_renomear_arquivos(origens, destino, renomeios)
    new_classificacao_projeto()
    atualizacao_classificao_projeto()
    copiar_arquivos_finalizados_para_dwpii(DIRETORIO_ARQUIVOS_FINALIZADOS)

if __name__ == "__main__":
    main_classificacao_projeto()
