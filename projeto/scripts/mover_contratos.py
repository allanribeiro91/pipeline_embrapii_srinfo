import os
import shutil
from glob import glob

def mover_contratos():

    downloads_folder = r'C:\Users\milena.goncalves\Downloads'
    data_raw_folder = r'C:\Users\milena.goncalves\OneDrive - Associação Brasileira de Pesquisa e Inovação Industrial - EMBRAPII\etl_srinfo\projeto\data_raw'

    # Verifica se a pasta data_raw existe, se não, cria
    if not os.path.exists(data_raw_folder):
        os.makedirs(data_raw_folder)

    # Exclui todos os arquivos existentes na pasta data_raw
    for file in os.listdir(data_raw_folder):
        file_path = os.path.join(data_raw_folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Erro ao excluir {file_path}. Razão: {e}')

    # Lista todos os arquivos Excel na pasta Downloads
    files = glob(os.path.join(downloads_folder, '*.xlsx'))

    # Ordena os arquivos por data de modificação (mais recentes primeiro)
    files.sort(key=os.path.getmtime, reverse=True)
    
    # Seleciona o arquivo mais recente
    files_to_move = files[0]
    
    # Move os arquivos selecionados para a pasta data_raw
    shutil.move(files_to_move, data_raw_folder)


if __name__ == "__main__":
    mover_contratos()