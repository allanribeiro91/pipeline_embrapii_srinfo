import os
import sys

# Adiciona o diretório correto ao sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.abspath(os.path.join(current_dir, '..', '..', 'ETL_SRInfo', 'office365_api'))
sys.path.append(path)

from download_files import get_files  # Importa a função necessária

def buscar_arquivos_sharepoint():
    pasta = "DWPII"
    destino = current_dir  # Define o destino dos arquivos como a pasta corrente
    get_files(pasta, destino)  # Usa a função get_files para baixar todos os arquivos da pasta

buscar_arquivos_sharepoint()
