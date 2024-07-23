import os
import sys

# Adicionar o caminho do diretório raiz ao sys.path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_root)

# Importar o módulo principal de contratos
from projeto.contratos.main_contratos import main_contratos
from projeto.projetos.main_projetos import main_projetos

def main_pipeline_srinfo():
    main_contratos()
    main_projetos()

if __name__ == "__main__":
    main_pipeline_srinfo()
