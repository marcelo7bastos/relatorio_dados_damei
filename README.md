# Relatório de Dados DAMEI

Projeto para gerar relatórios estaduais de monitoramento das políticas públicas do MDA a partir de bases locais, com foco em reprodutibilidade, documentação e colaboração via GitHub, VS Code e Google Colab.

O objetivo é produzir documentos `.docx` próximos ao modelo `templates/documento_padrao_v1.docx`, inicialmente para uma UF por execução e, em evolução posterior, para as 27 UFs em lote.

## Status do Projeto

Projeto em estruturação inicial.

Nesta fase, o foco é:

- organizar o repositório;
- documentar requisitos e decisões;
- trabalhar no notebook `notebooks/proposta_marcelo.ipynb`;
- consolidar a leitura das bases atuais;
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

Os dados ficam localmente em:

```text
dados_brutos/dado_atual/
```

Arquivos de dados, como `.xlsx`, `.csv` e `.parquet`, não devem ser enviados ao GitHub. O repositório versiona apenas a estrutura de pastas, código, documentação e templates.

## Ambiente Local

No PowerShell, dentro da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
code .
```

Depois, no VS Code, selecione o kernel Python do ambiente `.venv` para executar os notebooks.

## Google Colab

O Colab será usado como ambiente colaborativo de execução. O fluxo esperado é:

1. abrir o notebook no Colab;
2. clonar ou atualizar este repositório;
3. instalar as dependências com `requirements.txt`;
4. montar o Google Drive, se necessário;
5. apontar o caminho da pasta de dados;
6. executar o notebook;
7. gerar o relatório `.docx`.

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

Os relatórios gerados devem ser salvos em:

```text
relatorios_gerados/AAAAMM/
```

Onde `AAAAMM` é criado a partir da data do sistema no momento da execução.

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
- O template `templates/documento_padrao_v1.docx` deve ser versionado.
- A geração do documento será feita com `python-docx`.

## Documentação

O PRD do projeto está em:

```text
docs/PRD.md
```

Ele registra o escopo, requisitos, critérios de aceite, decisões tomadas e questões em aberto.

