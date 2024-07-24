import os
import pandas as pd
from datetime import datetime

def criar_tabela_portfolio():
    # Caminhos dos arquivos Excel
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    raw_projetos_path = os.path.join(base_dir, 'projeto', 'portfolio', 'step_1_data_raw', 'raw_projetos.xlsx')
    raw_contratos_path = os.path.join(base_dir, 'projeto', 'portfolio', 'step_1_data_raw', 'raw_contratos.xlsx')
    raw_classificacao_projeto_path = os.path.join(base_dir, 'projeto', 'portfolio', 'step_1_data_raw', 'raw_classificacao_projeto.xlsx')
    raw_relatorio_projetos_contratados_path = os.path.join(base_dir, 'analises_relatorios', 'projetos_contratados', 'step_1_data_raw', 'raw_relatorio_projetos_contratados.xlsx')
    destino = os.path.join(base_dir, 'projeto', 'portfolio', 'step_3_data_processed')
    arquivo_destino = os.path.join(destino, 'portfolio.xlsx')

    # Ler os arquivos Excel
    df_projetos = pd.read_excel(raw_projetos_path)
    df_contratos = pd.read_excel(raw_contratos_path)
    df_classificacao_projeto = pd.read_excel(raw_classificacao_projeto_path)
    df_projetos_contratados = pd.read_excel(raw_relatorio_projetos_contratados_path)

    # Selecionar apenas as colunas de interesse
    colunas_contratos = [
        "codigo_projeto",
        "unidade_embrapii",
        "data_contrato",
        "data_inicio",
        "data_termino",
        "parceria_programa",
        "call",
        "cooperacao_internacional",
        "modalidade_financiamento",
        "uso_recurso_obrigatorio",
        "projeto",
        "trl_inicial",
        "trl_final",
        "valor_embrapii",
        "valor_empresa",
        "valor_unidade_embrapii",
    ]
    df_contratos_selecionado = df_contratos[colunas_contratos]

    colunas_projetos = [
        "codigo_projeto",
        "status",
        "tipo_projeto",
        "titulo",
        "titulo_publico",
        "objetivo",
        "descricao_publica",
        "data_avaliacao",
        "nota_avaliacao",
        "observacoes",
        "tags",
    ]
    df_projetos_selecionado = df_projetos[colunas_projetos]

    colunas_classificacao_projeto = [
        "codigo_projeto",
        "tecnologia_habilitadora",
        "area_aplicacao",
    ]
    df_classificacao_projeto_selecionado = df_classificacao_projeto[colunas_classificacao_projeto]

    colunas_projetos_contratados = [
        "Código",
        "Status",
    ]
    df_projetos_contratados_selecionados = df_projetos_contratados[colunas_projetos_contratados].rename(columns={'Código': 'codigo_projeto'})


    # Mesclar os dados com base na chave "codigo_projeto"
    df_portfolio = df_contratos_selecionado.merge(df_projetos_selecionado, on='codigo_projeto', how='left')
    df_portfolio = df_portfolio.merge(df_classificacao_projeto_selecionado, on='codigo_projeto', how='left')
    # df_portfolio = df_portfolio.merge(df_projetos_contratados_selecionados, on='codigo_projeto', how='left')

    # Adicionar a coluna "data_extracao_dados" com a data de hoje
    df_portfolio['data_extracao_dados'] = datetime.now().strftime('%d/%m/%Y')

    # Reordenar as colunas conforme especificado
    colunas_finais = [
        "codigo_projeto",
        "unidade_embrapii",
        "data_contrato",
        "data_inicio",
        "data_termino",
        "status",
        "tipo_projeto",
        "parceria_programa",
        "call",
        "cooperacao_internacional",
        "modalidade_financiamento",
        "uso_recurso_obrigatorio",
        "tecnologia_habilitadora",
        "area_aplicacao",
        "projeto",
        "trl_inicial",
        "trl_final",
        "valor_embrapii",
        "valor_empresa",
        "valor_unidade_embrapii",
        "titulo",
        "titulo_publico",
        "objetivo",
        "descricao_publica",
        "data_avaliacao",
        "nota_avaliacao",
        "observacoes",
        "tags",
        "data_extracao_dados",
    ]
    df_portfolio = df_portfolio[colunas_finais]

    # Tratar campos de data e valores
    campos_data = [
        "data_contrato",
        "data_inicio",
        "data_termino",
        "data_avaliacao",
        "data_extracao_dados",
    ]
    campos_valores = [
        "valor_embrapii",
        "valor_empresa",
        "valor_unidade_embrapii",
    ]

    for campo in campos_data:
        df_portfolio[campo] = pd.to_datetime(df_portfolio[campo], errors='coerce')

    for campo in campos_valores:
        df_portfolio[campo] = df_portfolio[campo].apply(pd.to_numeric, errors='coerce').fillna(0)

    # Garantir que o diretório de destino existe
    os.makedirs(destino, exist_ok=True)

    # Salvar o arquivo resultante
    with pd.ExcelWriter(arquivo_destino, engine='xlsxwriter') as writer:
        df_portfolio.to_excel(writer, index=False, sheet_name='Portfolio')

        # Acessar o workbook e worksheet
        workbook = writer.book
        worksheet = writer.sheets['Portfolio']

        # Definir largura das colunas
        for i, coluna in enumerate(df_portfolio.columns):
            col_idx = i
            worksheet.set_column(col_idx, col_idx, 20)

        # Aplicar formatação de data
        format_date = workbook.add_format({'num_format': 'dd/mm/yyyy'})
        for campo in campos_data:
            if campo in df_portfolio.columns:
                col_idx = df_portfolio.columns.get_loc(campo)
                worksheet.set_column(col_idx, col_idx, 20, format_date)

        # Aplicar formatação numérica
        format_currency = workbook.add_format({'num_format': '#,##0.00'})
        for campo in campos_valores:
            if campo in df_portfolio.columns:
                col_idx = df_portfolio.columns.get_loc(campo)
                worksheet.set_column(col_idx, col_idx, 20, format_currency)

    print(f"Tabela 'portfolio' criada com sucesso em: {arquivo_destino}")

# Exemplo de chamada da função
if __name__ == "__main__":
    criar_tabela_portfolio()
