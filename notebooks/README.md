# Notebooks do Projeto

Esta pasta concentra os notebooks usados no fluxo de extração, transformação e geração dos relatórios estaduais de dados.

## Fluxo Produtivo

Execute os notebooks nesta ordem:

1. `000_preparar_dados_brutos.ipynb`
   - Lê pastas no padrão `dados_gaia_ref_<AAAAMM>`.
   - Seleciona as planilhas brutas mais recentes por política pública.
   - Prepara `dados_brutos/dado_atual/dados_atuais/` para o notebook `010`.
   - Gera inventário rastreável dos arquivos escolhidos.

2. `010_extracao_transformacao.ipynb`
   - Lê os arquivos brutos atuais e históricos.
   - Limpa e transforma os dados por política pública.
   - Salva CSVs intermediários e bases consolidadas.

3. `020_gerar_relatorio_dados.ipynb`
   - Gera o relatório Word de uma UF por execução.
   - Consome apenas os CSVs produzidos pelo notebook `010`.
   - Salva tabelas, gráficos PNG e o documento `.docx`.

4. `030_gerar_relatorios_todas_ufs.ipynb`
   - Orquestra a geração em lote.
   - Executa o notebook `020` uma vez para cada UF desejada.
   - Salva cópias executadas do `020` em `notebooks/executados/<AAAAMM>/`.

## Notebooks Produtivos

```text
000_preparar_dados_brutos.ipynb
010_extracao_transformacao.ipynb
020_gerar_relatorio_dados.ipynb
030_gerar_relatorios_todas_ufs.ipynb
```

Esses são os notebooks que devem ser usados para produção e manutenção do relatório.

## Pastas Auxiliares

```text
notebooks/
  legado/
  executados/
```

- `legado/`: notebooks exploratórios ou versões anteriores. Servem como referência histórica, mas não fazem parte do fluxo produtivo.
- `executados/`: cópias auditáveis geradas pelo notebook `030`. Essas cópias ajudam a verificar quais parâmetros foram usados em cada execução.

## Entradas Esperadas

O notebook `010` espera encontrar dados em:

```text
dados_brutos/
  dado_atual/
    dados_gaia_ref_<AAAAMM>/
    dados_atuais/
  dado_historico/
    PRONAF/
    ATER/
config/
  ufs.csv
```

Em ambiente Google Colab, os caminhos podem ser resolvidos a partir dos atalhos configurados no Google Drive.

## Saídas Geradas

Após executar o `010`:

```text
dados_intermediarios/
  <AAAAMM>/
    politicas/
    historico/
    consolidado/
    logs/
```

Após executar o `020` ou `030`:

```text
relatorios_gerados/
  <AAAAMM>/
    tabelas/<UF>/
    graficos/<UF>/
    logs/
    relatorio_dados_<UF>_<timestamp>.docx
```

## Parâmetros Importantes

No `020`:

- `UF_INTERESSE`: sigla da UF do relatório, por exemplo `MG`, `SC` ou `BA`.
- `ANO_MES_INTERMEDIARIO`: competência da pasta em `dados_intermediarios`. Se ficar `None`, usa a pasta mais recente.

No `030`:

- `UFS_RELATORIO`: lista de UFs a processar. Lista vazia significa todas as UFs disponíveis.
- `LIMITE_UFS`: limite temporário para testes rápidos.
- `PARAR_EM_ERRO`: interrompe o lote no primeiro erro quando `True`.

## Recomendações Para Manutenção

- Evite colocar lógica produtiva em notebooks dentro de `legado/`.
- Antes de alterar o relatório Word, valide se a mudança pertence ao `020` ou à etapa de transformação no `010`.
- Se uma regra muda a base consolidada, implemente no `010`.
- Se uma regra muda apenas aparência, texto, tabela, gráfico ou Word, implemente no `020`.
- Para geração em lote, prefira alterar o `030`, mantendo o `020` linear.
