from scripts.buscar_dados_brutos import copiar_e_renomear_arquivos
from scripts.criar_tabela_portfolio import criar_tabela_portfolio

def main_portfolio():
    copiar_e_renomear_arquivos()
    criar_tabela_portfolio()
    print('Tabela portfolio criada com sucesso!')

if __name__ == "__main__":
    main_portfolio()
