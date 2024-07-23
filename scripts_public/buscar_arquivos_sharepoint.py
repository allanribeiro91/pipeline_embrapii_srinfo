import os
import sys
from dotenv import load_dotenv

#carregar .env
load_dotenv()
ROOT = os.getenv('ROOT')

#Definição dos caminhos
CURRENT_DIR = os.path.abspath(os.path.join(ROOT, 'DWPII_copy'))
PATH_OFFICE = os.path.abspath(os.path.join(ROOT, 'office365_api'))

# Adiciona o diretório correto ao sys.path
sys.path.append(PATH_OFFICE)

from download_files import get_files

def buscar_arquivos_sharepoint():
    get_files("DWPII", CURRENT_DIR)

#Executar função
if __name__ == "__main__":
    buscar_arquivos_sharepoint()
