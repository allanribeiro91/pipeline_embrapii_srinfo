import os
import sys
from dotenv import load_dotenv

#carregar .env
load_dotenv()
ROOT = os.getenv('ROOT')

#Definição dos caminhos
PASTA_ARQUIVOS = os.path.abspath(os.path.join(ROOT, 'DWPII_up'))
DWII_COPY = os.path.abspath(os.path.join(ROOT, 'DWPII_copy'))
DWII_BACKUP = os.path.abspath(os.path.join(ROOT, 'DWPII_backup'))
PATH_OFFICE = os.path.abspath(os.path.join(ROOT, 'office365_api'))

# Adiciona o diretório correto ao sys.path
sys.path.append(PATH_OFFICE)

from upload_files import upload_files
from zipar_arquivos import zipar_arquivos

def levar_arquivos_sharepoint():

    # zipar_arquivos(DWII_COPY, DWII_BACKUP)
    upload_files(DWII_BACKUP, "DWPII_backup")
    # upload_files(PASTA_ARQUIVOS, "DWPII")

#Executar função
if __name__ == "__main__":
    levar_arquivos_sharepoint()
