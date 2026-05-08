# PRD - Relatório Estadual de Monitoramento DAMEI

## 1. Visão Geral

Este projeto tem como objetivo gerar, de forma reprodutível e versionada, relatórios estaduais de monitoramento das políticas públicas do MDA a partir das bases atuais mantidas no Google Drive.

O documento final deve se aproximar ao máximo do modelo existente em `templates/documento_padrao_v1.docx`, preservando sua lógica editorial, estrutura de seções, indicadores principais e forma geral de apresentação.

O produto deve permitir a geração mensal de relatórios para as 27 unidades federativas, com execução tanto no VS Code local quanto no Google Colab. O GitHub será a fonte oficial do código e da documentação; o Google Drive será o repositório operacional de dados e relatórios gerados.

## 2. Contexto

Existe uma demanda recorrente de produção de relatórios estaduais para acompanhamento regionalizado das políticas do MDA. Hoje esse trabalho depende de esforço manual de servidores públicos, com consulta às bases, cálculo de indicadores, montagem de tabelas e edição final do documento.

Há um protótipo anterior em notebook que gera arquivos Excel e Word, mas ele ainda não atende plenamente ao padrão desejado, pois depende de caminhos fixos, execução manual por células e ajustes pontuais. Este projeto deve transformar esse protótipo em um processo mais claro, documentado e reprodutível.

## 3. Problema

A geração atual dos relatórios é manual ou semiautomatizada, o que torna o processo lento, sujeito a inconsistências e difícil de repetir mensalmente para todas as UFs.

Além disso, o conhecimento do processo fica concentrado em quem executa os notebooks, dificultando colaboração, auditoria dos cálculos, versionamento e manutenção futura.

## 4. Objetivos

- Gerar documentos `.docx` a partir das bases atuais disponíveis no Google Drive.
- Reproduzir a estrutura do documento `templates/documento_padrao_v1.docx`.
- Permitir geração para qualquer UF, aceitando sigla (`MG`) ou código IBGE da UF.
- Permitir geração mensal dos relatórios.
- Automatizar cálculos nacionais, estaduais e percentuais UF/Brasil.
- Reduzir trabalho manual de cópia, colagem e formatação.
- Registrar claramente lacunas quando uma informação do modelo não existir nas bases disponíveis.
- Manter o código e a documentação versionados no GitHub.
- Permitir execução no VS Code e no Google Colab, para facilitar colaboração.
- Produzir notebooks bem documentados, com células markdown explicativas e células de código legíveis.

## 5. Não Objetivos Neste Primeiro Ciclo

- Criar uma aplicação web.
- Automatizar coleta de bases em sistemas externos.
- Versionar bases de dados brutas ou relatórios gerados no GitHub.
- Resolver todas as lacunas do modelo caso a informação não exista nas planilhas atuais.
- Produzir visual sofisticado além do padrão Word de referência.
- Substituir integralmente a validação humana do conteúdo final.
- Modularizar todo o código em pacote Python completo já na primeira versão.

## 6. Usuário Principal

Analista ou gestor técnico que precisa gerar relatórios estaduais de monitoramento com indicadores consolidados das políticas públicas do MDA.

O usuário deve conseguir executar o processo mensalmente, revisar os resultados, identificar lacunas e compartilhar os relatórios gerados.

## 7. Fonte de Verdade

### Código, documentação e template

- Repositório GitHub do projeto
- `docs/PRD.md`
- `README.md`
- `templates/documento_padrao_v1.docx`

### Dados e saídas operacionais

Os dados utilizados na execução ficam no Google Drive. O Google Drive também será o destino operacional dos relatórios gerados.

A pasta `dados_brutos/dado_atual` dentro do repositório deve ser tratada como estrutura local de apoio ou cache de desenvolvimento, não como fonte oficial. Bases de dados e saídas geradas não devem ser versionadas no GitHub.

Bases atuais esperadas:

- `ater_ate_2026_03_gerado_em_20260410151127.xlsx`
- `caf_dap_ativos_ate_2026_03_gerado_em_20260410152650.xlsx`
- `GARANTIA-SAFRA_2023-2024_ate_2026_04.xlsx`
- `mais_alimentos_gaia_202604151554.xlsx`
- `pncf_2026_03_gerado_em_20260410170006.xlsx`
- `PNRA_2026_2026_04_15.xlsx`
- `pronaf_gaia_20260414.xlsx`

## 8. Estrutura Esperada do Relatório

O modelo atual indica a seguinte estrutura principal:

1. Capa/cabeçalho
   - Versão
   - Título: Relatório Estadual de Monitoramento
   - Unidade federativa

2. CAF - Cadastro da Agricultura Familiar
   - Pessoa física
   - Pessoa jurídica
   - Mulheres e homens
   - Fonte e data de referência

3. Blocos CAF adicionais existentes no modelo
   - Quilombolas, indígenas e PCTs com DAP
   - Principais produtos da Agricultura Familiar no Estado
   - Produtos com maior valor total de produção no Estado

