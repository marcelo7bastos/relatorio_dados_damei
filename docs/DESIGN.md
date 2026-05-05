# DESIGN.md - Relatorio Estadual de Monitoramento DAMEI

## 1. Proposito do documento

Este arquivo define as diretrizes visuais, editoriais e de acessibilidade para a geracao automatizada do `Relatorio Estadual de Monitoramento DAMEI` em formato `.docx`.

O objetivo e orientar humanos e agentes de IA na criacao de um documento profissional, institucional, legivel, rastreavel e compativel com o contexto do Governo Federal brasileiro.

Este documento deve ser usado como referencia para:

- criar ou revisar templates Word (`.docx` ou `.dotx`);
- implementar funcoes de formatacao em `python-docx`;
- revisar a qualidade visual dos relatorios gerados;
- manter consistencia entre relatorios de diferentes UFs;
- evitar escolhas visuais incompativeis com comunicacao publica institucional.

## 2. Bases normativas e metodologicas

### 2.1 Base normativa e visual

As decisoes visuais deste projeto devem observar, nesta ordem:

1. **Secretaria de Comunicacao Social da Presidencia da Republica (Secom/PR)**  
   Referencia para uso da marca do Governo Federal, aplicacao conjunta com ministerios, arquivos de apoio, versoes de marca, limites de aplicacao e consistencia institucional.

2. **Padrao Digital de Governo / Design System GOV.BR**  
   Referencia para principios de experiencia publica: clareza, consistencia, previsibilidade, acessibilidade, reuso, simplicidade e confianca. Mesmo que o produto final seja `.docx`, os principios do Design System devem orientar hierarquia visual, componentes, linguagem de interface e padroes de apresentacao.

3. **Manual de Redacao da Presidencia da Republica**  
   Referencia para comunicacao oficial: clareza, precisao, concisao, formalidade, impessoalidade, padronizacao e respeito ao leitor.

4. **eMAG - Modelo de Acessibilidade em Governo Eletronico**  
   Referencia para acessibilidade, especialmente legibilidade, contraste, estrutura de informacao, textos alternativos, validacao humana e manutencao continua da acessibilidade.

5. **PRD do projeto**  
   Referencia funcional do produto, estrutura editorial, secoes, indicadores, lacunas, fontes, rastreabilidade e fluxo de geracao.

### 2.2 Base metodologica

Este arquivo segue a abordagem de `DESIGN.md` inspirada no repositorio `VoltAgent/awesome-design-md`: um documento em Markdown, legivel por humanos e agentes, que descreve tema visual, paleta, tipografia, componentes, layout, responsividade, padroes e antipadroes.

A diferenca central e que este projeto nao deve copiar esteticas de marcas privadas. A identidade visual deve ser publica, institucional, sobria e alinhada ao Governo Federal brasileiro.

### 2.3 Referencias de consulta

- Uso da Marca do Governo Federal - Secom/PR: https://www.gov.br/secom/pt-br/central-de-conteudo/guias-e-manuais/uso-da-marca-do-governo-federal
- Padrao de Governo Digital - Design System GOV.BR: https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital/sisp/guia-do-gestor/guia-orientativo-de-padroes-e-fluxos-das-tecnologias-de-transformacao-digital/padrao-de-governo-digital-design-system
- GOVBR-DS: https://www.gov.br/ds/
- Manual de Redacao da Presidencia da Republica: https://www.gov.br/pt-br/servicos/consultar-o-manual-de-redacao-da-presidencia-da-republica
- eMAG: https://emag.governoeletronico.gov.br/
- Awesome DESIGN.md: https://github.com/VoltAgent/awesome-design-md

## 3. Personalidade visual

### 3.1 Tom visual

O relatorio deve parecer:

- institucional;
- tecnico;
- claro;
- confiavel;
- republicano;
- acessivel;
- moderno sem parecer promocional;
- visualmente organizado sem parecer publicitario.

O documento deve transmitir que os dados foram tratados com rigor e que a informacao pode ser usada por analistas, gestores e equipes tecnicas.

### 3.2 Palavras-chave de design

- Clareza
- Evidencia
- Sobriedade
- Servico publico
- Rastreabilidade
- Comparabilidade
- Legibilidade
- Hierarquia
- Continuidade
- Consistencia

### 3.3 O que evitar

Evitar qualquer estetica que pareca:

- campanha publicitaria;
- apresentacao comercial;
- dashboard de startup;
- relatorio promocional;
- excesso decorativo;
- estetica de marca privada;
- layout com gradientes chamativos;
- excesso de cards, sombras ou elementos flutuantes;
- cores saturadas sem funcao informativa.

