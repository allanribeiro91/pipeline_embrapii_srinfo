import os
import sys

#sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_public_path = os.path.abspath(os.path.join(current_dir, '..', '..', '..', 'etl_srinfo\scripts_public'))
sys.path.append(scripts_public_path)

from scripts_public import baixar_e_juntar_arquivos

def main_contratos():
    link = 'https://srinfo.embrapii.org.br/projects/contracts/'
    pasta_download = r'C:\Users\allan.ribeiro\Downloads'
    nome_arquivo = 'contratos'
    baixar_e_juntar_arquivos(link, pasta_download, current_dir, nome_arquivo)


if __name__ == "__main__":
    main_contratos()