4. PRONAF
   - Dados gerais do ano corrente
   - Número de operações/contratos
   - Volume financeiro
   - Recortes por gênero quando disponíveis
   - Série histórica anual

5. Mais Alimentos
   - Quantidade de contratos
   - Valor dos contratos
   - Série histórica anual quando disponível

6. PNCF
   - Número de operações
   - Valor liberado
   - Série histórica anual quando disponível

7. Reforma Agrária / PNRA
   - Famílias assentadas
   - Assentamentos regularizados
   - Assentamentos em reconhecimento
   - Assentamentos tradicionais
   - Assentamentos diferenciados

8. ATER
   - Beneficiários com ATER recebida no ano
   - Beneficiários com ATER iniciada no ano

### Regra editorial: ano/período em títulos

- Para tabelas de **indicadores atuais**, o título deve incluir o **ano de referência** extraído de `dt_referencia` das bases consolidadas (ex.: `2026_03` → `2026`).
- Quando o recorte não for `2026`, o relatório deve indicar explicitamente o período/ano correspondente no título.

## 9. Requisitos Funcionais

### RF01 - Parametrizar UF

O sistema deve permitir informar uma UF de interesse por sigla ou código IBGE da UF.

Exemplos:

- `MG`
- `31`

### RF02 - Gerar relatório estadual

O relatório deve ser exclusivamente estadual. Não haverá, na primeira versão, seção de municípios selecionados.

### RF03 - Gerar relatórios para múltiplas UFs

Na primeira versão, o sistema deve gerar relatório para uma UF por execução. Em evolução posterior, será criado um loop para gerar os 27 relatórios em lote.

### RF04 - Ler bases atuais

O sistema deve localizar e carregar as bases oficiais a partir de uma pasta configurável no Google Drive, reconhecendo cada política pelo nome do arquivo e/ou estrutura da planilha.

Em execução local no VS Code, o notebook deve usar apenas uma cópia local/mock em `dados_brutos/dado_atual`. O acesso ao Google Drive deve ocorrer no Google Colab.

### RF05 - Validar entradas

Antes de gerar o relatório, o sistema deve validar a existência dos arquivos, abas e colunas obrigatórias. Erros devem ser claros e orientar o que precisa ser corrigido.

### RF06 - Calcular totais Brasil e UF

Para cada política, o sistema deve calcular totais nacionais, totais da UF selecionada e percentual da UF em relação ao Brasil, quando aplicável.

### RF07 - Gerar documento Word

O sistema deve gerar um `.docx` em uma pasta de saída configurável no Google Drive. Nesta fase, o caminho definido é `/content/drive/MyDrive/MDA/dado_atual`, usando o template como referência de estrutura e reproduzindo o documento via `python-docx`.

### RF08 - Registrar lacunas

Quando o modelo exigir informação indisponível nas bases atuais, o relatório deve manter a seção com aviso de dado faltante, em vez de omitir silenciosamente ou inventar valores.

### RF09 - Preservar rastreabilidade

O relatório deve indicar fonte e data de referência dos dados utilizados por seção.

### RF10 - Executar no Colab e no VS Code

O notebook principal deve selecionar automaticamente o modo de execução:

- no VS Code, em modo `local`, lendo uma cópia local/mock em `dados_brutos/dado_atual`;
- no Google Colab, em modo `google_drive`, após clonar o repositório, montar o Google Drive e apontar para a pasta de dados.

## 10. Requisitos Não Funcionais

- A primeira versão deve priorizar código em notebook.
- O notebook deve ser bem documentado, com células markdown para títulos, subtítulos, explicações e decisões metodológicas.
- As células de código devem ser organizadas por política pública.
- O código deve executar no Google Colab e no VS Code.
- O projeto não deve depender obrigatoriamente do Colab.
- Caminhos devem ser relativos ao repositório sempre que possível.
- Caminhos para dados e saídas devem ser configuráveis no modo `google_drive`.
- A geração deve ser reprodutível a partir dos mesmos dados.
- Bases de dados e saídas automáticas não devem ser versionadas no GitHub.
- Em uma evolução futura, o código poderá ser organizado em módulos reutilizáveis fora do notebook.
- Documentos markdown auxiliares podem ser usados para tratar uma política por vez durante o desenvolvimento.

## 11. Estratégia de Uso no Google Colab

O Colab será usado como ambiente colaborativo de execução e aprendizado, sem substituir o GitHub como fonte oficial do código.

O Google Drive será usado como repositório operacional de dados e relatórios gerados.

Fluxo previsto:

1. Abrir o notebook no Colab.
2. Clonar ou atualizar o repositório GitHub.
3. Montar o Google Drive quando necessário.
4. Definir o caminho da pasta de dados no Drive.
5. Definir o caminho da pasta de saída no Drive.
6. Executar as células do notebook.
7. Gerar o relatório `.docx` diretamente no Drive.

O notebook deve deixar explícito quais variáveis o usuário precisa configurar, especialmente:

- UF desejada;
- pasta de dados;
- pasta de saída;
- mês/ano de referência quando aplicável.

## 12. Mapeamento Inicial de Dados

