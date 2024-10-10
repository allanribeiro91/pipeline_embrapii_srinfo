import os
import sys
from dotenv import load_dotenv

#carregar .env
load_dotenv()
ROOT = os.getenv('ROOT')

#Definição dos caminhos
PATH_ROOT = os.path.abspath(os.path.join(ROOT))
SCRIPTS_PUBLIC_PATH = os.path.abspath(os.path.join(ROOT, 'scripts_public'))
CURRENT_DIR = os.path.abspath(os.path.join(ROOT, 'negociacoes', 'negociacoes'))
SCRIPTS_PATH = os.path.abspath(os.path.join(CURRENT_DIR, 'scripts'))
DIRETORIO_ARQUIVOS_FINALIZADOS = os.path.abspath(os.path.join(CURRENT_DIR, 'step_3_data_processed'))

#Adicionar caminhos ao sys.path
sys.path.append(PATH_ROOT)
sys.path.append(SCRIPTS_PUBLIC_PATH)
sys.path.append(CURRENT_DIR)

#Importar módulos necessários
from scripts_public.webdriver import configurar_webdriver
from scripts_public.scripts_public import baixar_e_juntar_arquivos
from scripts_public.copiar_arquivos_finalizados_para_dwpii import copiar_arquivos_finalizados_para_dwpii
from scripts_public.processar_excel import processar_excel
# from tratamento_dados import processar_dados

#Definição da função
def main_negociacoes(driver, option1000 = True):
    link = 'https://srinfo.embrapii.org.br/units/negotiations/'
    nome_arquivo = 'negociacoes_negociacoes'
    baixar_e_juntar_arquivos(driver, link, CURRENT_DIR, nome_arquivo, option1000=option1000)
    processar_dados()
    copiar_arquivos_finalizados_para_dwpii(DIRETORIO_ARQUIVOS_FINALIZADOS)


# Definições dos caminhos e nomes de arquivos
origem = os.path.join(ROOT, 'negociacoes', 'negociacoes', 'step_2_stage_area')
destino = os.path.join(ROOT, 'negociacoes', 'negociacoes', 'step_3_data_processed')
nome_arquivo = "negociacoes_negociacoes.xlsx"
arquivo_origem = os.path.join(origem, nome_arquivo)
arquivo_destino = os.path.join(destino, nome_arquivo)

# Campos de interesse e novos nomes das colunas
campos_interesse = [
    "Código da Negociação",
    "Unidade EMBRAPII",
    "Empresa(s)",
    "CNPJ",
    "CNAE",
    "Parceria / Programa",
    "Call",
    "Cooperação Internacional",
    "Modalidade de financiamento",
    "Primeira versão da Prop. Técnica",
    "Valor total do plano de trabalho",
    "Possibilidade de contratação",
    "Status",
    "Objetivos da Proposta Técnica",
    "Versão da Proposta Técnica",
    "Versão do plano de trabalho",
    "Projeto decorrente",
    "Observações ou comentários",
]

novos_nomes_e_ordem = {
    "Código da Negociação": 'codigo_negociacao',
    "Unidade EMBRAPII": 'unidade_embrapii',
    "Empresa(s)": 'empresa',
    "CNPJ": 'cnpj',
    "CNAE": 'cnae',
    "Parceria / Programa": 'parceria_programa',
    "Call": 'call',
    "Cooperação Internacional": 'cooperacao_internacional',
    "Modalidade de financiamento": 'modalidade_financiamento',
    "Primeira versão da Prop. Técnica": 'data_prim_ver_prop_tec',
    "Valor total do plano de trabalho": 'valor_total_plano_trabalho',
    "Possibilidade de contratação": 'possibilidade_contratacao',
    "Status": 'status',
    "Objetivos da Proposta Técnica": 'objetivos_prop_tec',
    "Versão da Proposta Técnica": 'ver_prop_tec',
    "Versão do plano de trabalho": 'ver_plano_trabalho',
    "Projeto decorrente": 'codigo_projeto',
    "Observações ou comentários": 'observacoes', 
}

# Campos de data e valor
campos_data = ['data_prim_ver_prop_tec']
campos_valor = ['valor_total_plano_trabalho']

def processar_dados():
    processar_excel(arquivo_origem, campos_interesse, novos_nomes_e_ordem, arquivo_destino, campos_data, campos_valor)
