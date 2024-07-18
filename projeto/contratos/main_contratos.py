import os
import sys

#sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_public_path = os.path.abspath(os.path.join(current_dir, '..', '..', '..', 'ETL_SRInfo\scripts_public'))
sys.path.append(scripts_public_path)

from baixar_dados_srinfo import baixar_dados_srinfo
from mover_arquivos import mover_arquivos_excel

def main_contratos():
    link = 'https://srinfo.embrapii.org.br/projects/contracts/'
    numero_arquivos = baixar_dados_srinfo(link)
    print('Número de arquivos: ', numero_arquivos)
    pasta_download = r'C:\Users\allan.ribeiro\Downloads'
    diretorio = r'C:\Users\allan.ribeiro\OneDrive\Embrapii\ETL_SRInfo\projeto'
    nome_arquivo = 'contratos'
    mover_arquivos_excel(numero_arquivos, pasta_download, diretorio, nome_arquivo)
    print('Finalizado!')


if __name__ == "__main__":
    main_contratos()