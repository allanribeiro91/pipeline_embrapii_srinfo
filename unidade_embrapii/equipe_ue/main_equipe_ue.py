import os
import sys
from dotenv import load_dotenv

#carregar .env
load_dotenv()
ROOT = os.getenv('ROOT')

#Definição dos caminhos
PATH_ROOT = os.path.abspath(os.path.join(ROOT))
SCRIPTS_PUBLIC_PATH = os.path.abspath(os.path.join(ROOT, 'scripts_public'))
CURRENT_DIR = os.path.abspath(os.path.join(ROOT, 'unidade_embrapii', 'equipe_ue'))
SCRIPTS_PATH = os.path.abspath(os.path.join(CURRENT_DIR, 'scripts'))
DIRETORIO_ARQUIVOS_FINALIZADOS = os.path.abspath(os.path.join(CURRENT_DIR, 'step_3_data_processed'))

#Adicionar caminhos ao sys.path
sys.path.append(PATH_ROOT)
sys.path.append(SCRIPTS_PUBLIC_PATH)
sys.path.append(SCRIPTS_PATH)

#Importar módulos necessários
from scripts_public.scripts_public import baixar_e_juntar_arquivos
from scripts_public.copiar_arquivos_finalizados_para_dwpii import copiar_arquivos_finalizados_para_dwpii
from scripts_public.processar_excel import processar_excel
# from tratamento_dados import processar_dados
from criar_tabela_ue_linhas_atuacao import criar_tabela_ue_linhas_atuacao

def main_equipe_ue(driver):
    link = 'https://srinfo.embrapii.org.br/people/list/'
    nome_arquivo = 'equipe_ue'
    baixar_e_juntar_arquivos(driver, link, CURRENT_DIR, nome_arquivo)
    processar_dados()
    copiar_arquivos_finalizados_para_dwpii(DIRETORIO_ARQUIVOS_FINALIZADOS)


# Definições dos caminhos e nomes de arquivos
origem = os.path.join(ROOT, 'unidade_embrapii', 'equipe_ue', 'step_2_stage_area')
destino = os.path.join(ROOT, 'unidade_embrapii', 'equipe_ue', 'step_3_data_processed')
nome_arquivo = "equipe_ue.xlsx"
arquivo_origem = os.path.join(origem, nome_arquivo)
arquivo_destino = os.path.join(destino, nome_arquivo)

# Campos de interesse e novos nomes das colunas
campos_interesse = [
    "Unidade EMBRAPII",
    "CPF",
    "Nome",
    "Titulação",
    "Formação Acadêmica",
    "Link Lattes",
    "Atividade / Função",
    "Data de entrada",
    "Data de saída",
    "Disponibilidade (horas/mês)",
]

novos_nomes_e_ordem = {
    'CPF': 'cpf',
    'Unidade EMBRAPII': 'unidade_embrapii',
    'Nome': 'nome',
    'Titulação': 'titulacao',
    'Formação Acadêmica': 'formacao_academica',
    'Link Lattes': 'link_lattes',
    'Atividade / Função': 'atividade_funcao',
    'Data de entrada': 'data_entrada',
    'Data de saída': 'data_saida',
    'Disponibilidade (horas/mês)': 'disponibilidade_horas_mes',
}


def processar_dados():
    processar_excel(arquivo_origem, campos_interesse, novos_nomes_e_ordem, arquivo_destino)


if __name__ == "__main__":
    main_equipe_ue()