### CAF/DAP

Arquivo atual possui colunas para:

- `dt_referencia`
- `cod_ibge`
- `nome_municipio`
- `uf`
- `CAFs PF ATIVO`
- `CAFs PJ ATIVO`
- `QUANTIDADE DE MULHERES EM CAF ATIVO`
- `QUANTIDADE DE HOMENS EM CAF ATIVO`

Lacunas prováveis em relação ao modelo:

- Jovens
- Quilombolas, indígenas e PCTs
- Principais produtos
- Valor total de produção por produto

### PRONAF

Arquivo atual possui dados por ano, município, UF, gênero, quantidade de contratos, valores, operações e ticket médio.

Uso esperado:

- Total Brasil por ano
- Total UF por ano
- Percentual UF/Brasil
- Recorte feminino quando aplicável

### Mais Alimentos

Arquivo atual possui totalizadores e dados municipais com quantidade de contratos e valor total.

Uso esperado:

- Total Brasil
- Total UF
- Percentual UF/Brasil
- Série anual se a base trouxer anos suficientes ou se houver histórico futuro

### PNCF

Arquivo atual possui número de operações, valor liberado e valor médio por operação.

Uso esperado:

- Total Brasil
- Total UF
- Percentual UF/Brasil

### PNRA

Arquivo atual possui famílias por tipo de assentamento/reconhecimento/regularização.

Uso esperado:

- Total Brasil
- Total UF
- Percentual UF/Brasil
- Tabela por categorias do PNRA

### ATER

Arquivo atual possui famílias com ATER iniciada e recebida no ano.

Uso esperado:

- Total Brasil
- Total UF
- Indicadores de ATER iniciada e recebida

## 13. Saídas Esperadas

### Arquivo principal

- `/content/drive/MyDrive/MDA/dado_atual/relatorio_estadual_monitoramento_<UF>_<AAAAMMDDHHMMSS>.docx`

`AAAAMMDDHHMMSS` deve ser sempre gerado a partir da data do sistema no momento da execução.

### Possíveis saídas auxiliares

- Planilha de apoio com cálculos intermediários.
- Log de validação das bases.
- Arquivo markdown com lacunas de dados.

## 14. Proposta de Arquitetura

Estrutura inicial sugerida:

```text
relatorio_dados_damei/
├─ dados_brutos/
│  ├─ .gitkeep
│  └─ dado_atual/
├─ docs/
│  └─ PRD.md
├─ notebooks/
├─ relatorios_gerados/
├─ templates/
│  └─ documento_padrao_v1.docx
├─ .gitignore
├─ README.md
└─ requirements.txt
```

Observação: a pasta `dados_brutos/` preserva a estrutura esperada para testes locais, mas os dados oficiais ficam no Google Drive. A pasta `relatorios_gerados/` no repositório também é apenas estrutura local; a saída operacional deve ser gravada no Google Drive.

Observação: `docs/` é o nome adequado para documentação do projeto. Não é necessário renomear para `agents/`, porque o conteúdo documenta o produto e o processo, não agentes específicos.

## 15. Critérios de Aceite da Primeira Versão

- O notebook de geração roda localmente no VS Code.
- O notebook de geração roda no Google Colab.
- O arquivo `.docx` final é criado no Google Drive em `/content/drive/MyDrive/MDA/dado_atual`.
- O relatório aceita UF por sigla ou código IBGE.
- A primeira versão gera uma UF por execução.
- O relatório contém, no mínimo, seções para CAF, PRONAF, Mais Alimentos, PNCF, PNRA e ATER.
- O relatório é exclusivamente estadual.
- Cada seção informa fonte/data de referência quando disponível.
- Valores de Brasil, UF e percentual são calculados a partir dos arquivos no Google Drive.
- Lacunas em relação ao template são identificadas explicitamente no relatório.
- Nenhuma base `.xlsx`, `.csv`, `.parquet` ou similar é versionada no GitHub.
- O projeto tem `README.md`, `.gitignore` e `requirements.txt`.

## 16. Decisões Já Tomadas

- O relatório deve aceitar qualquer UF.
- A UF pode ser informada por sigla ou código IBGE.
- O relatório será exclusivamente estadual.
- Dados faltantes no template devem aparecer como aviso de dado indisponível.
- Dados brutos não devem ir para o GitHub.
- O Google Drive será o repositório operacional de dados.
- O Google Drive será o destino operacional dos relatórios gerados.
- O template `templates/documento_padrao_v1.docx` deve ser versionado no GitHub.
- O documento final será reproduzido via `python-docx`, usando o `.docx` atual como referência visual e estrutural.
- O código da primeira versão ficará prioritariamente em notebook.
- O projeto deve ser executável no VS Code e no Google Colab.
- O carimbo `AAAAMMDDHHMMSS` será sempre definido pela data do sistema.
- O texto padrão para lacunas será: "Informação não disponível nas bases atuais."

## 17. Questões em Aberto

1. Devemos criar um notebook único com todas as políticas ou um notebook principal e notebooks auxiliares por política?
