from scripts_public.baixar_dados_srinfo import baixar_dados_srinfo
from scripts_public.mover_arquivos import mover_arquivos_excel

def main_contratos():
    link = 'https://srinfo.embrapii.org.br/projects/contracts/'
    numero_arquivos = baixar_dados_srinfo(link)
    print('Número de arquivos: ', numero_arquivos)
    pasta_download = r'C:\Users\allan.ribeiro\Downloads'
    diretorio = r'C:\Users\allan.ribeiro\OneDrive\Embrapii\ETL_SRInfo\projeto'
    nome_arquivo = 'contratos'
    mover_arquivos_excel(numero_arquivos, pasta_download, diretorio, nome_arquivo)
    print('Finalizado!')


if __name__ == "__main__":
    main_contratos()