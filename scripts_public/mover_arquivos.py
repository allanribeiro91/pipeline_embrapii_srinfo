import os
import shutil
from glob import glob
from datetime import datetime

def mover_arquivos_excel(numero_arquivos, pasta_download, diretorio, nome_arquivo):

    data_raw = os.path.join(diretorio, 'data_raw')
    data_log = os.path.join(diretorio, 'data_log')

    # Mover arquivos da pasta data_raw para a pasta data_log
    for file in os.listdir(data_raw):
        file_path = os.path.join(data_raw, file)
        dest_path = os.path.join(data_log, file)
        try:
            if os.path.isfile(file_path):
                if os.path.exists(dest_path):
                    os.remove(dest_path)
                shutil.move(file_path, data_log)
        except Exception as e:
            print(f'Erro ao mover {file_path}. Razão: {e}')

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
        novo_nome = f"{nome_arquivo}_{data_atual}_{i}.xlsx"
        novo_caminho = os.path.join(data_raw, novo_nome)
        try:
            shutil.move(file, novo_caminho)
        except Exception as e:
            print(f'Erro ao mover {file} para {novo_caminho}. Razão: {e}')
