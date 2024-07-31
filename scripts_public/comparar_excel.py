import os
import sys
import pandas as pd
from dotenv import load_dotenv

# Carregar .env
load_dotenv()
ROOT = os.getenv('ROOT')
sys.path.append(ROOT)

def comparar_excel():

    # Caminhos dos arquivos
    DWPII_COPY = os.path.abspath(os.path.join(ROOT, 'DWPII_copy'))
    DWPII_UP = os.path.abspath(os.path.join(ROOT, 'DWPII_up'))

    # Leitura das planilhas
    copy = pd.read_excel(os.path.abspath(os.path.join(DWPII_COPY, "projetos_empresas.xlsx")))
    up = pd.read_excel(os.path.abspath(os.path.join(DWPII_UP, "projetos_empresas.xlsx")))
    classif = pd.read_excel(os.path.abspath(os.path.join(DWPII_UP, "classificacao_projeto.xlsx")))

    # Calculando numero de novos projetos, novas empresas e numero de projetos sem classificacao 
    proj = len(up[~up['codigo_projeto'].isin(copy['codigo_projeto'])])
    emp = len(up[~up['cnpj'].isin(copy['cnpj'])])
    clas = len(classif[classif['Tecnologias Habilitadoras'] == 'Não definido'])

    return [proj, emp, clas]

# Executar função
if __name__ == "__main__":
    comparar_excel()