from baixar_dados_srinfo import baixar_dados_srinfo
from mover_arquivos import mover_arquivos_excel
from append_arquivos import append_excel_files

def teste():
    link = 'https://srinfo.embrapii.org.br/projects/contracts/'
    numero_arquivos = baixar_dados_srinfo(link)
    pasta_download = r'C:\Users\allan.ribeiro\Downloads'
    diretorio = r'C:\Users\allan.ribeiro\OneDrive\Embrapii\ETL_SRInfo\projeto\contratos'
    nome_arquivo = 'contratos'
    mover_arquivos_excel(numero_arquivos, pasta_download, diretorio, nome_arquivo)
    append_excel_files(diretorio, nome_arquivo)
    print('Finalizado!')


if __name__ == "__main__":
    teste()