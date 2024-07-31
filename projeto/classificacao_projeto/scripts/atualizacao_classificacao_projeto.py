import pandas as pd
import openpyxl
import os

def atualizacao_classificao_projeto():
    # Define os caminhos das planilhas
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    caminho_atual = os.path.join(base_dir, 'projeto', 'classificacao_projeto', 'step_1_data_raw', 'atual_classificacao_projeto.xlsx')
    caminho_new = os.path.join(base_dir, 'projeto', 'classificacao_projeto', 'step_2_stage_area', 'new_classificacao_projeto.xlsx')
    caminho_destino = os.path.join(base_dir, 'projeto', 'classificacao_projeto', 'step_3_data_processed', 'classificacao_projeto.xlsx')

    # Ler as planilhas
    df_atual = pd.read_excel(caminho_atual, sheet_name='Planilha1')
    df_new = pd.read_excel(caminho_new)

    # Identificar novos registros
    novos_registros = df_new[~df_new['Código'].isin(df_atual['Código'])]
    print(novos_registros.head())
    # Adicionar colunas com valor "Não definido" para os novos registros
    novos_registros['Tecnologias Habilitadoras'] = "Não definido"
    novos_registros['Áreas de Aplicação'] = "Não definido"

    # Carregar a planilha atual com openpyxl
    wb = openpyxl.load_workbook(caminho_atual)
    ws = wb['Planilha1']

    # Adicionar novos registros ao final da planilha atual
    for _, row in novos_registros.iterrows():
        ws.append(list(row))

    # Salvar a nova planilha temporariamente para manipulação com pandas
    caminho_temp = os.path.join(base_dir, 'projeto', 'classificacao_projeto', 'temp_classificacao_projeto.xlsx')
    wb.save(caminho_temp)

    # Recarregar a planilha temporária com pandas para reordenar
    df_final = pd.read_excel(caminho_temp, sheet_name='Planilha1')

    # Criar colunas auxiliares para priorizar "Não definido"
    df_final['Tecnologias Habilitadoras Prioridade'] = df_final['Tecnologias Habilitadoras'].apply(lambda x: 0 if x == "Não definido" else 1)
    df_final['Áreas de Aplicação Prioridade'] = df_final['Áreas de Aplicação'].apply(lambda x: 0 if x == "Não definido" else 1)

    # Ordenar priorizando "Não definido"
    df_final_sorted = df_final.sort_values(by=['Tecnologias Habilitadoras Prioridade', 'Áreas de Aplicação Prioridade', 'Tecnologias Habilitadoras', 'Áreas de Aplicação'])

    # Remover colunas auxiliares
    df_final_sorted = df_final_sorted.drop(columns=['Tecnologias Habilitadoras Prioridade', 'Áreas de Aplicação Prioridade'])

    # Salvar a planilha reordenada no caminho de destino
    df_final_sorted.to_excel(caminho_destino, index=False, sheet_name='Planilha1')

    # Ajustar as larguras das colunas
    wb_final = openpyxl.load_workbook(caminho_destino)
    ws_final = wb_final['Planilha1']

    for col in ws_final.columns:
        max_length = 30  # Largura desejada
        col_letter = col[0].column_letter  # Obter a letra da coluna
        ws_final.column_dimensions[col_letter].width = max_length

    wb_final.save(caminho_destino)

    # Remover o arquivo temporário
    os.remove(caminho_temp)

