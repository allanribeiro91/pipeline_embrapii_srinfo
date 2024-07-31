import pandas as pd
import os
import sys
from dotenv import load_dotenv

#carregar .env
load_dotenv()
ROOT = os.getenv('ROOT')

def new_classificacao_projeto():

    # Define os caminhos das planilhas
    path_projetos_contratados = os.path.join(ROOT, 'projeto', 'classificacao_projeto', 'step_1_data_raw', 'raw_projetos_contratados.xlsx')
    path_empresas_contratantes = os.path.join(ROOT, 'projeto', 'classificacao_projeto', 'step_1_data_raw', 'raw_empresas_contratantes.xlsx')
    path_cnae = os.path.join(ROOT, 'projeto', 'classificacao_projeto', 'step_1_data_raw', 'raw_cnae_divisao.xlsx')
    path_ues = os.path.join(ROOT, 'projeto', 'classificacao_projeto', 'step_1_data_raw', 'raw_competencias_ues.xlsx')
    path_destino = os.path.join(ROOT, 'projeto', 'classificacao_projeto', 'step_2_stage_area', 'new_classificacao_projeto.xlsx')

    # Ler as planilhas
    df_projetos_contratados = pd.read_excel(path_projetos_contratados)
    df_empresas_contratantes = pd.read_excel(path_empresas_contratantes)
    df_cnae = pd.read_excel(path_cnae)
    df_ues = pd.read_excel(path_ues)

    #buscar os dados de competências das UEs
    df_merged = df_projetos_contratados.merge(
        df_ues[['unidade_embrapii', 'grande_area_competencia', 'competencia']],
            left_on='Unidade EMBRAPII',
            right_on='unidade_embrapii',
            how='left'
    )
    
    #buscar informações das empresas
    # --> Criar planilha normalizada de projetos e empresas
    df_projetos_contratados_empresas_norm = normalizar_empresas_projetos_contratados(df_projetos_contratados)
    df_empresas_norm_merged = mesclar_dados_empresas(df_projetos_contratados_empresas_norm, df_empresas_contratantes, df_cnae)

    #mesclar os dados de empresas
    df_merged = df_merged.drop(columns=["Empresas", "Faixa de faturamento declarada", "CNAE", "CNPJ"])
    df_merged = df_merged.merge(df_empresas_norm_merged, on='Código', how='left')
    
    # Criar novas colunas
    df_merged["tecnologia_habilitadora"] = ""
    df_merged["area_aplicacao"] = ""


    #remover colunas
    colunas_remover = [
        "Unnamed: 0",
        "Macroentregas",
        "% de Aceites",
        "Status",
        "Data de início",
        "Data de término",
        "É usada obrigatoriedade?",
        "Tags",
        "project_context",
        "Negociação",
        "Parcerias",
        "Modalidade de financiamento",
        "Cooperação Internacional",
        "UF",
        "Faixa de empregados declarada_x",
        "unidade_embrapii",
        "CNPJ",
        "Faixa de faturamento declarada",
        "Faixa de empregados declarada_y",
    ]
    df_merged = df_merged.drop(columns=colunas_remover)

    #contar número de empresas
    def contar_empresas(empresas):
        if pd.isna(empresas) or empresas == "":
            return 0
        return empresas.count(';') + 1
    
    df_merged['Número de Empresas no Projeto'] = df_merged['Empresas'].apply(contar_empresas)

    # Renomear e reordenar as colunas
    df_merged = df_merged.rename(columns={
        'Código': 'Código',
        'Unidade EMBRAPII': 'Unidade EMBRAPII',
        'Empresas': 'Empresas',
        'porte_cnpj': 'Porte da Empresa',
        'Número de Empresas no Projeto': 'Número de Empresas no Projeto',
        'agrupamento': 'Agrupamento Div CNAE',
        'CNAE': 'CNAE Divisão',
        'nomenclatura': 'Nomenclatura CNAE Divisão',
        'grande_area_competencia': 'Grande Área de Competência',
        'competencia': 'Competência UE',
        'tecnologia_habilitadora': 'Tecnologias Habilitadoras',
        'area_aplicacao': 'Áreas de Aplicação',
        'Projeto': 'Projeto',
        'Título público': 'Título público',
        'Objetivo': 'Objetivo',
        'Descrição pública': 'Descrição pública',
        'Tipo de projeto': 'Tipo de projeto',
        'Call': 'Call',
        'Data do contrato': 'Data do contrato',
        'Nível de maturidade inicial': 'Nível de maturidade inicial',
        'Nível de maturidade final': 'Nível de maturidade final',
        'Valor total': 'Valor total',
        'Valor aportado EMBRAPII': 'Valor aportado EMBRAPII',
        'Valor aportado Empresa': 'Valor aportado Empresa',
        'Valor aportado Unidade': 'Valor aportado pela Unidade',
        'Pedidos de propriedade Intelectual': 'Pedidos de Propriedade Intelectual'
    })

    # Ordem das colunas conforme a lista fornecida
    colunas_ordenadas = [
        'Código',
        'Unidade EMBRAPII',
        'Empresas',
        'Porte da Empresa',
        'Número de Empresas no Projeto',
        'Agrupamento Div CNAE',
        'CNAE Divisão',
        'Nomenclatura CNAE Divisão',
        'Grande Área de Competência',
        'Competência UE',
        'Tecnologias Habilitadoras',
        'Áreas de Aplicação',
        'Projeto',
        'Título público',
        'Objetivo',
        'Descrição pública',
        'Tipo de projeto',
        'Call',
        'Data do contrato',
        'Nível de maturidade inicial',
        'Nível de maturidade final',
        'Valor total',
        'Valor aportado EMBRAPII',
        'Valor aportado Empresa',
        'Valor aportado pela Unidade',
        'Pedidos de Propriedade Intelectual'
    ]

    # Reordenar as colunas
    df_merged = df_merged[colunas_ordenadas]

    # Função para extrair os dois primeiros dígitos do CNAE
    def extrair_dois_primeiros_digitos(cnae):
        try:
            return int(cnae[:2]) if cnae else None
        except ValueError:
            return None

    df_merged['CNAE Divisão'] = df_merged['CNAE Divisão'].apply(extrair_dois_primeiros_digitos)

    # Ajustar campo de data: 'Data do contrato'
    df_merged['Data do contrato'] = pd.to_datetime(df_merged['Data do contrato'], format='%d/%m/%Y')

    # Função para converter valores monetários de texto para formato numérico
    def converter_valores(valor):
        try:
            return float(valor.replace('.', '').replace(',', '.'))
        except ValueError:
            return None

    # Ajustar os campos de valores
    campos_valores = ['Valor total', 'Valor aportado EMBRAPII', 'Valor aportado Empresa', 'Valor aportado pela Unidade']
    for campo in campos_valores:
        df_merged[campo] = df_merged[campo].apply(converter_valores)

    
    # Salvar em Excel com formatação
    with pd.ExcelWriter(path_destino, engine='xlsxwriter') as writer:
        df_merged.to_excel(writer, sheet_name='Sheet1', index=False)
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # Formatos
        format_date = workbook.add_format({'num_format': 'dd/mm/yyyy'})
        format_currency = workbook.add_format({'num_format': 'R$ #,##0.00'})

        # Aplicar formatação
        worksheet.set_column('T:T', None, format_date)
        for col in ['V', 'W', 'X', 'Y']:
            worksheet.set_column(f'{col}:{col}', None, format_currency)