## 4. Principios de design

### 4.1 Conteudo antes de ornamento

O dado e o protagonista. Elementos visuais devem ajudar o leitor a entender, comparar e localizar informacoes, nao competir com os indicadores.

### 4.2 Consistencia entre UFs

Todos os relatorios estaduais devem seguir a mesma estrutura visual. A UF muda o conteudo, nao o sistema de apresentacao.

### 4.3 Hierarquia clara

O leitor deve reconhecer rapidamente:

- titulo do documento;
- UF analisada;
- periodo de referencia;
- secoes por politica publica;
- indicadores principais;
- comparacao UF/Brasil;
- fontes;
- lacunas de dados.

### 4.4 Rastreabilidade visivel

Fonte, referencia temporal e data de geracao da base devem aparecer de forma discreta, mas clara, ao final de cada secao ou em bloco proprio.

### 4.5 Acessibilidade como requisito

O documento deve ser legivel em tela, impresso, exportado para PDF e consumido por tecnologias assistivas sempre que possivel.

### 4.6 Formalidade sem opacidade

A linguagem deve ser formal, mas direta. Frases longas, excesso de siglas e jargoes nao explicados reduzem a qualidade do relatorio.

### 4.7 Reprodutibilidade

Toda decisao visual deve poder ser implementada por template ou codigo. Ajustes manuais pontuais so devem ser aceitos como excecao de validacao, nao como parte do processo regular.

## 5. Paleta de cores

### 5.1 Direcao geral

A paleta deve ser inspirada em comunicacao institucional do Governo Federal e no contexto do MDA, com uso controlado de verde, azul, amarelo e neutros.

As cores devem cumprir papeis semanticos. Nao usar cor apenas como decoracao.

### 5.2 Tokens recomendados

| Token | Hex | Uso principal |
|---|---:|---|
| `gov-blue-900` | `#071D41` | Titulos principais, rodape institucional, linhas de forte hierarquia |
| `gov-blue-700` | `#1351B4` | Links, destaques discretos, divisores, elementos de navegacao interna |
| `gov-green-700` | `#168821` | Destaques relacionados a agricultura, indicadores positivos, acentos do MDA |
| `gov-yellow-500` | `#FFCD07` | Pequenos acentos institucionais, nunca como fundo dominante |
| `gray-900` | `#1B1B1B` | Texto principal |
| `gray-700` | `#555555` | Texto secundario, metadados |
| `gray-500` | `#888888` | Legendas e linhas de apoio |
| `gray-200` | `#E6E6E6` | Bordas de tabelas, divisores leves |
| `gray-100` | `#F7F7F7` | Fundo de celulas de cabecalho, boxes discretos |
| `white` | `#FFFFFF` | Fundo principal |
| `alert-yellow-100` | `#FFF4CC` | Box de lacunas ou informacao indisponivel |
| `alert-yellow-800` | `#5C4100` | Texto em box de lacunas |
| `info-blue-100` | `#EAF2FF` | Box informativo ou fonte/referencia |
| `info-blue-800` | `#17324D` | Texto em box informativo |

### 5.3 Regras de uso

- Usar fundo branco como base do documento.
- Usar `gov-blue-900` para capa, titulo do documento, rodape e separadores estruturais.
- Usar `gov-green-700` como acento secundario relacionado ao tema de agricultura familiar e politicas do MDA.
- Usar amarelo apenas como acento pequeno ou em boxes de alerta/lacuna, com contraste adequado.
- Nao usar gradientes como elemento central.
- Nao usar fundos escuros em paginas inteiras, exceto uma faixa institucional ou capa muito controlada.
- Nao usar cor como unica forma de comunicar significado. Sempre combinar com texto, rotulo ou estrutura.

### 5.4 Contraste

- Texto principal deve ter contraste forte contra o fundo.
- Evitar texto cinza claro em corpo de texto.
- Em tabelas, cabecalhos podem usar fundo azul escuro com texto branco ou fundo cinza claro com texto escuro.
- Boxes amarelos devem usar texto escuro, nao branco.

## 6. Tipografia

### 6.1 Fontes

Preferir fontes amplamente disponiveis no Word e no ambiente Windows/Colab.

Fontes recomendadas:

- **Aptos**: primeira opcao para documentos modernos no Microsoft 365.
- **Arial**: fallback seguro e amplamente disponivel.
- **Calibri**: fallback aceitavel para compatibilidade com documentos Word legados.

