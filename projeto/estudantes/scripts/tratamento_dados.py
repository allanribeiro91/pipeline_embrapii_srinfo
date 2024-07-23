import os
import sys

# sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_public_path = os.path.abspath(os.path.join(current_dir, '..', '..', '..', '..', 'etl_srinfo', 'scripts_public'))
sys.path.append(scripts_public_path)

from processar_excel import processar_excel

# Definições dos caminhos e nomes de arquivos
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
origem = os.path.join(base_dir, 'projeto', 'estudantes', 'step_2_stage_area')
destino = os.path.join(base_dir, 'projeto', 'estudantes', 'step_3_data_processed')
nome_arquivo = "estudantes.xlsx"
arquivo_origem = os.path.join(origem, nome_arquivo)
arquivo_destino = os.path.join(destino, nome_arquivo)

# Campos de interesse e novos nomes das colunas
campos_interesse = [
    "Código do projeto / Projeto Espelho",
    "Unidade EMBRAPII",
    "CPF",
    "Nome",
    "Titulação",
    "Formação Acadêmica",
    "Nível de formação (Em andamento)",
    "Atividade / Função",
    "Disponibilidade (horas/mês)",
    "Data de início das atividades no projeto",
    "Data de término das atividades no projeto",
    "Possui Bolsa",
    "Observações ou comentários",
]

novos_nomes_e_ordem = {
    "Código do projeto / Projeto Espelho": "codigo_projeto",
    "Unidade EMBRAPII": "unidade_embrapii",
    "CPF": "cpf",
    "Nome": "nome",
    "Titulação": "titulacao",
    "Formação Acadêmica": "formacao",
    "Nível de formação (Em andamento)": "nivel_formacao_cursando",
    "Atividade / Função": "atividade",
    "Disponibilidade (horas/mês)": "disponibilidade",
    "Data de início das atividades no projeto": "data_inicio_atividades",
    "Data de término das atividades no projeto": "data_termino_atividades",
    "Possui Bolsa": "bolsista",
    "Observações ou comentários": "observacoes",
}

# Campos de data e valor
campos_data = ['data_inicio_atividades', 'data_termino_atividades']
campos_valor = []

def processar_dados():
    processar_excel(arquivo_origem, campos_interesse, novos_nomes_e_ordem, arquivo_destino, campos_data, campos_valor)

if __name__ == "__main__":
    processar_dados()
