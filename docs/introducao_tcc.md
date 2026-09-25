# 1 Introdução

## 1.1 Contextualização e problema de pesquisa

A evasão no ensino superior constitui um fenômeno relevante para a compreensão das trajetórias acadêmicas e para o planejamento das instituições de ensino superior. Seu estudo envolve diferentes perspectivas teóricas e metodológicas, uma vez que a interrupção da trajetória educacional pode estar relacionada a características dos estudantes, aspectos acadêmicos, condições institucionais e ao próprio momento da trajetória em que ocorre a saída. No contexto brasileiro, a literatura apresenta diferentes formas de operacionalizar a evasão e diferentes estratégias para investigar seus fatores associados, o que dificulta comparações diretas entre estudos quando as definições, unidades de análise e métodos empregados não são equivalentes.

A revisão sistemática de Mançano, Monteiro e Carmo (2026), realizada sobre estudos quantitativos brasileiros publicados entre 2010 e 2024, identificou 312 artigos únicos e selecionou 16 estudos para análise detalhada. Os autores destacam a heterogeneidade metodológica do campo e observam que, entre os estudos selecionados voltados à investigação de fatores associados à evasão, análise de sobrevivência e regressões logísticas aparecem como os principais métodos estatísticos empregados. A revisão também evidencia diversidade na escolha das variáveis analisadas e dificuldades de comparação decorrentes das diferenças entre bases de dados, variáveis e modelos empregados (MANÇANO; MONTEIRO; CARMO, 2026).

Essa literatura não significa, entretanto, que abordagens preditivas sejam ausentes no estudo da evasão. Silva, Cabral e Pacheco (2020), por exemplo, desenvolveram modelos de regressão logística para previsão de evasão ou permanência em quatro cursos de graduação a distância de uma instituição pública brasileira, utilizando dados de 2.991 estudantes. O estudo demonstra a possibilidade de aplicação de modelos preditivos ao problema e também destaca que diferentes contextos podem apresentar relações distintas entre as variáveis analisadas e a evasão. Assim, o espaço de investigação não está na simples introdução de modelos preditivos ao tema, mas na comparação sistemática de abordagens sob condições experimentais explicitamente definidas.

Nesse contexto, este trabalho propõe uma abordagem preditiva de caráter agregado para a taxa de evasão no ensino superior brasileiro. Em vez de estimar a probabilidade de evasão de um estudante individual, a unidade de análise adotada é a combinação entre unidade da federação (UF) e período de fluxo. A variável de interesse é a taxa de evasão observada em determinado período, enquanto as variáveis explicativas são construídas a partir de informações disponíveis no período anterior. Essa organização temporal permite investigar a capacidade preditiva dos modelos sem utilizar informações do futuro no treinamento, aspecto particularmente importante em problemas de previsão temporal.

A fonte de dados é composta pelos Indicadores de Fluxo da Educação Superior disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). A página oficial do conjunto informa cobertura dos indicadores de fluxo de 2010 a 2024. Neste trabalho, foram integradas informações de evasão, conclusão, retenção e permanência, organizadas por UF e período de fluxo. A partir da estrutura temporal da base, foram construídas variáveis defasadas de um período, de modo que cada previsão utilize somente informações que estariam disponíveis antes do período a ser previsto (INEP, 2025).

O desenho experimental contempla dois cenários de variáveis preditoras. O Cenário A utiliza quatro indicadores agregados defasados: taxa de evasão, taxa de conclusão, taxa de retenção e taxa de permanência. O Cenário B amplia esse conjunto com informações desagregadas da evasão por sexo, pertencimento ao grupo de pretos, pardos e indígenas (PPI), faixa etária e deficiência, também defasadas em um período. Dessa forma, o trabalho examina não apenas diferenças entre algoritmos, mas também o efeito da ampliação do conjunto informacional utilizado na previsão.

A comparação dos modelos é realizada sob dois protocolos de validação temporal: Expanding Window e Rolling Window. Ambos mantêm os mesmos períodos de teste e alteram somente a composição do histórico utilizado no treinamento. Essa estratégia permite avaliar se a quantidade e a recência do histórico de treinamento influenciam o desempenho preditivo, evitando uma divisão aleatória da base que poderia desconsiderar a ordem temporal dos dados.

Diante desse desenho, a questão central desta pesquisa é:

> **Em que medida diferentes abordagens preditivas apresentam desempenhos distintos na previsão da taxa de evasão no ensino superior brasileiro quando avaliadas por protocolos temporais, e qual é o efeito da incorporação de informações desagregadas da evasão sobre esse desempenho?**

## 1.2 Objetivo geral

Avaliar comparativamente diferentes abordagens preditivas para a taxa de evasão no ensino superior brasileiro, considerando protocolos de validação temporal e diferentes conjuntos de variáveis preditoras.

## 1.3 Objetivos específicos

1. Construir uma base longitudinal por UF e período a partir dos Indicadores de Fluxo da Educação Superior do INEP.
2. Estruturar variáveis preditoras defasadas em um período, preservando a ordem temporal das observações.
3. Comparar os protocolos de validação Expanding Window e Rolling Window em condições de teste equivalentes.
4. Comparar regressão linear, Ridge, Random Forest e Gradient Boosting com um baseline de persistência.
5. Avaliar o efeito da incorporação de informações desagregadas da evasão por sexo, pertencimento ao grupo de pretos, pardos e indígenas (PPI), faixa etária e deficiência.
6. Analisar a heterogeneidade temporal dos erros de previsão e investigar situações em que a ampliação das variáveis altera o desempenho dos modelos.
7. Examinar a relevância preditiva das variáveis do Cenário B por meio de medidas de importância de características.

## 1.4 Hipóteses

**H1 — Protocolo temporal:** a utilização de diferentes estratégias de formação do conjunto de treinamento (Expanding Window e Rolling Window) produz diferenças mensuráveis no desempenho preditivo, ainda que a direção e a magnitude dessas diferenças possam variar entre os modelos.

**H2 — Ampliação informacional:** a incorporação de informações desagregadas da evasão altera o desempenho preditivo em relação ao cenário baseado somente nos indicadores agregados.

**H3 — Heterogeneidade temporal:** o efeito da ampliação do conjunto de variáveis não é necessariamente uniforme entre os períodos de teste, podendo haver mudanças no desempenho conforme o período avaliado.

## 1.5 Justificativa e contribuição

A pesquisa se justifica pela necessidade de avaliar empiricamente estratégias preditivas para a evasão sob condições temporais controladas. A literatura brasileira apresenta estudos que empregam análise de sobrevivência, regressões logísticas e outras abordagens estatísticas, além de aplicações explicitamente preditivas. Entretanto, diferenças entre unidades de análise, fontes de dados, variáveis e protocolos tornam difícil atribuir diferenças de desempenho exclusivamente ao método utilizado. O desenho deste trabalho busca reduzir parte dessa heterogeneidade ao manter a mesma base, os mesmos períodos de teste e métricas comuns na comparação entre modelos.

A contribuição proposta é, portanto, metodológica e empírica: comparar diferentes abordagens preditivas para uma variável agregada de evasão sob protocolos temporais explícitos e verificar se informações desagregadas da evasão acrescentam capacidade preditiva ao conjunto de indicadores agregados. A pesquisa não pretende estabelecer relações causais entre as características analisadas e a evasão, nem substituir estudos individuais sobre as trajetórias dos estudantes. Seu foco está na avaliação do desempenho preditivo de diferentes configurações de modelos em uma base longitudinal por UF e período.

