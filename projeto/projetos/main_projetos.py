import os
import sys

#sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_public_path = os.path.abspath(os.path.join(current_dir, '..', '..', '..', 'etl_srinfo/scripts_public')) # barra pra direita / pra funcionar no pc do lucas
sys.path.append(scripts_public_path)

from baixar_dados_srinfo import baixar_dados_srinfo
from mover_arquivos import mover_arquivos_excel

def main_projetos():
    link = 'https://srinfo.embrapii.org.br/projects/list/'
    numero_arquivos = baixar_dados_srinfo(link)
    print('Número de arquivos: ', numero_arquivos)
    pasta_download = fr'C:\Users\{os.getenv('USERNAME')}\Downloads'
    diretorio = current_dir
    nome_arquivo = 'projetos'
    mover_arquivos_excel(numero_arquivos, pasta_download, diretorio, nome_arquivo)
    print('Finalizado!')


if __name__ == "__main__":
    main_projetos()