def normalizar_empresas_projetos_contratados(df):
    # Selecionar as colunas Código, CNPJ, CNAE e Empresas
    df_selecionado = df[['Código', 'CNPJ', 'CNAE', 'Empresas']]
    
    # Transpor os valores, quebrando pelos valores que estão em CNPJ, CNAE e Empresas separados por vírgula
    data = {
        'Código': [],
        'CNPJ': [],
        'CNAE': [],
        'Empresas': []
    }
    
    for index, row in df_selecionado.iterrows():
        cnpjs = row['CNPJ'].split(';')
        cnaes = row['CNAE'].split(';')
        empresas = row['Empresas'].split(';')
        
        max_len = max(len(cnpjs), len(cnaes), len(empresas))
        
        for i in range(max_len):
            data['Código'].append(row['Código'])  # Replicar o código para cada linha
            data['CNPJ'].append(cnpjs[i] if i < len(cnpjs) else None)
            data['CNAE'].append(cnaes[i] if i < len(cnaes) else None)
            data['Empresas'].append(empresas[i] if i < len(empresas) else None)
    
    # Criar um novo dataframe com os dados normalizados
    novo_df = pd.DataFrame(data)
    
    return novo_df


import pandas as pd

def mesclar_dados_empresas(df_empresas_norm, df_empresas_contratantes, df_cnae):
    # Selecionar as colunas necessárias de df_empresas_contratantes
    df_contratantes = df_empresas_contratantes[['CNPJ', 'Faixa de faturamento declarada', 'Faixa de empregados declarada']]

    # Função para obter o último valor de uma lista separada por vírgulas
    def obter_ultimo_valor(valor):
        if pd.isna(valor):
            return "Não informado"
        ultimo_valor = valor.split(';')[-1].strip()
        return "Não Informado" if ultimo_valor == "N/D" else ultimo_valor

    # Aplicar a função para obter o último valor e ajustar os campos
    df_contratantes['Faixa de faturamento declarada'] = df_contratantes['Faixa de faturamento declarada'].apply(obter_ultimo_valor)
    df_contratantes['Faixa de empregados declarada'] = df_contratantes['Faixa de empregados declarada'].apply(obter_ultimo_valor)

    # Mesclar os dataframes com base na coluna CNPJ
    df_merged = df_empresas_norm.merge(df_contratantes, on='CNPJ', how='left')

    # Criar a coluna CNAE_parte com os dois primeiros dígitos do CNAE
    df_merged['CNAE'] = df_merged['CNAE'].fillna('')

    # Função para extrair os dois primeiros dígitos do CNAE
    def extrair_dois_primeiros_digitos(cnae):
        try:
            return int(cnae[:2]) if cnae else None
        except ValueError:
            return None

    df_merged['CNAE_parte'] = df_merged['CNAE'].apply(extrair_dois_primeiros_digitos)

    # Mesclar dados do CNAE
    df_merged = df_merged.merge(df_cnae, left_on='CNAE_parte', right_on='cnae_divisao', how='left')

    # Criar a coluna porte_cnpj com base na Faixa de faturamento declarada
    def determinar_porte(faixa):
        if faixa == "Até R$ 360 mil":
            return "Microempresa"
        elif faixa == "Entre R$ 360 mil e R$ 4,8 milhões":
            return "Pequena"
        elif faixa == "Entre R$ 4,8 e R$ 300 milhões":
            return "Média"
        elif faixa == "Maior que R$ 300 milhões":
            return "Grande"
        elif faixa == "Não Informado":
            return "Não Informado"
        else:
            return "Não informado"
    df_merged['porte_cnpj'] = df_merged['Faixa de faturamento declarada'].apply(determinar_porte)

    # Agregar os dados pelo Código
    df_aggregated = df_merged.groupby('Código').agg({
        'CNPJ': lambda x: '; '.join(x.dropna().astype(str)),
        'CNAE': lambda x: '; '.join(x.dropna().astype(str)),
        'Empresas': lambda x: '; '.join(x.dropna().astype(str)),
        'Faixa de faturamento declarada': lambda x: '; '.join(x.dropna().astype(str)),
        'Faixa de empregados declarada': lambda x: '; '.join(x.dropna().astype(str)),
        'agrupamento': lambda x: '; '.join(x.dropna().astype(str)),
        'nomenclatura': lambda x: '; '.join(x.dropna().astype(str)),
        'porte_cnpj': lambda x: '; '.join(x.dropna().astype(str))
    }).reset_index()

    return df_aggregated

#Executar função
if __name__ == "__main__":
    new_classificacao_projeto()