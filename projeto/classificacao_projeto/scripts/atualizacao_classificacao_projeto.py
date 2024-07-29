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
    df_atual = pd.read_excel(caminho_atual, sheet_name='Sheet1')
    df_new = pd.read_excel(caminho_new)
    df_new = df_new[df_new['status'] != 'Desqualificado']

    # Identificar novos registros
    novos_registros = df_new[~df_new['codigo_projeto'].isin(df_atual['codigo_projeto'])]

    # Adicionar colunas com valor "Não definido" para os novos registros
    novos_registros['tecnologia_habilitadora'] = "Não definido"
    novos_registros['area_aplicacao'] = "Não definido"

    # Carregar a planilha atual com openpyxl
    wb = openpyxl.load_workbook(caminho_atual)
    ws = wb['Sheet1']

    # Adicionar novos registros ao final da planilha atual
    for _, row in novos_registros.iterrows():
        ws.append(list(row))

    # Salvar a nova planilha
    if not os.path.exists(os.path.dirname(caminho_destino)):
        os.makedirs(os.path.dirname(caminho_destino))

    wb.save(caminho_destino)
    print(f"Planilha salva em {caminho_destino}")