Evitar:

- fontes decorativas;
- serifas ornamentais;
- fontes condensadas para corpo de texto;
- fontes muito finas;
- mistura de muitas familias tipograficas.

### 6.2 Escala tipografica para Word

| Estilo | Tamanho | Peso | Cor | Uso |
|---|---:|---|---|---|
| `Title` | 24-28 pt | Bold | `gov-blue-900` | Titulo da capa |
| `Subtitle` | 16-18 pt | Regular/Semibold | `gray-700` | Nome da UF e subtitulo |
| `Heading 1` | 15-17 pt | Bold | `gov-blue-900` | Secao principal por politica |
| `Heading 2` | 12-14 pt | Bold | `gov-blue-700` | Subsecao |
| `Heading 3` | 11-12 pt | Semibold | `gray-900` | Subtitulo local |
| `Body Text` | 10.5-11 pt | Regular | `gray-900` | Corpo do texto |
| `Caption` | 8.5-9.5 pt | Regular | `gray-700` | Legendas, fontes, observacoes |
| `Table Header` | 9.5-10 pt | Bold | conforme fundo | Cabecalho de tabela |
| `Table Body` | 9-10 pt | Regular | `gray-900` | Celulas de tabela |
| `Footnote` | 8-8.5 pt | Regular | `gray-700` | Rodape e notas auxiliares |

### 6.3 Regras tipograficas

- Usar alinhamento a esquerda para textos corridos.
- Evitar texto justificado se houver risco de grandes espacos entre palavras.
- Usar negrito para rotulos e destaques pontuais, nao para paragrafos inteiros.
- Evitar sublinhado, exceto em links se necessario.
- Evitar CAIXA ALTA em blocos longos.
- Manter entrelinha de 1,05 a 1,15 no corpo do texto.
- Usar espaco antes/depois de paragrafo, nao linhas vazias repetidas.

## 7. Estrutura do documento

### 7.1 Ordem recomendada

1. Capa
2. Informacoes de geracao
3. Sumario executivo
4. Secoes de politicas publicas
5. Fontes e referencias por secao
6. Lacunas e informacoes indisponiveis
7. Notas metodologicas, se aplicavel

### 7.2 Capa

A capa deve conter:

- marca institucional correta, quando disponivel e autorizada;
- nome do ministerio/unidade;
- titulo: `Relatorio Estadual de Monitoramento`;
- subtitulo com a UF;
- mes/ano de referencia;
- data de geracao;
- versao do relatorio;
- indicacao de documento preliminar, quando aplicavel.

Diretriz visual:

- fundo predominantemente branco;
- faixa superior ou inferior em azul institucional;
- uso discreto de verde como acento;
- sem imagem decorativa de banco de imagens;
- sem elementos publicitarios;
- sem excesso de logos.

### 7.3 Cabecalho

Para paginas internas:

- lado esquerdo: titulo curto do relatorio;
- lado direito: UF ou mes/ano;
- linha divisoria fina em `gray-200` ou `gov-blue-700`;
- nao repetir blocos grandes de marca em todas as paginas.

### 7.4 Rodape

O rodape deve conter:

- numeracao de pagina;
- identificacao curta do projeto ou ministerio;
- opcionalmente versao/data de geracao;
- texto em 8-8.5 pt, cor `gray-700`.

### 7.5 Sumario executivo

O sumario executivo deve ser curto e orientado a decisao.

Formato recomendado:

- titulo `Sumario Executivo`;
- 2 a 4 frases com indicadores principais;
- opcionalmente um quadro de destaques com ate 4 indicadores-chave;
- evitar tabelas extensas no sumario.

Indicadores-chave possiveis:

- CAFs Pessoa Fisica ativos;
- valor total dos contratos do PRONAF;
- familias assentadas ou indicador principal de PNRA;
- beneficiarios ATER.

### 7.6 Secoes por politica publica

Cada secao deve conter:

1. Titulo numerado da politica.
2. Breve descricao.
3. Tabela de indicadores.
4. Avaliacao de ranking, se aplicavel.
5. Fonte e referencia.
6. Lacunas em relacao ao documento padrao.

Padrao de titulo:

```text
1. CAF - Cadastro da Agricultura Familiar
2. PRONAF
3. Mais Alimentos
4. PNCF
5. PNRA - Reforma Agraria
6. ATER
```

## 8. Componentes visuais

### 8.1 Tabela de indicadores

As tabelas sao o componente mais importante do relatorio.

