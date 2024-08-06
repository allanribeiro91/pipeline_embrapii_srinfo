import os
import sys
from dotenv import load_dotenv
import win32com.client as win32
import time

#Carregar variáveis de ambiente
load_dotenv()
ROOT = os.getenv('ROOT')

#Caminhos
DWPII_UP = os.path.abspath(os.path.join(ROOT, 'DWPII_up'))
PATH_OFFICE = os.path.abspath(os.path.join(ROOT, 'office365_api'))

# Adiciona o diretório correto ao sys.path
sys.path.append(PATH_OFFICE)

from upload_files import upload_files

# Definir caminhos
SNAPSHOT_FOLDER = os.path.abspath(os.path.join(ROOT, 'report_snapshot'))
SNAPSHOT_FILE = os.path.abspath(os.path.join(SNAPSHOT_FOLDER, 'report_snapshot_embrapii.xlsx'))

def gerar_report_snapshot():
    # Inicializar o Excel
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = False

    # Abrir a planilha
    workbook = excel.Workbooks.Open(SNAPSHOT_FILE)

    # Atualizar todas as conexões e consultas de dados
    workbook.RefreshAll()

    # Aguardar a conclusão da atualização (adicionar um atraso)
    print("Aguardando a atualização das consultas...")
    time.sleep(120) 

    # Definir caminho para salvar o PDF
    pdf_path = os.path.join(SNAPSHOT_FOLDER, 'report_snapshot_embrapii.pdf')

    # Exportar para PDF
    workbook.ExportAsFixedFormat(0, pdf_path)

    # Fechar o workbook e o Excel
    workbook.Close(False)
    excel.Application.Quit()

    levar_relatorio_snapshot()


def levar_relatorio_snapshot():
    upload_files(SNAPSHOT_FOLDER, "Reports")
