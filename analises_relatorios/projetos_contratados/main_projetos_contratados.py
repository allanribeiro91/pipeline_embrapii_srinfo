from scripts.baixar_dados_srinfo import baixar_dados_srinfo_projetos_contratados
import os
import sys
from dotenv import load_dotenv

#sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_public_path = os.path.abspath(os.path.join(current_dir, '..', '..', '..', 'etl_srinfo\scripts_public'))
sys.path.append(scripts_public_path)

from mover_arquivos import mover_arquivos_excel

def main_info_empresas():
    # baixar_dados_srinfo_projetos_contratados()
    pasta_download = os.getenv('PASTA_DOWNLOAD')
    nome_arquivo = 'raw_relatorio_projetos_contratados'
    mover_arquivos_excel(1, pasta_download, current_dir, nome_arquivo)

if __name__ == "__main__":
    main_info_empresas()