Colunas padrao:

| Coluna | Alinhamento | Largura relativa | Observacao |
|---|---|---:|---|
| Indicador | esquerda | 42% | Texto descritivo |
| Brasil | direita | 18% | Numero nacional |
| UF | direita | 18% | Numero estadual |
| Percentual em relacao ao nacional | direita | 22% | Percentual |

Tratamento visual:

- bordas finas em `gray-200`;
- cabecalho com fundo `gov-blue-900` e texto branco, ou fundo `gray-100` e texto `gov-blue-900`;
- linhas alternadas com fundo branco e `gray-100` muito leve;
- numeros alinhados a direita;
- indicador alinhado a esquerda;
- padding interno suficiente;
- evitar celulas coladas nas bordas;
- repetir cabecalho se tabela quebrar entre paginas;
- evitar que uma linha de tabela seja cortada de modo ruim no fim da pagina, quando tecnicamente possivel.

### 8.2 Box de fonte e referencia

Usar box discreto ao final de cada secao.

Conteudo:

```text
Fonte: [nome da base]. Referencia: [data]. Geracao da base: [data].
```

Tratamento visual:

- fundo `info-blue-100`;
- borda esquerda em `gov-blue-700`;
- texto em `info-blue-800`;
- fonte 8.5-9.5 pt;
- espacamento antes de 6 pt e depois de 6 pt.

### 8.3 Box de lacunas

Usar quando houver informacao indisponivel em relacao ao modelo padrao.

Conteudo:

```text
Lacunas em relacao ao documento padrao:
- [lacuna]. Informacao indisponivel nas bases atuais.
```

Tratamento visual:

- fundo `alert-yellow-100`;
- borda esquerda em `gov-yellow-500`;
- texto em `alert-yellow-800`;
- fonte 9-10 pt;
- evitar tom alarmista;
- deixar claro que e uma lacuna de base, nao erro do relatorio.

### 8.4 Destaques numericos

Pode ser usado no sumario executivo ou inicio de secao, com moderacao.

Formato:

- rotulo curto;
- numero em destaque;
- complemento pequeno;
- sem sombras pesadas;
- fundo claro;
- borda fina ou linha superior em cor institucional.

Exemplo:

```text
CAFs PF ativos
123.456
4,2% do Brasil
```

Regras:

- usar no maximo 4 destaques por pagina;
- nao substituir tabelas de rastreabilidade;
- nao usar como card publicitario.

### 8.5 Ranking

O texto de ranking deve ser apresentado como bloco interpretativo discreto.

Tratamento visual:

- paragrafo normal ou box `info-blue-100`;
- destacar apenas posicao e universo, por exemplo `3a posicao entre 27 UFs`;
- nao usar trofeus, medalhas ou linguagem competitiva excessiva.

### 8.6 Notas metodologicas

Notas devem ser usadas para explicar:

- filtros aplicados;
- definicoes de indicadores;
- tratamento de ausencia de dados;
- referencia temporal;
- diferencas entre bases.

Tratamento visual:

- fonte menor que corpo;
- cor `gray-700`;
- titulo curto `Nota metodologica`;
- sem excesso de caixas.

## 9. Layout e espacamento

### 9.1 Pagina

Configuracao recomendada:

- tamanho: A4;
- orientacao: retrato;
- margens: 2,0 cm a 2,5 cm;
- margem interna suficiente para encadernacao digital/impressa;
- cabecalho e rodape discretos.

### 9.2 Espacamento vertical

Regras recomendadas:

- antes de `Heading 1`: 18-24 pt;
- depois de `Heading 1`: 6-10 pt;
- antes de `Heading 2`: 12-16 pt;
- depois de `Heading 2`: 4-8 pt;
- corpo de texto: 3-6 pt depois;
- antes de tabela: 6 pt;
- depois de tabela: 8-12 pt;
- entre box de fonte e proxima secao: 12-18 pt.

### 9.3 Quebras de pagina

- A capa deve terminar com quebra de pagina.
- O sumario executivo deve comecar em pagina propria se a capa for completa.
- Evitar iniciar uma secao no fim da pagina com apenas o titulo.
- Manter titulo e primeiro paragrafo juntos.
- Manter legenda/fonte proxima ao componente que descreve.
- Aceitar quebra de tabela entre paginas apenas quando a tabela for longa e tiver cabecalho repetido.

### 9.4 Densidade

O relatorio deve ser denso o suficiente para uso tecnico, mas nao deve parecer uma planilha colada no Word.

Evitar:

