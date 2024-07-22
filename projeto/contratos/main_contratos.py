import os
import sys

#sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))

scripts_public_path = os.path.abspath(os.path.join(current_dir, '..', '..', '..', 'etl_srinfo\scripts_public'))
sys.path.append(scripts_public_path)
from scripts_public import baixar_e_juntar_arquivos

scripts_contratos_path = os.path.abspath(os.path.join(current_dir, 'scripts'))
sys.path.append(scripts_contratos_path)
from tratamento_dados import processar_dados

def main_contratos():
    link = 'https://srinfo.embrapii.org.br/projects/contracts/'
    nome_arquivo = 'contratos'
    baixar_e_juntar_arquivos(link, current_dir, nome_arquivo)
    processar_dados()
    print('main_contratos finalizado!!')


if __name__ == "__main__":
    main_contratos()