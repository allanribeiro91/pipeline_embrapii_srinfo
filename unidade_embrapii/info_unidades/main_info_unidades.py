from scripts.tratamento_dados import processar_dados
from scripts.criar_tabela_ue_linhas_atuacao import criar_tabela_ue_linhas_atuacao
import os
import sys

#sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_public_path = os.path.abspath(os.path.join(current_dir, '..', '..', '..', 'etl_srinfo\scripts_public'))
sys.path.append(scripts_public_path)

from scripts_public import baixar_e_juntar_arquivos

def main_info_unidades():
    link = 'https://srinfo.embrapii.org.br/units/list/'
    nome_arquivo = 'info_unidades_embrapii'
    baixar_e_juntar_arquivos(link, current_dir, nome_arquivo)
    processar_dados()
    criar_tabela_ue_linhas_atuacao()


if __name__ == "__main__":
    main_info_unidades()