- muitas tabelas consecutivas sem texto;
- paragrafos longos antes de indicadores;
- excesso de negrito;
- excesso de bordas;
- espacamento apertado em tabelas.

## 10. Linguagem editorial

### 10.1 Principios

Seguir os principios do Manual de Redacao da Presidencia da Republica:

- clareza;
- precisao;
- concisao;
- formalidade;
- impessoalidade;
- padronizacao;
- coerencia terminologica.

### 10.2 Tom

O texto deve ser:

- tecnico;
- neutro;
- objetivo;
- transparente sobre limitacoes;
- compreensivel por gestores e analistas.

### 10.3 Padroes de redacao

Preferir:

```text
O estado de Minas Gerais possui 123.456 CAFs Pessoa Fisica ativos, equivalentes a 4,2% do total nacional.
```

Evitar:

```text
Minas Gerais se destaca fortemente no cenario nacional, com numeros expressivos e grande protagonismo.
```

### 10.4 Siglas

- Expandir siglas na primeira ocorrencia relevante.
- Manter siglas consolidadas quando forem nomes oficiais de politicas.
- Nao alternar nomes para a mesma politica ao longo do documento.

Exemplo:

```text
CAF - Cadastro da Agricultura Familiar
PRONAF - Programa Nacional de Fortalecimento da Agricultura Familiar
PNCF - Programa Nacional de Credito Fundiario
PNRA - Programa Nacional de Reforma Agraria
ATER - Assistencia Tecnica e Extensao Rural
```

### 10.5 Informacao indisponivel

Usar formula padronizada:

```text
Informacao indisponivel nas bases atuais.
```

Evitar:

- `N/A`;
- `sem dados`, quando puder ser confundido com zero;
- celulas vazias;
- textos informais.

## 11. Acessibilidade

### 11.1 Requisitos gerais

- Usar hierarquia real de estilos do Word (`Title`, `Heading 1`, `Heading 2`, corpo), nao apenas texto visualmente maior.
- Garantir contraste adequado entre texto e fundo.
- Evitar depender somente de cor para indicar status.
- Usar texto alternativo em imagens, logos, graficos e mapas.
- Manter tabelas simples, com cabecalhos claros.
- Evitar tabelas usadas apenas para layout.
- Evitar textos em imagens.
- Evitar fontes menores que 8 pt.
- Preferir linguagem clara e frases curtas.

### 11.2 Tabelas acessiveis

- Toda tabela deve ter linha de cabecalho.
- Cabecalhos devem ser descritivos.
- Numeros devem ter unidades ou formatos claros.
- Evitar mesclar celulas desnecessariamente.
- Evitar tabelas muito largas.
- Repetir cabecalho em quebras de pagina.

### 11.3 Imagens e marcas

- Logos devem ter texto alternativo descritivo.
- Elementos decorativos sem informacao podem ser marcados como decorativos quando a ferramenta permitir.
- Nao usar imagem como unico suporte de informacao essencial.

### 11.4 Validacao visual e humana

Antes de considerar um `.docx` pronto:

- renderizar o documento em imagens ou PDF;
- revisar pagina a pagina;
- verificar quebras, sobreposicoes, tabelas e rodapes;
- revisar contraste e tamanho de fonte;
- verificar se informacoes de fonte/referencia estao presentes;
- abrir o documento no Word ou visualizador equivalente quando possivel.

## 12. Regras para implementacao em python-docx

### 12.1 Estrategia recomendada

Preferir um template Word profissional:

```python
doc = Document(TEMPLATE_PROFISSIONAL_PATH)
```

Em seguida, preencher conteudo com funcoes especializadas:

```python
configurar_metadados_documento(doc, uf, periodo)
adicionar_capa_profissional(doc, contexto)
adicionar_sumario_executivo(doc, indicadores)
adicionar_secao_politica(doc, politica, indicadores)
adicionar_tabela_indicadores(doc, df_indicadores, uf_label)
adicionar_fonte_referencia(doc, politica)
adicionar_lacunas(doc, politica["lacunas"])
```

### 12.2 Separacao de responsabilidades

Separar:

- calculo dos indicadores;
- redacao dos textos;
- formatacao visual;
- validacao do documento;
- exportacao/renderizacao.

Evitar que funcoes de calculo manipulem estilos Word.

### 12.3 Estilos nomeados

Criar estilos no template ou por codigo:

