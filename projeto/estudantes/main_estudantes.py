import os
import sys
from dotenv import load_dotenv

#carregar .env
load_dotenv()
ROOT = os.getenv('ROOT')

#Definição dos caminhos
PATH_ROOT = os.path.abspath(os.path.join(ROOT))
SCRIPTS_PUBLIC_PATH = os.path.abspath(os.path.join(ROOT, 'scripts_public'))
CURRENT_DIR = os.path.abspath(os.path.join(ROOT, 'projeto', 'estudantes'))
SCRIPTS_PATH = os.path.abspath(os.path.join(CURRENT_DIR, 'scripts'))

#Adicionar caminhos ao sys.path
sys.path.append(PATH_ROOT)
sys.path.append(SCRIPTS_PUBLIC_PATH)
sys.path.append(SCRIPTS_PATH)

#Importar módulos necessários
from scripts_public.scripts_public import baixar_e_juntar_arquivos
from tratamento_dados import processar_dados

#Definição da função
def main_estudantes():
    link = 'https://srinfo.embrapii.org.br/projects/student/list'
    nome_arquivo = 'estudantes'
    baixar_e_juntar_arquivos(link, CURRENT_DIR, nome_arquivo)
    processar_dados()
    print('main_estudantes finalizado!!')


if __name__ == "__main__":
    main_estudantes()