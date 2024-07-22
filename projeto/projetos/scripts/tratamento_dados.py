import os
import sys

# sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_public_path = os.path.abspath(os.path.join(current_dir, '..', '..', '..', '..', 'etl_srinfo', 'scripts_public'))
sys.path.append(scripts_public_path)

from processar_excel import processar_excel

# Definições dos caminhos e nomes de arquivos
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
origem = os.path.join(base_dir, 'projeto', 'projetos', 'step_2_stage_area')
destino = os.path.join(base_dir, 'projeto', 'projetos', 'step_3_data_processed')
nome_arquivo = "projetos.xlsx"
arquivo_origem = os.path.join(origem, nome_arquivo)
arquivo_destino = os.path.join(destino, nome_arquivo)

# Campos de interesse e novos nomes das colunas
campos_interesse = [
    "Código Interno",
    "Unidade EMBRAPII",
    "Código EMBRAPII",
    "Tipo de projeto",
    "Status",
    "Título",
    "Título público",
    "Objetivo",
    "Descrição pública",
    "Data da Avaliação",
    "Nota da Avaliação",
    "Observações ou comentários",
    "Tags",
]

novos_nomes_e_ordem = {
    'Código EMBRAPII':'codigo_projeto',
    'Código Interno':'codigo_interno',
    'Unidade EMBRAPII':'unidade_embrapii',
    'Tipo de projeto':'tipo_projeto',
    'Status':'status',
    'Título':'titulo',
    'Título público':'titulo_publico',
    'Objetivo':'objetivo',
    'Descrição pública':'descricao_publica',
    'Data da Avaliação':'data_avaliacao',
    'Nota da Avaliação':'nota_avaliacao',
    'Observações ou comentários':'observacoes',
    'Tags':'tags',
}



def processar_dados():
    processar_excel(arquivo_origem, campos_interesse, novos_nomes_e_ordem, arquivo_destino)

if __name__ == "__main__":
    processar_dados()
