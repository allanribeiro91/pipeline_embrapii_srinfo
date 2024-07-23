import pandas as pd
import os
import sys
from dotenv import load_dotenv

#carregar .env
load_dotenv()
ROOT = os.getenv('ROOT')

def new_classificacao_projeto():

    # Define os caminhos das planilhas
    caminho_projetos = os.path.join(ROOT, 'projeto', 'classificacao_projeto', 'step_1_data_raw', 'raw_projetos.xlsx')
    caminho_unidades_embrapii = os.path.join(ROOT, 'projeto', 'classificacao_projeto', 'step_1_data_raw', 'raw_unidades_embrapiis.xlsx')
    caminho_destino = os.path.join(ROOT, 'projeto', 'classificacao_projeto', 'step_2_stage_area', 'new_classificacao_projeto.xlsx')

    # Ler as planilhas
    df_projetos = pd.read_excel(caminho_projetos)
    df_unidades_embrapii = pd.read_excel(caminho_unidades_embrapii)

    # Selecionar as colunas desejadas
    colunas_projetos = [
        "Código EMBRAPII", 
        "Unidade EMBRAPII", 
        "Empresas", "Parceria / Programa", 
        "Tipo de projeto", 
        "Título", 
        "Título público", 
        "Objetivo", 
        "Descrição pública"]
    df_projetos_selecionado = df_projetos[colunas_projetos]

    colunas_unidades_embrapii = [
        "Unidade EMBRAPII", 
        "Tipo de Instituição", 
        "Competências Técnicas", 
        "Linhas de Atuação"]
    df_unidades_embrapii_selecionado = df_unidades_embrapii[colunas_unidades_embrapii]

    # Mesclar os dados com base na chave "Unidade EMBRAPII"
    df_merged = pd.merge(df_projetos_selecionado, df_unidades_embrapii_selecionado, on="Unidade EMBRAPII", how="left")

    # Criar novas colunas
    df_merged["tecnologia_habilitadora"] = ""
    df_merged["area_aplicacao"] = ""
    df_merged["data_avaliacao"] = ""

    # Renomear e reordenar as colunas
    df_merged = df_merged.rename(columns={
        "Código EMBRAPII": "codigo_projeto",
        "Tipo de Instituição": "ue_tipo",
        "Unidade EMBRAPII": "ue_nome",
        "Competências Técnicas": "ue_competencias",
        "Linhas de Atuação": "ue_linhas_atuacao",
        "Empresas": "empresas",
        "Parceria / Programa": "parceria_programa",
        "Tipo de projeto": "tipo_projeto",
        "Título": "titulo",
        "Título público": "titulo_publico",
        "Objetivo": "objetivo",
        "Descrição pública": "descricao_publica"
    })

    # Definir a ordem das colunas
    ordem_colunas = [
        "codigo_projeto",
        "ue_tipo",
        "ue_nome",
        "ue_competencias",
        "ue_linhas_atuacao",
        "empresas",
        "parceria_programa",
        "tipo_projeto",
        "titulo",
        "titulo_publico",
        "objetivo",
        "descricao_publica",
        "tecnologia_habilitadora",
        "area_aplicacao",
        "data_avaliacao"
    ]

    df_final = df_merged[ordem_colunas]

    # Salvar a nova planilha no formato xlsx
    df_final.to_excel(caminho_destino, index=False)

    print(f"Planilha salva em {caminho_destino}")

#Executar função
if __name__ == "__main__":
    new_classificacao_projeto()