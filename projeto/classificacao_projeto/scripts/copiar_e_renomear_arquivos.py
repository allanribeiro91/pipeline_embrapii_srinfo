import os
import shutil

def copiar_e_renomear_arquivos():

    # Define o caminho base relativo ao script
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

    origens = {
        'empresas': os.path.join(base_dir, 'empresa', 'info_empresas', 'step_2_stage_area', 'info_empresas.xlsx'),
        'projetos': os.path.join(base_dir, 'projeto', 'projetos', 'step_2_stage_area', 'info_projetos.xlsx'),
        'unidades_embrapiis': os.path.join(base_dir, 'unidade_embrapii', 'info_unidades', 'step_2_stage_area', 'info_unidades_embrapiis.xlsx'),
        'classificacao_projeto': os.path.join(base_dir, 'DWPII_copy', 'classificacao_projeto.xlsx')
    }

    # Define o caminho relativo da pasta de destino
    destino = os.path.join(base_dir, 'projeto', 'classificacao_projeto', 'step_1_data_raw')

    # Renomeia os arquivos ao copiar
    renomeios = {
        'empresas': 'raw_empresas.xlsx',
        'projetos': 'raw_projetos.xlsx',
        'unidades_embrapiis': 'raw_unidades_embrapiis.xlsx',
        'classificacao_projeto': 'atual_classificacao_projeto.xlsx'
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
