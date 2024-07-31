<h1>pipeline_embrapii_srinfo</h1>

<h2>Objetivo</h2>
<p>O <b>pipeline_embrapii_srinfo</b> tem como objetivo realizar a extração, transformação e carga de dados do SRInfo da Embrapii para o DWPII.
  <br>Este processo automatizado visa facilitar a integração e a análise dos dados, garantindo que estejam prontos para uso em relatórios e outras aplicações analíticas.</p>

<h2>Sequência lógica do script</h2>
- Ver o main_pipeline_srinfo.py
1. Faz uma cópia dos dados do DWPII
Acessa a pasta do Sharepoint e faz cópia dos arquivos atuais.
2. Baixa os dados do SRInfo
Acessa o SRInfo e baixa os dados das diferentes tabelas.
3. Cria a tabelas normalizadas
Processa os dados: retirada de dados redundantes, padronização do nome dos campos e das chaves primárias e secundárias e criação das tabelas normalizadas.
4. Registra os logs
Registra as operações realizadas em uma tabela de logs.
5. Carrega os dados no DWPII backup
Cria um arquivo .zip com as planilhas atuais que foram baixadas no início do script e salva em uma pasta específica do sharepoint.
6. Carrega os dados no DWPII
Carrega os novos arquivos processados na pasta do Sharepoint.
7. Envia mensagem no whatsapp
Encaminha mensagem com resumo da operação para o grupo do whatsapp.

<h2>Como usar</h2>
1. clone o repositório: git clone https://github.com/allanribeiro91/pipeline_embrapii_srinfo.git
2. cd pipeline_embrapii_srinfo
3. virtualenv .venv
4. .venv/Scripts/Activate 
5. pip install -r requirements.txt
6. python main_pipeline_srinfo.py 

<h2>Requisito</h2>
- Criar o arquivo .env:
USERNAME= <i>incluir o nome de usuário de acesso ao srinfo</i>
PASSWORD= <i>incluir a senha de acesso ao srinfo</i>

PASTA_DOWNLOAD= <i>incluir o caminho para a pasta downloads (onde os arquivos serão baixados)</i>
ROOT= <i>incluir o caminho da pasta root do projeto</i>

sharepoint_email= <i>incluir o email de acesso ao sharepoint</i>
sharepoint_password= <i>incluir a senha de acesso ao sharepoint</i>
sharepoint_url_site="https://embrapii.sharepoint.com/sites/GEEDD"
sharepoint_site_name="GEEDD"
sharepoint_doc_library="Documentos Compartilhados/"
