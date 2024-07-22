import os
import shutil

def copiar_e_renomear_arquivos():

    # Define o caminho base relativo ao script
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

    origens = {
        'contratos': os.path.join(base_dir, 'projeto', 'contratos', 'step_3_data_processed', 'contratos.xlsx'),
        'projetos': os.path.join(base_dir, 'projeto', 'projetos', 'step_3_data_processed', 'projetos.xlsx'),
        'classificacao_projeto': os.path.join(base_dir, 'projeto', 'classificacao_projeto', 'step_3_data_processed', 'classificacao_projeto.xlsx')
    }

    # Define o caminho relativo da pasta de destino
    destino = os.path.join(base_dir, 'projeto', 'portfolio', 'step_1_data_raw')

    # Renomeia os arquivos ao copiar
    renomeios = {
        'contratos': 'raw_contratos.xlsx',
        'projetos': 'raw_projetos.xlsx',
        'classificacao_projeto': 'raw_classificacao_projeto.xlsx'
    }

    for chave, caminho_origem in origens.items():
        # Verifica se o arquivo de origem existe
        if not os.path.isfile(caminho_origem):
            print(f"Atenção: O arquivo {caminho_origem} não foi encontrado.")
            continue
        
        arquivo_destino = os.path.join(destino, renomeios[chave])
        
        # Copia e renomeia o arquivo
        shutil.copy2(caminho_origem, arquivo_destino)
    
    
    print(f"Arquivos copiados com sucesso!")


# Executa a função
# copiar_e_renomear_arquivos(origens, destino, renomeios)