- `DAMEI Title`
- `DAMEI Subtitle`
- `DAMEI Heading 1`
- `DAMEI Heading 2`
- `DAMEI Body`
- `DAMEI Caption`
- `DAMEI Table`
- `DAMEI Table Header`
- `DAMEI Source Box`
- `DAMEI Gap Box`
- `DAMEI KPI Label`
- `DAMEI KPI Value`

### 12.4 Tabelas

Ao criar tabelas:

- definir largura de colunas;
- alinhar numeros a direita;
- alinhar textos a esquerda;
- aplicar padding de celula;
- aplicar cabecalho;
- aplicar repeticao de cabecalho, se possivel;
- evitar estilo `Table Grid` puro como resultado final.

### 12.5 Metadados

O documento deve conter, quando possivel:

- titulo;
- assunto;
- autor institucional;
- palavras-chave;
- data de criacao;
- versao;
- UF;
- periodo de referencia.

## 13. Checklist de qualidade visual

Antes de entregar uma nova versao do relatorio, verificar:

- [ ] A capa identifica corretamente relatorio, UF, periodo, versao e data de geracao.
- [ ] O documento usa estilos de titulo reais do Word.
- [ ] As secoes seguem a ordem definida no PRD.
- [ ] As tabelas estao legiveis e com numeros alinhados.
- [ ] Nao ha tabelas cortadas de forma ruim.
- [ ] Nao ha texto sobreposto.
- [ ] Nao ha grandes espacos vazios causados por quebras ruins.
- [ ] Fonte e referencia aparecem em todas as secoes.
- [ ] Lacunas aparecem de forma clara e padronizada.
- [ ] O documento nao depende de cor para comunicar informacao essencial.
- [ ] O contraste esta adequado.
- [ ] Logos e imagens possuem texto alternativo quando aplicavel.
- [ ] Rodape e numeracao de paginas estao consistentes.
- [ ] O arquivo abre corretamente no Word.
- [ ] O documento renderizado foi revisado pagina a pagina.

## 14. Padroes e antipadroes

### 14.1 Fazer

- Usar branco, azul institucional, verde discreto e neutros.
- Priorizar tabelas claras e bem espacadas.
- Usar boxes apenas para informacao relevante.
- Manter visual limpo e institucional.
- Preservar rastreabilidade dos dados.
- Usar linguagem objetiva e impessoal.
- Aplicar o mesmo template para todas as UFs.
- Revisar o documento renderizado antes da entrega.

### 14.2 Nao fazer

- Nao criar layout com aparencia de campanha.
- Nao usar gradientes chamativos.
- Nao usar sombras pesadas.
- Nao transformar cada dado em card.
- Nao usar cores sem significado.
- Nao deixar celulas vazias sem explicacao.
- Nao usar `N/A` como texto final.
- Nao usar tabelas sem cabecalho.
- Nao depender de ajustes manuais apos a geracao.
- Nao copiar identidade visual de empresas privadas.

## 15. Guia rapido para agentes de IA

Quando um agente for criar, alterar ou revisar o `.docx`, ele deve seguir esta ordem:

1. Ler `docs/PRD.md`.
2. Ler este `docs/DESIGN.md`.
3. Preservar a estrutura funcional do relatorio.
4. Aplicar identidade visual institucional brasileira.
5. Usar template profissional sempre que possivel.
6. Melhorar capa, hierarquia, tabelas, boxes, cabecalho e rodape.
7. Renderizar e revisar visualmente o documento antes de concluir.
8. Nao inventar dados ausentes.
9. Nao omitir lacunas.
10. Nao trocar formalidade institucional por linguagem promocional.

Prompt de referencia:

```text
Use docs/DESIGN.md como sistema visual do Relatorio Estadual de Monitoramento DAMEI.
O documento deve parecer institucional, tecnico, claro, acessivel e alinhado ao Governo Federal brasileiro.
Preserve a estrutura e os dados do PRD. Melhore apenas apresentacao, hierarquia, tabelas, capa, cabecalho, rodape, boxes de fonte e lacunas.
Nao use estetica de marca privada, promocional ou decorativa.
```

## 16. Criterio de pronto

Uma versao visual do relatorio so deve ser considerada pronta quando:

- o `.docx` for gerado automaticamente;
- o conteudo estiver completo;
- o template for aplicado sem ajuste manual obrigatorio;
- o documento renderizado nao apresentar problemas visuais;
- a identidade estiver compativel com Secom/GOV.BR;
- a linguagem estiver compativel com redacao oficial;
- os requisitos de acessibilidade forem verificados;
- o mesmo processo puder gerar os 27 relatorios estaduais.
