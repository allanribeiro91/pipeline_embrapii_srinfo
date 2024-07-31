import os
import sys
from dotenv import load_dotenv

#carregar .env
load_dotenv()
ROOT = os.getenv('ROOT')

#Definição dos caminhos
SCRIPTS_PUBLIC_PATH = os.path.abspath(os.path.join(ROOT, 'scripts_public'))
CURRENT_DIR = os.path.abspath(os.path.join(ROOT, 'DWPII_copy'))
DWPII_UP = os.path.abspath(os.path.join(ROOT, 'DWPII_up'))
DWPII_BACKUP = os.path.abspath(os.path.join(ROOT, 'DWPII_backup'))
PATH_OFFICE = os.path.abspath(os.path.join(ROOT, 'office365_api'))

# Adiciona o diretório correto ao sys.path
sys.path.append(SCRIPTS_PUBLIC_PATH)
sys.path.append(PATH_OFFICE)

from download_files import get_files
from apagar_arquivos_pasta import apagar_arquivos_pasta

def buscar_arquivos_sharepoint():
    apagar_arquivos_pasta(CURRENT_DIR)
    apagar_arquivos_pasta(DWPII_UP)
    apagar_arquivos_pasta(DWPII_BACKUP)

    get_files("DWPII/srinfo", CURRENT_DIR)


#Executar função
if __name__ == "__main__":
    buscar_arquivos_sharepoint()
