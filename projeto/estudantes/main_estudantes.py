import os
import sys

#sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_public_path = os.path.abspath(os.path.join(current_dir, '..', '..', '..', 'etl_srinfo\scripts_public'))
sys.path.append(scripts_public_path)

from baixar_dados_srinfo import baixar_dados_srinfo
from mover_arquivos import mover_arquivos_excel

def main_estudantes():
    link = 'https://srinfo.embrapii.org.br/projects/student/list'
    numero_arquivos = baixar_dados_srinfo(link)
    print('Número de arquivos: ', numero_arquivos)
    pasta_download = r'C:\Users\milena.goncalves\Downloads'
    diretorio = current_dir
    nome_arquivo = 'estudantes'
    mover_arquivos_excel(numero_arquivos, pasta_download, diretorio, nome_arquivo)
    print('Finalizado!')


if __name__ == "__main__":
    main_estudantes()