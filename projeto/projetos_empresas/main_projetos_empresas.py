from scripts.copiar_e_renomear_arquivos import copiar_e_renomear_arquivos
from scripts.new_classificacao_projeto import new_classificacao_projeto
from scripts.atualizacao_classificacao_projeto import atualizacao_classificao_projeto

def main_classificacao_projeto():
    copiar_e_renomear_arquivos()
    new_classificacao_projeto()
    atualizacao_classificao_projeto()
    print('Tabela classificacao_projeto concluída com sucesso!')

if __name__ == "__main__":
    main_classificacao_projeto()
