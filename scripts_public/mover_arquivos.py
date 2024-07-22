import os
import shutil
from glob import glob
from datetime import datetime

def mover_arquivos_excel(numero_arquivos, pasta_download, diretorio, nome_arquivo):

    data_raw = os.path.join(diretorio, 'step_1_data_raw')
    # data_log = os.path.join(diretorio, 'data_log')

    # Apagar os arquivos da data_raw
    for file in os.listdir(data_raw):
        file_path = os.path.join(data_raw, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Falha ao deletar {file_path}. Razão: {e}')

    #Lista todos os arquivos Excel na pasta Downloads
    files = glob(os.path.join(pasta_download, '*.xlsx'))
    
    #Ordena os arquivos por data de modificação (mais recentes primeiro)
    files.sort(key=os.path.getmtime, reverse=True)
    
    #Seleciona os n arquivos mais recentes
    files_to_move = files[:numero_arquivos]

    #Obtém a data atual no formato aaaa.mm.dd
    data_atual = datetime.now().strftime('%Y.%m.%d')
    
    # Move os arquivos selecionados para a pasta data_raw com renome
    for i, file in enumerate(files_to_move, start=1):
        novo_nome = f"{nome_arquivo}.xlsx"
        novo_caminho = os.path.join(data_raw, novo_nome)
        try:
            shutil.move(file, novo_caminho)
        except Exception as e:
            print(f'Erro ao mover {file} para {novo_caminho}. Razão: {e}')
