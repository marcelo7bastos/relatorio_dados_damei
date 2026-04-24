# Relatório de Dados DAMEI

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/marcelo7bastos/relatorio_dados_damei/blob/main/notebooks/proposta_marcelo.ipynb)

Projeto para gerar relatórios estaduais de monitoramento das políticas públicas do MDA a partir de bases mantidas no Google Drive, com foco em reprodutibilidade, documentação e colaboração via GitHub, VS Code e Google Colab.

O objetivo é produzir documentos `.docx` próximos ao modelo `templates/documento_padrao_v1.docx`, inicialmente para uma UF por execução e, em evolução posterior, para as 27 UFs em lote.

O GitHub é a fonte oficial do código, da documentação e do template. O Google Drive é o repositório operacional dos dados e dos relatórios gerados.

## Status do Projeto

Projeto em estruturação inicial.

Nesta fase, o foco é:

- organizar o repositório;
- documentar requisitos e decisões;
- trabalhar no notebook `notebooks/proposta_marcelo.ipynb`;
- consolidar a leitura das bases atuais no Google Drive;
- gerar a primeira versão do relatório Word.

## Estrutura

```text
relatorio_dados_damei/
├─ dados_brutos/
│  ├─ dado_atual/
│  └─ dado_historico/
├─ docs/
│  └─ PRD.md
├─ notebooks/
│  ├─ proposta_marcelo.ipynb
│  └─ proposta_wesley.ipynb
├─ relatorios_gerados/
├─ templates/
│  └─ documento_padrao_v1.docx
├─ .gitignore
├─ README.md
└─ requirements.txt
```

## Dados

Os dados oficiais ficam no Google Drive.

A pasta local abaixo existe como apoio para testes e para preservar a estrutura esperada pelo projeto, mas não é a fonte oficial dos dados:

```text
dados_brutos/dado_atual/
```

Arquivos de dados, como `.xlsx`, `.csv` e `.parquet`, não devem ser enviados ao GitHub. O repositório versiona apenas a estrutura de pastas, código, documentação e templates.

## Ambiente Local

No PowerShell, dentro da pasta do projeto:

```powershell
pip install -r requirements.txt
code .
```

Nesta fase, o projeto será executado sem ambiente virtual. O notebook deve usar o Python local selecionado no VS Code.

No VS Code local, o notebook usa automaticamente:

```python
MODO_DADOS = "local"
```

Nesse modo, ele lê uma cópia local/mock em:

```text
dados_brutos/dado_atual/
```

O modo `google_drive` é acionado automaticamente quando o notebook roda no Google Colab.

## Google Colab

O Colab será usado como ambiente colaborativo de execução. O fluxo esperado é:

1. abrir o notebook no Colab;
2. clonar ou atualizar este repositório;
3. instalar as dependências com `requirements.txt`;
4. montar o Google Drive;
5. apontar o caminho da pasta de dados;
6. apontar o caminho da pasta de saída;
7. executar o notebook;
8. gerar o relatório `.docx` diretamente no Google Drive.

No Colab, o notebook usa automaticamente:

```python
MODO_DADOS = "google_drive"
```

Exemplo de instalação no Colab:

```python
!pip install -r requirements.txt
```

## Dependências

As dependências principais estão em `requirements.txt`:

- `pandas`: leitura e tratamento dos dados;
- `openpyxl`: leitura de arquivos Excel;
- `python-docx`: geração de documentos Word;
- `ipykernel`: execução dos notebooks no VS Code.

## Saídas

Nesta fase, os relatórios gerados no Colab devem ser salvos no Google Drive em:

```text
/content/drive/MyDrive/MDA/dado_atual
```

Esse caminho está configurado no notebook como `GOOGLE_DRIVE_OUTPUT_DIR`.

Formato esperado do arquivo final:

```text
relatorio_estadual_monitoramento_<UF>_<AAAAMMDDHHMMSS>.docx
```

## Decisões Principais

- A primeira versão gera uma UF por execução.
- A UF deve poder ser informada por sigla ou código IBGE.
- O relatório é exclusivamente estadual.
- Dados faltantes devem aparecer com o texto: `Informação não disponível nas bases atuais.`
- Dados brutos e relatórios gerados não devem ser versionados.
- O Google Drive é o repositório operacional dos dados.
- O Google Drive é o destino operacional dos relatórios gerados.
- O template `templates/documento_padrao_v1.docx` deve ser versionado.
- A geração do documento será feita com `python-docx`.

## Documentação

O PRD do projeto está em:

```text
docs/PRD.md
```

Ele registra o escopo, requisitos, critérios de aceite, decisões tomadas e questões em aberto.
