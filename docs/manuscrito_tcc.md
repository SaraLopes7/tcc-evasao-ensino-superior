# Avaliação comparativa de abordagens preditivas para a taxa de evasão no ensino superior brasileiro

# Resumo

A evasão no ensino superior brasileiro é um fenômeno de natureza temporal e multifatorial, investigado na literatura por diferentes abordagens estatísticas. Este trabalho avalia comparativamente diferentes abordagens preditivas para a taxa de evasão no ensino superior brasileiro, considerando protocolos de validação temporal e diferentes conjuntos de variáveis preditoras. A unidade de análise é a combinação entre unidade da federação e período de fluxo, e a tarefa consiste em prever a taxa de evasão de um período a partir de informações disponíveis no período anterior. Foram utilizados os Indicadores de Fluxo da Educação Superior do INEP e construídos dois cenários de variáveis. O Cenário A utiliza taxas agregadas de evasão, conclusão, retenção e permanência, enquanto o Cenário B acrescenta taxas de evasão desagregadas por sexo, pertencimento a PPI, faixa etária e deficiência. Foram comparadas uma estratégia de persistência, Regressão Linear, Regressão Ridge, Random Forest e Gradient Boosting sob os protocolos Expanding Window e Rolling Window, preservando a ordem temporal dos dados. Os resultados mostram que o desempenho varia conforme o modelo, o protocolo e o conjunto de informações utilizado. No Cenário A, os métodos lineares apresentaram menores erros médios agregados que os modelos baseados em árvores. A inclusão das informações desagregadas alterou o desempenho de todos os métodos, mas sem produzir efeito uniforme. No Gradient Boosting, observaram-se reduções de erro nos dois protocolos, com efeito especialmente expressivo no período de 2022–2023. A análise temporal evidenciou, portanto, que a utilidade preditiva das informações desagregadas depende do período avaliado. Os resultados reforçam a importância de protocolos temporais explícitos e de comparações controladas na avaliação de modelos preditivos aplicados à evasão no ensino superior.

**Palavras-chave:** evasão no ensino superior; previsão; validação temporal; aprendizado de máquina; análise comparativa.

# Abstract

Dropout in Brazilian higher education is a temporal and multifactorial phenomenon that has been investigated through different statistical approaches. This study comparatively evaluates predictive approaches for higher education dropout rates in Brazil, considering temporal validation protocols and different sets of predictor variables. The unit of analysis is the combination of federative unit and academic-flow period, and the task consists of predicting the dropout rate for a given period using information available in the preceding period. Data from INEP's Higher Education Flow Indicators were used to construct two predictor scenarios. Scenario A uses aggregate dropout, completion, retention, and permanence rates, whereas Scenario B adds disaggregated dropout rates by sex, PPI status, age group, and disability. A persistence strategy, Linear Regression, Ridge Regression, Random Forest, and Gradient Boosting were compared under Expanding Window and Rolling Window protocols while preserving the temporal order of observations. The results show that predictive performance varies according to the model, validation protocol, and information set. In Scenario A, linear methods presented lower aggregate errors than tree-based models. The inclusion of disaggregated information changed the performance of all methods, but the effect was not uniform. Gradient Boosting showed error reductions under both protocols, with a particularly strong effect in the 2022–2023 test period. The temporal analysis therefore indicates that the predictive usefulness of disaggregated information depends on the period under evaluation. These findings reinforce the importance of explicit temporal validation protocols and controlled comparisons when evaluating predictive models applied to higher education dropout.

**Keywords:** higher education dropout; prediction; temporal validation; machine learning; comparative analysis.

---

## 1 Introdução

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

## 2 Fundamentação teórica

## 2.1 Evasão no ensino superior como fenômeno de trajetória

A evasão no ensino superior não corresponde a um fenômeno conceitualmente único. Diferentes pesquisas podem utilizar definições distintas de evasão conforme a unidade de análise, o horizonte temporal e o tipo de trajetória considerada. Essa diversidade é importante porque uma taxa agregada de evasão e a saída individual de um estudante de determinado curso representam fenômenos relacionados, mas não equivalentes.

No campo teórico da evasão, Tinto (1975) propôs um modelo que procura explicar o processo pelo qual diferentes formas de interação entre o indivíduo e a instituição podem contribuir para a permanência ou para a saída do estudante. O modelo destaca a trajetória como processo, em vez de tratar a evasão apenas como uma característica fixa do indivíduo. Essa perspectiva contribuiu para que estudos posteriores incorporassem dimensões acadêmicas, sociais e institucionais ao problema.

No contexto brasileiro, a questão da definição e da operacionalização da evasão também é central. Vitelli e Fritsch (2016) discutem justamente a necessidade de explicitar qual indicador de evasão está sendo utilizado, uma vez que diferentes formas de operacionalização podem representar dimensões distintas do fenômeno. Mançano, Monteiro e Carmo (2026) destacam a pluralidade conceitual e metodológica existente na produção nacional e observam que diferenças na maneira de calcular e operacionalizar a evasão podem limitar a comparabilidade entre pesquisas. Por essa razão, o presente trabalho explicita desde o início que não estima o risco individual de um estudante abandonar determinado curso. A variável de interesse é a **taxa de evasão agregada por UF e período de fluxo**.

Essa distinção delimita o alcance das interpretações. Os resultados obtidos neste estudo descrevem diferenças de desempenho na previsão de uma medida agregada e não permitem concluir que determinada característica individual aumente ou reduza causalmente a probabilidade de um estudante abandonar o ensino superior.

## 2.2 Evidências empíricas sobre fatores associados à evasão

A literatura empírica brasileira apresenta diferentes conjuntos de variáveis associados à evasão, dependendo da instituição, da população analisada e do método utilizado. Na revisão sistemática de Mançano, Monteiro e Carmo (2026), sexo, idade, raça/cor, proxies de renda, educação parental, origem escolar, desempenho acadêmico e turno aparecem entre as variáveis analisadas com maior frequência no conjunto de estudos selecionados. Os autores também ressaltam que a disponibilidade das informações administrativas condiciona quais variáveis podem ser incorporadas aos modelos.

A idade se destaca na revisão por apresentar associação estatisticamente significativa nos estudos que a analisaram, enquanto sexo também aparece de maneira recorrente. Entretanto, esses resultados devem ser entendidos no contexto dos modelos e populações de cada estudo, não como relações universais aplicáveis a qualquer instituição ou população.

Estudos longitudinais reforçam a importância de considerar a trajetória temporal. Saccaro, França e Jacinto (2019), Rosa, Milani e Santos (2021) e Klitzke e Carvalhaes (2023) empregaram análise de sobrevivência em diferentes contextos institucionais brasileiros, enquanto Nierotka, Salata e Klitzke (2023) analisaram fatores associados à evasão em perspectiva longitudinal. Nierotka, Bonamino e Carrasqueira (2023), acompanhando uma coorte de ingressantes de uma instituição pública, também investigaram a relação entre características dos estudantes e da instituição e os desfechos de evasão e conclusão.

Esses trabalhos são relevantes para a presente pesquisa principalmente por evidenciarem que a evasão possui dimensão temporal e que diferentes conjuntos de variáveis podem apresentar comportamentos distintos em diferentes contextos. O presente estudo, contudo, não reproduz esses desenhos de sobrevivência em nível individual. A proposta é utilizar informações agregadas de períodos anteriores para prever a taxa agregada de evasão do período seguinte.

## 2.3 Abordagens estatísticas e preditivas na literatura

A revisão sistemática de Mançano, Monteiro e Carmo (2026) identificou análise de sobrevivência e regressões logísticas como os dois principais métodos estatísticos utilizados nos estudos selecionados para investigar fatores associados à evasão. A análise de sobrevivência permite modelar o tempo até a ocorrência do evento e lidar com situações em que a trajetória observacional termina antes da ocorrência da evasão. A regressão logística, por sua vez, é utilizada em estudos que buscam modelar resultados binários e estimar associações entre variáveis explicativas e a ocorrência da evasão.

A presença desses métodos na literatura não significa que o campo esteja restrito à descrição ou à explicação estatística do fenômeno. Silva, Cabral e Pacheco (2020), por exemplo, utilizaram regressão logística binária para construir modelos preditivos de evasão ou permanência em estudantes de quatro cursos de graduação a distância de uma instituição pública brasileira. O estudo encontrou diferenças nas variáveis relevantes entre cursos e destacou que a mesma variável pode produzir efeitos distintos em realidades diferentes.

Essa evidência é particularmente relevante para a formulação do presente estudo: o desempenho de um modelo preditivo não deve ser considerado independente do conjunto de dados, da unidade de análise e do período em que a previsão é realizada. Assim, a comparação proposta aqui mantém constantes a fonte de dados, os períodos de teste, a variável-alvo e as métricas, permitindo observar como diferentes abordagens se comportam sob condições experimentais comuns.

## 2.4 Dados agregados e informações desagregadas da evasão

O uso de dados administrativos possibilita construir análises longitudinais em escala ampla, mas também impõe limitações relacionadas à disponibilidade e ao nível de agregação das variáveis. Mançano, Monteiro e Carmo (2026) observam que a escolha das variáveis nos estudos sobre evasão é frequentemente condicionada pelos dados administrativos disponíveis.

Neste trabalho, essa questão é explorada mediante dois conjuntos de variáveis. O Cenário A reúne quatro indicadores agregados de trajetória: evasão, conclusão, retenção e permanência, todos utilizados com defasagem de um período. O Cenário B preserva essas variáveis e acrescenta taxas de evasão desagregadas por sexo, pertencimento ao grupo de pretos, pardos e indígenas (PPI), faixa etária e deficiência.

É importante diferenciar **informação desagregada da evasão** de **composição demográfica da população estudantil**. As variáveis do Cenário B não representam a proporção de estudantes de cada grupo na população universitária. Elas representam taxas de evasão calculadas para grupos definidos pela fonte. Portanto, a análise investiga se a informação histórica sobre as taxas de evasão desses grupos acrescenta capacidade preditiva à informação agregada, e não se a composição demográfica das UFs explica causalmente a evasão.

Essa distinção também limita a interpretação das medidas de importância. Uma variável apresentar maior importância preditiva significa que ela contribuiu mais para o desempenho do modelo dentro da configuração experimental utilizada. Isso não implica que mudanças nessa variável produziriam causalmente mudanças na taxa de evasão.

## 2.5 Previsão temporal e risco de vazamento de dados

Problemas de previsão temporal exigem que a avaliação preserve a ordem cronológica das observações. Quando informações do período futuro são utilizadas durante o treinamento ou na preparação das variáveis, o modelo pode apresentar desempenho artificialmente elevado porque recebe informações que não estariam disponíveis no momento real da previsão. Esse problema é conhecido como *data leakage* (vazamento de dados).

A estrutura do presente trabalho foi construída para evitar esse tipo de vazamento. Para cada observação do período-alvo \(t\), as variáveis utilizadas como preditoras correspondem ao período anterior \(t-1\). Além disso, os períodos de teste são mantidos posteriores aos períodos utilizados para treinamento. Dessa forma, a comparação entre os modelos procura reproduzir uma situação de previsão em que o passado é utilizado para estimar um período futuro.

A escolha de validação temporal também está relacionada à pergunta de pesquisa. Como o trabalho pretende comparar Expanding Window e Rolling Window, uma divisão aleatória entre treinamento e teste seria inadequada para essa finalidade, pois destruiria a estrutura temporal que os dois protocolos pretendem representar.

## 2.6 Expanding Window e Rolling Window

Na validação **Expanding Window**, o conjunto de treinamento aumenta progressivamente à medida que novos períodos históricos passam a estar disponíveis. No experimento, o primeiro treinamento utiliza os períodos de 2017–2018 a 2020–2021 para testar 2021–2022; posteriormente, o período de teste é avançado e o histórico utilizado no treinamento é ampliado.

Na validação **Rolling Window**, o tamanho da janela de treinamento permanece constante. Quando o período de teste avança, o período histórico mais antigo é retirado e um período mais recente é incorporado. Neste estudo, ambas as estratégias utilizam os mesmos três períodos de teste: 2021–2022, 2022–2023 e 2023–2024. A diferença entre elas está, portanto, na quantidade e na recência do histórico de treinamento.

Essa comparação permite avaliar uma questão prática: para a previsão agregada da evasão, utilizar toda a história disponível ou privilegiar uma janela fixa de períodos recentes produz desempenhos diferentes? A hipótese H1 foi formulada exatamente para testar essa diferença.

## 2.7 Modelos avaliados

O experimento compara quatro modelos de regressão supervisionada e um baseline de persistência. A **persistência** utiliza a taxa de evasão do período anterior como previsão para o período atual. Trata-se de uma referência simples para verificar se os modelos conseguem extrair informação adicional além da continuidade temporal da própria série.

A **Regressão Linear** estabelece uma relação linear entre as variáveis preditoras e a taxa de evasão-alvo. O **Ridge** adiciona regularização L2 aos coeficientes da regressão, com padronização das variáveis antes do ajuste. O **Random Forest** utiliza um conjunto de árvores de decisão treinadas sobre diferentes amostras e subconjuntos de variáveis, permitindo representar relações não lineares e interações. O **Gradient Boosting** constrói sequencialmente árvores de decisão pequenas, buscando reduzir os erros residuais das etapas anteriores.

A comparação entre modelos lineares e métodos baseados em árvores é coerente com o objetivo exploratório do trabalho: verificar se a ampliação do conjunto de variáveis e a presença de possíveis relações não lineares produzem diferenças de desempenho. A análise, entretanto, não pressupõe previamente que modelos mais complexos devam superar modelos lineares.

## 2.8 Avaliação do desempenho preditivo

O desempenho dos modelos é analisado por três métricas: erro absoluto médio (MAE), raiz do erro quadrático médio (RMSE) e coeficiente de determinação \(R^2\).

O **MAE** representa a magnitude média dos erros absolutos e mantém a unidade da variável-alvo. Valores menores indicam menor erro absoluto médio.

O **RMSE** também é expresso na unidade da variável-alvo, mas atribui maior peso aos erros de maior magnitude por meio da etapa de quadratização. Essa característica é relevante para a análise porque alguns períodos e UFs apresentam erros consideravelmente maiores que os demais.

O **R²** descreve a proporção da variabilidade da variável-alvo explicada pelas previsões em relação ao benchmark de uma previsão baseada na média do conjunto de teste. Valores podem ser negativos quando o modelo apresenta desempenho inferior a essa referência no conjunto avaliado.

Além dessas métricas agregadas, o estudo utiliza análise de erro por período e por UF, permitindo verificar se os resultados globais escondem comportamentos distintos entre os folds.

## 2.9 Interpretabilidade e análise de importância

Para o Cenário B, a análise de interpretabilidade concentra-se no Gradient Boosting. São utilizadas tanto as importâncias nativas do modelo quanto a importância por permutação.

A importância por permutação avalia a alteração do desempenho quando os valores de uma determinada variável são embaralhados no conjunto de teste, preservando as demais variáveis. Quanto maior a deterioração do desempenho após a permutação, maior a contribuição preditiva da variável dentro daquela avaliação.

Essa medida deve ser interpretada com cautela. Em particular, importância preditiva não equivale a efeito causal. Variáveis correlacionadas podem compartilhar informação, e a importância de uma variável pode mudar entre períodos. Além disso, os folds possuem somente 27 observações de teste, o que aumenta a sensibilidade das medidas a variações específicas de cada período. Por esse motivo, neste trabalho a interpretabilidade é utilizada para identificar padrões de relevância preditiva e estabilidade, e não para estabelecer relações causais.

## 2.10 Síntese do posicionamento teórico

A fundamentação apresentada situa o trabalho na interseção entre três dimensões: estudos sobre evasão no ensino superior, modelagem preditiva e validação temporal. A literatura demonstra que a evasão é um fenômeno complexo e dependente do contexto, enquanto as abordagens empíricas apresentam diversidade de unidades de análise, variáveis e métodos.

A presente pesquisa se diferencia por adotar explicitamente uma unidade agregada UF × período, construir preditores defasados, comparar duas formas de validação temporal e testar dois conjuntos de informação preditora sob as mesmas condições. O objetivo não é substituir estudos de trajetória individual ou análises explicativas da evasão, mas complementar esse campo com uma avaliação comparativa de desempenho preditivo em dados longitudinais agregados.

## 3 Metodologia

## 3.1 Delineamento da pesquisa

Este estudo adota abordagem **quantitativa, comparativa e preditiva**, estruturada como uma validação de solução. O propósito é avaliar diferentes abordagens para a previsão da taxa de evasão no ensino superior brasileiro, considerando explicitamente a dimensão temporal dos dados.

A unidade de análise é a combinação entre **unidade federativa (UF) e período de fluxo**. Dessa forma, o estudo não estima a probabilidade individual de um estudante evadir. O problema investigado é a previsão da **taxa agregada de evasão de uma UF em um período futuro**, utilizando informações disponíveis no período anterior.

O desenho experimental foi construído para responder a duas dimensões principais: (i) o efeito do protocolo de validação temporal sobre o desempenho preditivo; e (ii) o efeito da ampliação do conjunto de variáveis, comparando informações agregadas com informações agregadas acrescidas de taxas de evasão desagregadas.

A literatura brasileira reúne estudos baseados em modelos preditivos, regressão logística e análise de sobrevivência. Por isso, a contribuição deste trabalho é apresentada como uma **avaliação comparativa sob protocolos temporais comuns**, e não como a introdução inédita de modelos preditivos na literatura sobre evasão.

## 3.2 Fonte dos dados e preparação da base

Foram utilizados os **Indicadores de Fluxo da Educação Superior disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)**. A série disponibilizada pela fonte cobre o período de 2010 a 2024.

Foram integradas quatro dimensões dos indicadores de fluxo:

- taxa de evasão;
- taxa de conclusão;
- taxa de retenção;
- taxa de permanência.

Os dados foram padronizados para uma estrutura longitudinal por **UF × período**, contemplando as 27 unidades federativas brasileiras. A variável temporal foi representada pelo ano inicial do período de fluxo, permitindo ordenar as observações cronologicamente e construir as variáveis defasadas.

A disponibilidade temporal dos indicadores auxiliares restringiu a janela comum de modelagem. A partir dessa interseção, foram utilizados os períodos-alvo de **2017–2018 a 2023–2024**. Após a criação das defasagens e a remoção da primeira observação de cada UF, a base final de modelagem contém **189 observações**, correspondentes a 27 UFs em sete períodos-alvo.

A remoção da primeira observação de cada UF decorre da necessidade de possuir um período anterior para a construção das variáveis preditoras. Portanto, essas exclusões não representam valores ausentes na fonte original.

## 3.3 Definição do problema preditivo e prevenção do vazamento de dados

A variável-alvo é a taxa de evasão observada no período atual. As variáveis explicativas utilizadas na modelagem correspondem ao período imediatamente anterior.

A estrutura temporal do problema pode ser representada como:

\[
\text{informações disponíveis em } t-1 \rightarrow \text{previsão da evasão em } t
\]

Essa definição evita utilizar informações do próprio período que se deseja prever. Consequentemente, variáveis do período-alvo não são empregadas como preditoras.

A divisão entre treinamento e teste também respeita a ordem temporal. Para cada fold, o modelo é ajustado apenas com períodos anteriores ao período de teste. Quando há necessidade de transformação dos dados, como a padronização utilizada na Regressão Ridge, essa transformação é ajustada exclusivamente com o conjunto de treinamento de cada fold e posteriormente aplicada ao conjunto de teste. Esse procedimento evita que informações do futuro sejam incorporadas ao processo de ajuste.

As verificações estruturais do protocolo incluíram ainda a confirmação de que nenhum período futuro estivesse presente no treinamento e de que os dois protocolos utilizassem os mesmos períodos e as mesmas UFs nos respectivos conjuntos de teste.

## 3.4 Cenário A — indicadores agregados

O **Cenário A** utiliza quatro variáveis preditoras, todas referentes ao período anterior:

| Grupo | Variável preditora |
|---|---|
| Histórico agregado | Taxa de evasão (t−1) |
| Histórico agregado | Taxa de conclusão (t−1) |
| Histórico agregado | Taxa de retenção (t−1) |
| Histórico agregado | Taxa de permanência (t−1) |

O alvo é a taxa de evasão no período t.

Esse cenário representa uma configuração baseada exclusivamente no histórico agregado dos indicadores de fluxo e funciona como referência para avaliar o efeito da inclusão das informações desagregadas.

## 3.5 Cenário B — informações agregadas e desagregadas

O **Cenário B** mantém as quatro variáveis do Cenário A e incorpora informações desagregadas da taxa de evasão observada no período anterior. As informações adicionais estão organizadas nas dimensões de **sexo, pertencimento a PPI, faixa etária e deficiência**. Neste estudo, PPI corresponde a pretos, pardos e indígenas.

O cenário possui 17 variáveis preditoras, distribuídas da seguinte forma:

| Dimensão | Informações utilizadas no período t−1 |
|---|---|
| Histórico agregado | evasão, conclusão, retenção e permanência |
| Sexo | evasão entre mulheres; evasão entre homens |
| PPI | evasão entre PPI; evasão entre não PPI |
| Faixa etária | evasão até 19 anos; 20–22; 23–24; 25–29; 30–39; 40–49; 50 anos ou mais |
| Deficiência | evasão entre pessoas com deficiência; evasão entre pessoas sem deficiência |

A comparação entre os cenários mantém constantes os algoritmos, os hiperparâmetros, os períodos de teste, os protocolos temporais e as métricas de avaliação. Dessa forma, a principal diferença experimental entre A e B é o conjunto de variáveis preditoras disponibilizado ao modelo.

É importante destacar que as variáveis do Cenário B representam **taxas de evasão desagregadas por grupo**, e não a composição demográfica da população estudantil. Portanto, sua interpretação permanece no nível agregado da unidade federativa e do período.

## 3.6 Protocolos de validação temporal

Foram empregados dois protocolos de validação temporal: **Expanding Window** e **Rolling Window**. Em ambos, os períodos de teste são os mesmos: 2021–2022, 2022–2023 e 2023–2024, sempre contendo as 27 UFs. A diferença entre os protocolos está na quantidade de histórico utilizada para treinamento.

### 3.6.1 Expanding Window

No Expanding Window, todo o histórico disponível até o período imediatamente anterior ao teste é incorporado ao treinamento.

| Fold | Treinamento | Teste | Observações de treino |
|---|---|---|---:|
| 1 | 2017–2018 a 2020–2021 | 2021–2022 | 108 |
| 2 | 2017–2018 a 2021–2022 | 2022–2023 | 135 |
| 3 | 2017–2018 a 2022–2023 | 2023–2024 | 162 |

Cada conjunto de teste contém 27 observações, uma para cada UF.

### 3.6.2 Rolling Window

No Rolling Window, utiliza-se uma janela fixa de quatro períodos imediatamente anteriores ao período de teste.

| Fold | Treinamento | Teste | Observações de treino |
|---|---|---|---:|
| 1 | 2017–2018 a 2020–2021 | 2021–2022 | 108 |
| 2 | 2018–2019 a 2021–2022 | 2022–2023 | 108 |
| 3 | 2019–2020 a 2022–2023 | 2023–2024 | 108 |

Cada conjunto de teste também contém 27 observações.

A utilização de ambos os protocolos permite verificar se o desempenho dos modelos se mantém semelhante quando se utiliza todo o histórico disponível ou apenas uma janela temporal recente e de tamanho fixo.

## 3.7 Baseline de persistência

Como referência foi utilizado um baseline de **persistência**, definido por:

\[
\hat{y}_t = y_{t-1}
\]

No contexto deste estudo, isso equivale a utilizar a taxa de evasão do período anterior como previsão para o período seguinte. A persistência é avaliada nos mesmos períodos de teste dos modelos supervisionados e estabelece uma referência simples baseada exclusivamente na continuidade temporal da própria variável-alvo.

## 3.8 Modelos avaliados

Foram comparadas cinco abordagens: persistência, Regressão Linear, Regressão Ridge, Random Forest e Gradient Boosting.

### 3.8.1 Persistência

Estratégia de referência definida anteriormente, sem ajuste de parâmetros a partir dos dados de treinamento.

### 3.8.2 Regressão Linear

Modelo linear utilizado como referência para a relação entre as variáveis preditoras e a taxa contínua de evasão.

### 3.8.3 Regressão Ridge

Modelo linear com regularização L2, conforme a formulação clássica de Hoerl e Kennard (1970). A padronização das variáveis é realizada em conjunto com o modelo dentro do treinamento de cada fold, evitando que parâmetros calculados com os dados de teste participem do ajuste.

### 3.8.4 Random Forest

Modelo baseado em um conjunto de árvores de decisão, utilizado para representar uma abordagem não linear, conforme a proposta de Random Forest de Breiman (2001). A configuração utilizada contou com 300 árvores, tamanho mínimo de três observações por folha e semente aleatória fixa em 42.

### 3.8.5 Gradient Boosting

Modelo de boosting baseado em árvores, também utilizado como abordagem não linear, seguindo a formulação apresentada por Friedman (2001). A configuração utilizada contou com 100 estimadores, taxa de aprendizagem de 0,05, profundidade máxima de dois níveis, tamanho mínimo de três observações por folha e semente aleatória fixa em 42.

Os hiperparâmetros foram definidos previamente e mantidos constantes entre os folds e os protocolos na rodada experimental analisada. Não foi realizada busca de hiperparâmetros orientada pelos conjuntos de teste. O objetivo foi manter condições comparáveis entre os métodos e os cenários.

## 3.9 Métricas de avaliação

O desempenho preditivo foi avaliado por **MAE, RMSE e R²**. As métricas foram calculadas individualmente em cada fold e, adicionalmente, sobre a concatenação das previsões fora da amostra dos três períodos de teste.

### 3.9.1 MAE

O erro absoluto médio (Mean Absolute Error — MAE) é calculado por:

\[
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
\]

A métrica representa o erro absoluto médio entre os valores observados e previstos. Quanto menor o MAE, menor o erro médio das previsões.

### 3.9.2 RMSE

A raiz do erro quadrático médio (Root Mean Squared Error — RMSE) é calculada por:

\[
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
\]

Como os erros são elevados ao quadrado antes da agregação, erros de maior magnitude têm maior influência no resultado.

### 3.9.3 R²

O coeficiente de determinação foi utilizado como medida complementar de desempenho relativo:

\[
R^2 = 1 - \frac{\sum(y_i-\hat{y}_i)^2}{\sum(y_i-\bar{y})^2}
\]

Valores próximos de 1 indicam maior desempenho em relação à referência baseada na média dos valores observados no conjunto avaliado. Valores negativos são possíveis quando as previsões apresentam erro superior ao dessa referência.

Nenhuma métrica isolada é utilizada para estabelecer uma classificação absoluta dos métodos. A interpretação considera conjuntamente o erro médio, a penalização de erros de maior magnitude e o comportamento ao longo dos períodos.

## 3.10 Análise de erros

Além das métricas agregadas, foram realizadas análises descritivas dos erros de previsão. Foram considerados o erro com sinal, o erro absoluto, medidas de distribuição dos erros, MAE por período, erro por UF, relação entre erro absoluto e taxa de evasão observada, distribuição do erro segundo faixas de evasão observada e frequência com que cada abordagem apresentou o menor erro absoluto em uma observação.

O erro com sinal foi definido como a diferença entre o valor observado e o valor previsto. Assim, valores positivos representam subestimação e valores negativos representam superestimação.

Também foi realizado um diagnóstico de calibração descritivo por meio de regressão linear entre valores observados e previstos. Esse ajuste é utilizado exclusivamente como instrumento diagnóstico e **não constitui um sexto modelo do experimento**.

As análises de erro são interpretadas como evidências descritivas sobre o comportamento preditivo dos métodos, sem atribuir relações causais aos padrões identificados.

## 3.11 Interpretabilidade do Cenário B

Como análise complementar, foi estudado o comportamento do **Gradient Boosting no Cenário B**, utilizando o protocolo Expanding Window.

Foram empregados dois mecanismos de análise de importância das variáveis.

### 3.11.1 Importância interna do modelo

Foi utilizada a importância das variáveis calculada pelo próprio conjunto de árvores. Essa medida permite identificar quais preditores participam mais fortemente das decisões internas do modelo.

### 3.11.2 Importância por permutação

Para cada fold, uma variável é embaralhada no conjunto de teste e observa-se a alteração no desempenho do modelo. As importâncias foram calculadas separadamente nos três folds e resumidas por média, desvio-padrão, mínimo, máximo e número de folds com importância positiva.

Essa análise busca caracterizar a **relevância preditiva** das variáveis e sua estabilidade temporal. Uma variável com maior importância não é interpretada como causa da evasão. Também são consideradas as limitações impostas pelo tamanho de cada conjunto de teste, que possui apenas 27 observações, e pela possível correlação entre variáveis relacionadas.

## 3.12 Validações estruturais e controles experimentais

Antes e durante a modelagem, foram realizadas verificações para garantir a consistência do experimento: ausência de duplicidades por UF e período; presença das 27 UFs nos períodos utilizados; ordenação temporal das observações; ausência de valores ausentes nas variáveis finais utilizadas na modelagem; correspondência entre os períodos de treinamento e teste; ausência de períodos futuros no treinamento; igualdade dos períodos de teste entre Expanding e Rolling; e igualdade das UFs presentes nos conjuntos de teste dos dois protocolos.

Além disso, foram mantidos constantes os hiperparâmetros e as métricas entre os cenários, de modo que a comparação entre A e B pudesse ser atribuída principalmente à alteração do conjunto de variáveis preditoras.

## 3.13 Estrutura do experimento

O desenho experimental combina duas configurações de variáveis preditoras, dois protocolos de validação temporal e cinco abordagens de previsão. As condições são avaliadas nos mesmos três períodos de teste, permitindo a comparação direta entre os cenários e os modelos.

| Dimensão | Condições |
|---|---|
| Cenário de variáveis | A: 4 preditores agregados; B: 17 preditores agregados e desagregados |
| Validação temporal | Expanding Window; Rolling Window |
| Abordagens | Persistência; Regressão Linear; Ridge; Random Forest; Gradient Boosting |
| Períodos de teste | 2021–2022; 2022–2023; 2023–2024 |
| Unidades por teste | 27 UFs |

O desenho contém **2 cenários × 2 protocolos × 5 abordagens**, totalizando **20 condições experimentais**. Como cada condição é avaliada em três folds temporais, são realizadas **60 avaliações modelo-fold** ao longo dos dois cenários, além da comparação consolidada das previsões fora da amostra.

Em cada cenário, existem 10 condições experimentais, correspondentes às cinco abordagens combinadas com os dois protocolos, cada uma avaliada nos três períodos de teste.

## 3.14 Limitações metodológicas

### 3.14.1 Unidade de análise agregada

A análise em nível de UF × período impede interpretações sobre risco individual de evasão. Os resultados descrevem capacidade preditiva para taxas agregadas.

### 3.14.2 Janela temporal disponível

Apesar de a fonte possuir uma série mais longa, a interseção temporal necessária entre os indicadores utilizados reduziu a janela efetivamente disponível para modelagem. O desenho possui apenas três períodos de teste fora da amostra.

### 3.14.3 Tamanho dos conjuntos de teste

Cada fold possui 27 observações no teste. Esse tamanho limita a precisão de algumas estatísticas descritivas e exige cautela adicional na interpretação da importância por permutação.

### 3.14.4 Natureza observacional

Os resultados são preditivos e não permitem estabelecer relações causais entre as variáveis utilizadas e a evasão.

### 3.14.5 Dependência entre variáveis

Variáveis agregadas e desagregadas podem representar dimensões relacionadas da mesma realidade educacional. Essa característica pode afetar tanto estimativas de modelos lineares quanto medidas de importância das variáveis.

### 3.14.6 Hiperparâmetros fixos

A rodada analisada utilizou hiperparâmetros definidos previamente, sem busca sistemática. Estudos posteriores poderiam comparar estratégias de ajuste de hiperparâmetros, desde que a seleção também respeite a estrutura temporal dos dados.

## 3.15 Posicionamento da contribuição metodológica

A contribuição metodológica deste estudo não está na proposição de um novo algoritmo, mas na construção de uma comparação controlada entre abordagens preditivas para uma taxa agregada de evasão. O experimento combina dois protocolos temporais, dois conjuntos de variáveis e cinco abordagens de previsão, utilizando os mesmos períodos de teste e as mesmas unidades federativas.

Esse desenho permite investigar separadamente o efeito da formação do histórico de treinamento e o efeito da ampliação das informações preditoras, mantendo constantes as demais condições experimentais. A análise complementar dos erros e da relevância preditiva das variáveis amplia a interpretação dos resultados sem ultrapassar o alcance observacional e agregado da base utilizada.

## 4 Resultados

## 4.1. Caracterização da base experimental

A base final de modelagem foi composta por 189 observações, correspondentes a 27 unidades federativas brasileiras acompanhadas em sete períodos de fluxo, de 2017–2018 a 2023–2024. Para cada UF e período-alvo, a variável dependente corresponde à taxa de evasão observada no período corrente, enquanto as variáveis preditoras foram construídas a partir das informações do período anterior (t-1).

A avaliação preditiva foi realizada em três períodos de teste: 2021–2022, 2022–2023 e 2023–2024. Cada fold de teste contém 27 observações, uma para cada UF. Assim, os cinco métodos avaliados foram submetidos a três avaliações temporais em cada um dos dois protocolos e em cada um dos dois cenários, totalizando 20 combinações modelo–protocolo–cenário e 60 avaliações fold-modelo–protocolo–cenário.

O Cenário A utilizou quatro preditores agregados. O Cenário B manteve esses quatro preditores e incorporou 13 variáveis adicionais de evasão desagregadas por sexo, pertencimento ao grupo de pretos, pardos e indígenas (PPI), faixa etária e deficiência, totalizando 17 preditores.

## 4.2. Desempenho no Cenário A

A Tabela 1 apresenta o desempenho agregado das previsões fora da amostra do Cenário A, obtido pela concatenação das previsões dos três períodos de teste.

### Tabela 1 — Desempenho agregado no Cenário A

| Modelo | Protocolo | MAE | RMSE | R² |
|---|---|---:|---:|---:|
| Persistência | Expanding | 1,9840 | 2,5240 | -0,2399 |
| Persistência | Rolling | 1,9840 | 2,5240 | -0,2399 |
| Regressão Linear | Expanding | 1,5891 | 2,1761 | 0,0783 |
| Regressão Linear | Rolling | 1,5988 | 2,1127 | 0,1312 |
| Ridge | Expanding | 1,5823 | 2,1419 | 0,1071 |
| Ridge | Rolling | 1,6214 | 2,1102 | 0,1333 |
| Random Forest | Expanding | 1,7317 | 2,2991 | -0,0288 |
| Random Forest | Rolling | 1,7138 | 2,2549 | 0,0104 |
| Gradient Boosting | Expanding | 1,8782 | 2,4053 | -0,1261 |
| Gradient Boosting | Rolling | 1,8422 | 2,3523 | -0,0770 |

### 4.2.1 Comportamento do baseline

A persistência apresentou MAE de 1,9840, RMSE de 2,5240 e R² de -0,2399 nos dois protocolos. Como a previsão da persistência é determinada exclusivamente pela taxa de evasão do período anterior, os resultados permanecem idênticos entre Expanding e Rolling.

Esse resultado estabelece uma referência para interpretar os modelos supervisionados. Nas avaliações fora da amostra agregadas, as quatro abordagens supervisionadas apresentaram MAE inferior ao baseline de persistência nos dois protocolos.

### 4.2.2 Regressão Linear e Ridge

As abordagens lineares apresentaram erros agregados inferiores aos observados nas demais abordagens supervisionadas no Cenário A. A Regressão Linear apresentou MAE de 1,5891 no Expanding e 1,5988 no Rolling. A Ridge apresentou MAE de 1,5823 no Expanding e 1,6214 no Rolling.

No protocolo Rolling, os valores de RMSE das duas abordagens foram muito próximos: 2,1127 para a Regressão Linear e 2,1102 para a Ridge. Os R² também foram próximos, 0,1312 e 0,1333, respectivamente. Portanto, os resultados agregados indicam comportamento semelhante entre os dois modelos lineares, com diferenças pequenas entre as condições.

### 4.2.3 Modelos baseados em árvores

O Random Forest apresentou MAE de 1,7317 no Expanding e 1,7138 no Rolling. O Gradient Boosting apresentou MAE de 1,8782 e 1,8422 nos mesmos protocolos. Em ambos os casos, os resultados agregados de R² foram negativos no Expanding para o Gradient Boosting (-0,1261) e para o Random Forest (-0,0288), enquanto no Rolling o Random Forest apresentou R² de 0,0104 e o Gradient Boosting de -0,0770.

Esses resultados mostram que, com o conjunto reduzido de quatro variáveis do Cenário A e sob o protocolo temporal adotado, as abordagens não lineares não reproduziram o mesmo nível de erro agregado observado nas abordagens lineares.

## 4.3. Comparação dos protocolos temporais no Cenário A

A comparação entre Expanding e Rolling indica diferenças relativamente pequenas no MAE agregado, mas diferenças mais perceptíveis em RMSE e R² para alguns métodos.

Na Regressão Linear, a mudança para Rolling elevou o MAE de 1,5891 para 1,5988, enquanto reduziu o RMSE de 2,1761 para 2,1127 e elevou o R² de 0,0783 para 0,1312. Na Ridge, o MAE passou de 1,5823 para 1,6214, enquanto o RMSE caiu de 2,1419 para 2,1102 e o R² passou de 0,1071 para 0,1333.

No Random Forest, o MAE foi reduzido de 1,7317 para 1,7138 no Rolling, acompanhando uma redução do RMSE de 2,2991 para 2,2549 e uma mudança do R² de -0,0288 para 0,0104. No Gradient Boosting, MAE e RMSE também foram menores no Rolling, passando de 1,8782 para 1,8422 e de 2,4053 para 2,3523, respectivamente, enquanto o R² passou de -0,1261 para -0,0770.

Esses resultados são compatíveis com a hipótese de que a quantidade de histórico utilizada no treinamento modifica o desempenho, mas a magnitude e a direção da alteração dependem do método e da métrica considerada.

## 4.4. Desempenho no Cenário B

A Tabela 2 apresenta os resultados agregados para o Cenário B.

### Tabela 2 — Desempenho agregado no Cenário B

| Modelo | Protocolo | MAE | RMSE | R² |
|---|---|---:|---:|---:|
| Persistência | Expanding | 1,9840 | 2,5240 | -0,2399 |
| Persistência | Rolling | 1,9840 | 2,5240 | -0,2399 |
| Regressão Linear | Expanding | 1,6713 | 2,1564 | 0,0949 |
| Regressão Linear | Rolling | 1,7276 | 2,1426 | 0,1065 |
| Ridge | Expanding | 1,6553 | 2,1557 | 0,0955 |
| Ridge | Rolling | 1,6732 | 2,1042 | 0,1383 |
| Random Forest | Expanding | 1,8504 | 2,3208 | -0,0483 |
| Random Forest | Rolling | 1,8628 | 2,3174 | -0,0452 |
| Gradient Boosting | Expanding | 1,7686 | 2,3054 | -0,0345 |
| Gradient Boosting | Rolling | 1,7867 | 2,3035 | -0,0327 |

A inclusão das informações desagregadas não produziu uma mudança uniforme de desempenho entre os métodos. Regressão Linear e Ridge apresentaram aumento de MAE em relação ao Cenário A nas condições comparáveis, enquanto o Gradient Boosting apresentou redução de MAE nos dois protocolos.

## 4.5. Efeito da inclusão das variáveis desagregadas

A Tabela 3 resume a diferença entre o Cenário B e o Cenário A. Valores positivos de ΔMAE representam aumento do erro absoluto médio no Cenário B; valores negativos representam redução.

### Tabela 3 — Diferença de desempenho entre os cenários A e B

| Modelo | Protocolo | Δ MAE | Δ RMSE | Δ R² |
|---|---|---:|---:|---:|
| Regressão Linear | Expanding | +0,0821 | -0,0197 | +0,0166 |
| Regressão Linear | Rolling | +0,1288 | +0,0299 | -0,0247 |
| Ridge | Expanding | +0,0730 | +0,0138 | -0,0116 |
| Ridge | Rolling | +0,0519 | -0,0060 | +0,0050 |
| Random Forest | Expanding | +0,1187 | +0,0217 | -0,0195 |
| Random Forest | Rolling | +0,1489 | +0,0625 | -0,0556 |
| Gradient Boosting | Expanding | -0,1096 | -0,0999 | +0,0916 |
| Gradient Boosting | Rolling | -0,0555 | -0,0488 | +0,0443 |

O comportamento mais distinto ocorreu no Gradient Boosting. No Expanding, a introdução das variáveis desagregadas reduziu o MAE em 0,1096 ponto e o RMSE em 0,0999, ao mesmo tempo em que elevou o R² em 0,0916. No Rolling, as diferenças também foram favoráveis em termos de erro e R², embora de menor magnitude.

Nas abordagens lineares e no Random Forest, a alteração foi menos favorável quando considerada exclusivamente pelo MAE. Ainda assim, alguns indicadores apresentaram mudanças em direções diferentes. Por exemplo, a Regressão Linear no Expanding apresentou aumento de MAE (+0,0821), mas redução de RMSE (-0,0197) e aumento de R² (+0,0166).

A persistência permaneceu inalterada, pois não utiliza as variáveis adicionais do Cenário B.

## 4.6. Variação temporal do efeito do Cenário B

A análise por fold mostrou que o efeito das variáveis desagregadas não é constante ao longo do tempo. O Gradient Boosting no protocolo Expanding apresentou os seguintes resultados de diferença de MAE em relação ao Cenário A:

| Período de teste | Δ MAE B − A | UFs com melhoria | UFs com piora |
|---|---:|---:|---:|
| 2021–2022 | +0,1404 | 11 | 16 |
| 2022–2023 | -0,4674 | 21 | 6 |
| 2023–2024 | -0,0020 | 13 | 14 |

O período de 2022–2023 concentrou a maior redução média de erro. Nesse fold, 21 das 27 UFs apresentaram redução do erro absoluto quando as variáveis desagregadas foram incorporadas ao Gradient Boosting, enquanto seis apresentaram aumento.

Entre as maiores reduções de erro absoluto nesse período estiveram Mato Grosso do Sul (-1,932), Pará (-1,698), Goiás (-1,686), Rio de Janeiro (-1,680), Amapá (-1,592) e Mato Grosso (-1,441). Entre as maiores elevações estiveram Alagoas (+2,249), Maranhão (+1,166) e Ceará (+0,534).

Os resultados mostram que a redução agregada observada para o Gradient Boosting no Cenário B não ocorreu de maneira uniforme nos três períodos. Houve uma contribuição particularmente forte do fold de 2022–2023, enquanto 2021–2022 apresentou aumento médio de MAE e 2023–2024 apresentou diferença média próxima de zero.

## 4.7. Análise dos erros no Cenário A

Para aprofundar a avaliação, foram analisados os erros das previsões fora da amostra do Cenário A. No caso da Ridge, o erro foi definido como real − previsão, de modo que valores positivos indicam subestimação e valores negativos indicam superestimação.

A distribuição dos erros da Ridge apresentou média de +0,9596, mediana de +0,8584, mínimo de -3,7883 e máximo de +8,3715. O maior erro positivo ocorreu para o Rio Grande do Norte no período 2022–2023, quando a taxa observada foi 22,2 e a previsão foi aproximadamente 13,83, resultando em erro de +8,37 pontos. Outro erro elevado ocorreu em Rondônia em 2021–2022, com taxa observada de 21,5 e previsão de aproximadamente 14,73, resultando em erro de +6,77 pontos.

Por período, o MAE da Ridge foi 1,993 em 2021–2022, 1,164 em 2022–2023 e 1,590 em 2023–2024. A maior diferença entre a média e casos individuais ocorreu no período 2022–2023, que apresentou MAE relativamente baixo apesar da presença de um erro máximo de 8,37 pontos.

## 4.8. Relação entre magnitude da evasão e erro de previsão

Foi calculada a correlação entre a taxa de evasão observada e o erro absoluto das previsões. Os coeficientes foram:

| Modelo | Correlação entre evasão observada e erro absoluto |
|---|---:|
| Persistência | 0,3336 |
| Ridge | 0,4658 |
| Random Forest | 0,5319 |
| Gradient Boosting | 0,5195 |

Os coeficientes positivos indicam associação entre maiores valores observados de evasão e maiores erros absolutos, com magnitudes diferentes entre os métodos.

A análise por tercis da evasão observada mostrou ainda que, para os quatro métodos, os erros absolutos médios foram maiores no grupo de maior evasão observada do que nos grupos de menor e intermediária evasão. Para a Ridge, por exemplo, o MAE foi 1,085 no tercil inferior, 1,192 no tercil intermediário e 2,519 no tercil superior.

Os erros com sinal também apresentaram padrões distintos entre os tercis. Na Ridge, a média do erro foi -0,424 no tercil inferior, +1,156 no tercil intermediário e +2,298 no tercil superior. Esse comportamento é compatível com uma tendência descritiva de subestimação nos casos de maior evasão observada, mas não permite, isoladamente, afirmar a existência de um mecanismo causal ou de uma propriedade estrutural permanente dos modelos.

## 4.9. Diagnóstico de calibração

Como análise complementar, foi ajustada uma regressão linear entre os valores observados e os valores previstos para cada método. Esse ajuste foi utilizado apenas como diagnóstico de calibração e não foi considerado um sexto método experimental.

Os resultados foram:

| Método | Intercepto | Inclinação | R² do diagnóstico |
|---|---:|---:|---:|
| Persistência | 8,635 | 0,523 | 0,329 |
| Ridge | 4,573 | 0,773 | 0,328 |
| Random Forest | 4,642 | 0,777 | 0,260 |
| Gradient Boosting | 5,397 | 0,732 | 0,198 |

Na Ridge, uma regressão adicional entre o erro com sinal e a evasão observada resultou em:

O ajuste descritivo entre o erro com sinal e a taxa de evasão observada pode ser expresso por: erro = 0,5750 × taxa de evasão − 8,6346.

Esse ajuste reforça, de forma descritiva, a associação positiva entre a taxa de evasão observada e o erro com sinal identificada na análise anterior.

## 4.10. Interpretabilidade do Cenário B

A análise de interpretabilidade foi concentrada no Gradient Boosting do Cenário B sob o protocolo Expanding. Foram comparadas a importância interna do modelo e a importância por permutação calculada nos três folds de teste.

Pela importância interna média, as variáveis com maiores valores foram:

| Variável | Importância média |
|---|---:|
| Taxa de evasão — 20 a 22 anos (t−1) | 0,2562 |
| Taxa de evasão — mulheres (t−1) | 0,2057 |
| Taxa de evasão — até 19 anos (t−1) | 0,1138 |
| Taxa de evasão — 40 a 49 anos (t−1) | 0,0604 |
| Taxa de retenção (t−1) | 0,0445 |
| Taxa de conclusão (t−1) | 0,0409 |

A importância por permutação (*permutation importance*) mostrou maior consistência para algumas variáveis. A média de importância de Taxa de evasão — mulheres (t−1) foi 0,1434, com valores positivos nos três folds. Taxa de evasão — até 19 anos (t−1) apresentou média de 0,0576 e também foi positiva nos três folds. Taxa de evasão — 20 a 22 anos (t−1) apresentou média de 0,1073, mas variou mais entre os períodos, com valor próximo de zero no último fold.

Outras variáveis apresentaram comportamento temporal mais instável. Taxa de permanência (t−1), por exemplo, apresentou importância por permutação (*permutation importance*) média de 0,0268, mas variou de -0,0755 a 0,1133 nos três folds. Taxa de evasão agregada (t−1), por outro lado, apresentou magnitude menor, porém importância positiva nos três períodos.

As importâncias negativas observadas em alguns folds não representam efeitos causais negativos. Nesse procedimento, elas indicam que a permutação da variável não aumentou o erro de teste naquele fold, podendo inclusive ter produzido uma pequena redução do erro. Como cada conjunto de teste contém apenas 27 observações, diferenças pequenas devem ser interpretadas com cautela.

## 4.11. Síntese dos resultados

Os experimentos evidenciaram três padrões principais.

Primeiro, a alteração do protocolo temporal modificou o desempenho agregado de várias abordagens, embora a magnitude e a direção dessa alteração dependessem do modelo e da métrica considerada. Segundo, a inclusão das variáveis de evasão desagregadas produziu efeitos heterogêneos entre os métodos e entre os períodos: para o Gradient Boosting, houve redução agregada de erro nos dois protocolos, enquanto Regressão Linear, Ridge e Random Forest apresentaram aumento do MAE agregado. Terceiro, a análise de interpretabilidade indicou que algumas variáveis desagregadas, especialmente Taxa de evasão — mulheres (t−1) e determinadas faixas etárias, contribuíram de forma relevante para as previsões do Gradient Boosting, mas essa relevância variou em magnitude entre os folds.

Esses achados devem ser interpretados como resultados preditivos e descritivos. Eles não permitem concluir que uma determinada variável desagregada cause maior ou menor evasão, nem que sua inclusão produza necessariamente melhoria em períodos futuros.

## 5 Discussão

## 5.1. Considerações iniciais sobre os achados

Os resultados deste estudo devem ser interpretados a partir de duas dimensões complementares: a capacidade preditiva dos modelos e o efeito do desenho temporal e do conjunto de variáveis sobre essa capacidade. Em vez de indicar um comportamento uniforme entre todos os métodos, os experimentos mostram que o desempenho depende da combinação entre modelo, protocolo de validação e informações disponíveis para a previsão.

Esse resultado é coerente com a própria heterogeneidade identificada na literatura brasileira sobre evasão. A revisão sistemática de Mançano, Monteiro e Carmo (2026) aponta que, entre os estudos quantitativos selecionados, predominam análise de sobrevivência e regressões logísticas e que a diversidade de variáveis e modelos dificulta comparações diretas entre resultados. Nesse sentido, o desenho adotado neste trabalho procura reduzir parte dessa heterogeneidade ao manter constantes os períodos de teste, as unidades federativas e as métricas, variando sistematicamente o protocolo temporal e o conjunto de preditores.

O estudo também se diferencia de trabalhos preditivos existentes por não formular a tarefa como classificação individual de estudantes. Silva, Cabral e Pacheco (2020), por exemplo, desenvolveram modelos de regressão logística para prever evasão ou permanência de estudantes de uma instituição de ensino superior. No presente trabalho, a unidade de análise é agregada por UF e período, e o objetivo é prever a taxa de evasão no período subsequente. Assim, os resultados não devem ser comparados diretamente em termos de acurácia entre os dois estudos, mas podem ser aproximados quanto ao interesse comum em avaliar o potencial preditivo de informações associadas à evasão.

## 5.2. Discussão da hipótese H1: efeito do protocolo temporal

A primeira hipótese estabeleceu que a utilização de diferentes estratégias de validação temporal produziria diferenças mensuráveis no desempenho preditivo. Os resultados são compatíveis com essa hipótese, embora as diferenças observadas não tenham sido uniformes entre os modelos ou entre as métricas.

No Cenário A, a mudança do Expanding para o Rolling produziu alterações no MAE entre -0,0179 e +0,0391 ponto nos quatro modelos supervisionados. Apesar da pequena magnitude dessas diferenças, houve mudanças mais visíveis no RMSE e no R². Na Regressão Linear, por exemplo, o R² passou de 0,0783 no Expanding para 0,1312 no Rolling; na Ridge, de 0,1071 para 0,1333. Já no Random Forest, o R² passou de -0,0288 para 0,0104.

Esse comportamento sugere que a quantidade e a composição do histórico utilizado no treinamento podem afetar a capacidade de generalização para períodos posteriores, mesmo quando os períodos de teste são mantidos constantes. A diferença entre os protocolos, portanto, não se manifesta necessariamente como uma mudança grande no erro médio absoluto, mas pode aparecer com maior clareza na sensibilidade a erros maiores, capturada pelo RMSE, e na variância explicada, representada pelo R².

No entanto, os resultados também mostram que não seria adequado interpretar o protocolo Rolling como universalmente superior ao Expanding. Na Regressão Linear e na Ridge, por exemplo, houve redução do RMSE e aumento do R² no Rolling, mas aumento do MAE. Isso evidencia que os protocolos podem produzir leituras diferentes conforme a métrica adotada. A hipótese H1, portanto, encontra apoio na existência de diferenças mensuráveis, mas os resultados não sustentam uma interpretação de vantagem uniforme de uma estratégia sobre a outra.

## 5.3. Discussão da hipótese H2: efeito das informações desagregadas

A segunda hipótese propôs que a incorporação de informações desagregadas da evasão modificaria o desempenho em relação ao cenário formado apenas por variáveis agregadas. Os resultados dão suporte claro a essa hipótese.

A alteração do conjunto de variáveis produziu efeitos distintos entre os modelos. No Gradient Boosting, a passagem do Cenário A para o Cenário B reduziu o MAE de 1,8782 para 1,7686 no Expanding e de 1,8422 para 1,7867 no Rolling. Também houve redução do RMSE e aumento do R² nas duas estratégias. Em contraste, a Regressão Linear, a Ridge e o Random Forest apresentaram aumento do MAE agregado com a inclusão das informações desagregadas.

Esse comportamento é importante porque mostra que adicionar variáveis não produz automaticamente melhoria de desempenho. O efeito depende da forma como o modelo utiliza a informação adicional. No conjunto avaliado, a inclusão de 13 novas variáveis alterou substancialmente o espaço de predição, mas os ganhos não foram compartilhados por todos os métodos. Portanto, H2 não deve ser interpretada como uma hipótese de que o Cenário B necessariamente produziria previsões mais precisas; a hipótese dizia respeito à existência de efeito, e esse efeito foi observado.

Esse resultado também dialoga com a literatura sistematizada por Mançano, Monteiro e Carmo (2026). Os autores identificam ampla diversidade de variáveis nos estudos sobre evasão e destacam que sexo, idade e raça/cor estão entre as características mais frequentemente investigadas. A revisão também mostra que a frequência de significância varia entre as variáveis, e que a disponibilidade e a qualidade dos dados administrativos condicionam o que pode ser incorporado aos modelos. Nesse sentido, o presente experimento acrescenta uma dimensão preditiva à discussão: não se analisou apenas se uma variável aparece associada à evasão em um modelo estatístico, mas se informações desagregadas do próprio indicador de evasão alteram a previsão da taxa agregada em períodos futuros.

É importante, contudo, evitar equivalência direta entre os resultados. Os estudos reunidos por Mançano, Monteiro e Carmo analisam principalmente associações entre características dos estudantes e evasão, enquanto este trabalho utiliza taxas agregadas por UF. Dessa forma, a presença de uma variável como taxa de evasão entre mulheres no período anterior no conjunto preditor não significa que ser mulher, individualmente, aumente ou reduza a probabilidade de evasão. Trata-se da taxa de evasão observada entre mulheres na UF no período anterior. Essa distinção é essencial para evitar interpretação individual ou causal de uma variável agregada.

## 5.4. Discussão da hipótese H3: heterogeneidade temporal do efeito do Cenário B

A terceira hipótese estabeleceu que o efeito do conjunto de variáveis desagregadas não seria necessariamente uniforme entre os períodos de teste. Os resultados apresentam evidência consistente em favor dessa hipótese.

O caso mais evidente foi o Gradient Boosting sob o protocolo Expanding. Entre 2021–2022 e 2022–2023, o efeito do Cenário B mudou de um aumento médio do MAE de 0,1404 para uma redução de 0,4674. No último período, 2023–2024, a diferença foi praticamente nula (-0,0020). Esse padrão demonstra que uma melhoria observada no resultado agregado pode esconder diferenças relevantes entre os momentos avaliados.

A análise por UF reforça essa conclusão. Em 2022–2023, 21 das 27 unidades federativas apresentaram redução do erro absoluto com a inclusão das variáveis desagregadas, enquanto seis apresentaram aumento. Portanto, o ganho nesse período não pode ser atribuído apenas a uma pequena quantidade de observações extremas. Ao mesmo tempo, como houve piora em outras unidades e o comportamento mudou nos demais períodos, também não é possível tratar a incorporação dessas informações como uma melhoria estável e generalizável para qualquer horizonte.

Esse achado é compatível com resultados da literatura que mostram que a relação entre características dos estudantes e evasão pode variar segundo o contexto. Nierotka, Bonamino e Carrasqueira (2023), por exemplo, mostram que determinadas associações encontradas em uma instituição podem estar relacionadas à configuração específica da instituição e às iniciativas implementadas localmente. Silva, Cabral e Pacheco (2020) também observaram, em seu estudo, que diferentes cursos podem apresentar variáveis distintas associadas à evasão e que uma mesma variável pode produzir efeitos diferentes em contextos distintos. Embora esses trabalhos tenham unidades de análise diferentes, ambos reforçam a necessidade de cautela ao transportar relações observadas em um contexto para outro.

## 5.5. Desempenho dos modelos e implicações para o desenho preditivo

Os resultados do Cenário A mostraram desempenho mais consistente das abordagens lineares, especialmente da Regressão Linear e da Ridge, em termos de erro agregado. Esse padrão não significa que relações não lineares sejam irrelevantes para a evasão, mas indica que, sob o conjunto específico de quatro preditores agregados e o tamanho amostral utilizado, os modelos mais complexos não produziram redução de erro em relação às abordagens lineares.

A diferença observada no Cenário B é especialmente relevante. O Gradient Boosting apresentou redução de erro após a incorporação das variáveis desagregadas, enquanto essa alteração não se repetiu nas outras abordagens. Uma interpretação possível é que as novas variáveis tenham introduzido padrões combinados que foram melhor aproveitados por uma função de predição não linear. Essa interpretação, entretanto, deve ser considerada como hipótese explicativa e não como conclusão causal, pois o experimento não isolou quais interações específicas foram responsáveis pelo comportamento.

Também é importante considerar o papel do tamanho da base. O experimento utiliza 189 observações, distribuídas em 27 UFs e sete períodos-alvo, com apenas 27 observações em cada conjunto de teste. Nesse contexto, alterações relativamente pequenas em alguns períodos podem produzir mudanças perceptíveis nas métricas agregadas. Por isso, a comparação de modelos deve ser lida juntamente com a análise por fold e não apenas com os valores agregados.

A utilização da persistência como baseline reforça essa interpretação. O R² negativo do baseline de persistência (-0,2399) indica que, nos conjuntos de teste agregados, essa estratégia apresentou desempenho inferior ao benchmark baseado na média, segundo essa métrica. Os modelos supervisionados, em geral, reduziram o MAE em relação a esse baseline, indicando que as variáveis utilizadas carregam informação adicional para a previsão. Ainda assim, os valores de R² próximos de zero e, em algumas condições, negativos, mostram que a capacidade explicativa preditiva permanece limitada e que os resultados não devem ser apresentados como previsão de alta precisão.

## 5.6. Análise dos erros e comportamento em níveis diferentes de evasão

A análise de erros mostra um aspecto complementar do experimento: os modelos não apresentam o mesmo comportamento em todos os níveis observados de evasão. A correlação positiva entre a taxa observada e o erro absoluto foi de 0,4658 para a Ridge, 0,5319 para o Random Forest e 0,5195 para o Gradient Boosting. Além disso, a análise por tercis mostrou erros absolutos maiores no grupo de maior evasão observada.

Para a Ridge, esse padrão foi particularmente visível: o MAE passou de 1,085 no tercil inferior para 2,519 no tercil superior. Ao mesmo tempo, o erro com sinal passou de média negativa no tercil inferior para média positiva no tercil superior. Descritivamente, isso indica que os modelos tendem a produzir previsões mais próximas de uma faixa intermediária, superestimando parte dos valores baixos e subestimando parte dos valores altos.

Esse comportamento deve ser tratado como diagnóstico, e não como evidência de uma propriedade universal dos modelos. Os dados de teste são pequenos e os níveis de evasão variam entre as UFs. Ainda assim, o resultado aponta para uma questão importante para aplicações futuras: avaliar apenas o MAE agregado pode ocultar uma maior dificuldade de previsão nos extremos da distribuição.

## 5.7. Interpretabilidade do Cenário B

A análise de interpretabilidade do Gradient Boosting acrescenta uma dimensão importante aos resultados de desempenho. A taxa de evasão entre mulheres no período anterior apresentou a maior média de permutation importance entre as variáveis analisadas, com valor positivo nos três folds. A taxa de evasão entre estudantes de até 19 anos no período anterior também manteve importância positiva nos três períodos, enquanto taxa de evasão entre estudantes de 20 a 22 anos no período anterior apresentou valor médio elevado, mas maior instabilidade entre os folds.

Há uma aproximação interessante entre esse resultado e a literatura nacional. Mançano, Monteiro e Carmo (2026) identificam sexo e idade entre as variáveis mais frequentemente investigadas nos estudos brasileiros e relatam que idade apresentou associação estatisticamente consistente nos trabalhos que a analisaram. Nierotka, Bonamino e Carrasqueira (2023), por sua vez, encontraram associação entre ser mulher, estar na faixa etária de até 20 anos e menores chances de evasão na coorte analisada.

Entretanto, a comparação deve permanecer no nível da relevância das dimensões analisadas, e não da direção dos efeitos. No presente trabalho, a variável taxa de evasão entre mulheres no período anterior representa uma taxa agregada de evasão feminina por UF e período, e sua permutation importance indica quanto o desempenho preditivo do modelo se altera quando essa informação é embaralhada. Isso não permite afirmar que a condição de ser mulher provoque maior ou menor evasão individual.

A instabilidade encontrada em taxa de permanência do período anterior e em algumas outras variáveis também é informativa. Uma variável pode apresentar importância elevada em um fold e baixa ou negativa em outro sem que isso implique mudança causal no fenômeno. No caso deste experimento, com 27 observações por conjunto de teste, a permutation importance deve ser vista como uma evidência de utilidade preditiva contextual, sujeita à variação amostral.

## 5.8. Contribuição do estudo frente à literatura

A contribuição deste trabalho está menos na proposição de um novo algoritmo de aprendizado de máquina e mais no desenho comparativo utilizado para estudar a previsão da taxa de evasão em uma estrutura temporal comum.

A literatura nacional já apresenta estudos com regressão logística e análise de sobrevivência e também há trabalhos explicitamente voltados à construção de modelos preditivos. Mançano, Monteiro e Carmo (2026) mostram, inclusive, que a literatura sobre fatores associados à evasão é marcada por heterogeneidade de variáveis e modelos, o que dificulta comparações diretas.

Nesse contexto, este estudo contribui ao estabelecer um protocolo único para comparar cinco abordagens preditivas, dois mecanismos de treinamento temporal e dois conjuntos de variáveis, utilizando os mesmos períodos de teste e as mesmas 27 UFs. A comparação entre Cenário A e Cenário B acrescenta ainda uma segunda dimensão experimental: o efeito da incorporação de taxas de evasão desagregadas por sexo, pertencimento ao grupo de pretos, pardos e indígenas (PPI), faixa etária e deficiência.

O estudo também enfatiza a importância da validação temporal. Em problemas de previsão de fenômenos educacionais, o objetivo é estimar valores futuros a partir de informações disponíveis anteriormente. A separação temporal adotada busca aproximar esse cenário e evita que informações de períodos posteriores sejam utilizadas para prever períodos anteriores. Dessa forma, o desempenho reportado deve ser entendido como desempenho fora da amostra sob os períodos de teste especificados, e não como desempenho retrospectivo sobre toda a base.

## 5.9. Limitações e implicações para trabalhos futuros

A primeira limitação é o tamanho temporal da base efetivamente utilizada na modelagem. Embora o indicador de evasão tenha série mais longa, as variáveis auxiliares necessárias para os cenários avaliados estão disponíveis a partir de período mais recente, restringindo a janela comum de modelagem a sete períodos-alvo.

A segunda limitação decorre da unidade de análise. As observações representam UF × período, portanto os resultados descrevem padrões agregados e não permitem inferir comportamentos individuais de estudantes. Essa característica impede, por exemplo, interpretar a importância de uma taxa de evasão feminina como efeito individual do sexo sobre a probabilidade de evasão.

A terceira limitação está relacionada ao número de observações nos conjuntos de teste: 27 UFs por fold. Esse tamanho reduzido pode aumentar a sensibilidade das métricas e das medidas de interpretabilidade a casos específicos. A análise por período e por UF foi incluída justamente para reduzir o risco de interpretar apenas os resultados agregados.

A quarta limitação é que os modelos foram avaliados com configurações de hiperparâmetros definidas no protocolo experimental. O estudo não realizou uma busca exaustiva de hiperparâmetros nem uma comparação de técnicas adicionais de seleção de atributos. Assim, os resultados representam o desempenho das configurações especificadas, e não um limite máximo de desempenho que cada algoritmo poderia atingir.

Por fim, a análise não possui desenho causal. As associações encontradas entre variáveis desagregadas e desempenho preditivo indicam utilidade para a previsão no conjunto estudado, mas não permitem concluir que essas variáveis causem a evasão nem que intervenções sobre elas produziriam determinada alteração na taxa de evasão.

## 5.10. Síntese em relação às hipóteses

Considerando o conjunto dos resultados, H1 encontra suporte descritivo porque a alteração entre Expanding e Rolling produziu diferenças observáveis nas métricas de desempenho, ainda que pequenas e dependentes do modelo e da métrica. H2 também encontra suporte descritivo, uma vez que a inclusão das informações desagregadas alterou o desempenho em relação ao Cenário A, com efeitos distintos entre os métodos. H3 encontra suporte mais evidente, pois o efeito do Cenário B variou de forma substancial entre os períodos de teste, especialmente no Gradient Boosting.

Assim, as hipóteses não apontam para uma única configuração universalmente superior, mas para a existência de dependência entre estratégia temporal, conjunto de variáveis e momento da previsão. Esse resultado é central para a interpretação do experimento e reforça a necessidade de avaliar modelos preditivos de evasão sob protocolos que respeitem a estrutura temporal do problema.

## 6 Conclusão

## 6.1. Retomada do problema e do objetivo

Este trabalho teve como objetivo avaliar comparativamente diferentes abordagens preditivas para a taxa de evasão no ensino superior brasileiro, considerando protocolos de validação temporal e diferentes conjuntos de variáveis preditoras. A análise foi realizada em nível agregado de Unidade da Federação (UF) e período, tendo como variável-alvo a taxa de evasão observada no período seguinte.

O desenho experimental foi construído para preservar a ordem temporal dos dados e evitar o uso de informações futuras no treinamento. Foram comparados os protocolos Expanding e Rolling, cinco métodos preditivos — Persistência, Regressão Linear, Ridge, Random Forest e Gradient Boosting — e dois conjuntos de variáveis: o Cenário A, formado pelas taxas agregadas defasadas de evasão, conclusão, retenção e permanência; e o Cenário B, que acrescentou informações desagregadas da taxa de evasão por sexo, pertencimento ao grupo de pretos, pardos e indígenas (PPI), faixa etária e deficiência.

## 6.2. Síntese dos principais achados

Os resultados mostram que o desempenho preditivo depende simultaneamente do método empregado, do protocolo temporal e do conjunto de informações disponibilizado ao modelo. No Cenário A, os métodos lineares apresentaram erros médios inferiores aos métodos baseados em árvores nos conjuntos de teste agregados, enquanto a persistência apresentou desempenho inferior aos modelos ajustados. O resultado evidencia que a informação histórica disponível nas variáveis defasadas possui capacidade preditiva adicional em relação à simples repetição do valor anterior da evasão.

A comparação entre Expanding e Rolling não produziu uma diferença uniforme entre todos os métodos. Em alguns casos, a utilização de uma janela histórica fixa apresentou métricas agregadas ligeiramente diferentes daquelas obtidas com a acumulação progressiva das observações, mas a direção e a magnitude dessas diferenças variaram conforme o modelo. Esse resultado sustenta a importância de considerar o protocolo temporal como parte do desenho experimental, em vez de tratá-lo apenas como uma escolha operacional de treinamento.

A incorporação das variáveis desagregadas no Cenário B também não produziu um efeito uniforme. Para Regressão Linear, Ridge e Random Forest, foram observadas alterações relativamente pequenas ou aumento do MAE em determinadas condições. Para Gradient Boosting, por outro lado, o acréscimo das informações desagregadas esteve associado à redução do MAE e do RMSE agregados nos dois protocolos. Esse comportamento, contudo, não se repetiu da mesma forma em todos os períodos de teste.

A análise por período mostrou que a principal contribuição do Cenário B para o Gradient Boosting esteve associada ao período 2022–2023. Nesse intervalo, houve redução substancial do erro médio absoluto e a maior parte das UFs apresentou redução do erro absoluto. Em 2021–2022, ocorreu o movimento oposto, enquanto em 2023–2024 a diferença entre os cenários foi pequena em termos de erro médio. Dessa forma, a informação desagregada apresentou utilidade preditiva dependente do período analisado.

A análise de erros também indicou associação entre a magnitude observada da evasão e o tamanho do erro de previsão. Os modelos apresentaram maior dificuldade nos casos de evasão mais elevada, com tendência descritiva de aproximação das previsões a valores intermediários. Esse comportamento deve ser interpretado como característica do conjunto de previsões analisado e não como evidência de um mecanismo causal.

Na análise de interpretabilidade do Gradient Boosting no Cenário B, as variáveis associadas à evasão feminina e à faixa etária de 20 a 22 anos apresentaram destaque entre as medidas de importância. A importância por permutação também mostrou que a relevância das variáveis pode variar entre os períodos de teste. Esses resultados indicam que informações desagregadas podem contribuir para a previsão, mas não autorizam interpretar a importância preditiva como efeito causal de uma característica sobre a evasão.

## 6.3. Retomada das hipóteses

### 6.3.1 H1 — efeito do protocolo temporal

Os resultados oferecem suporte descritivo parcial à hipótese H1. Foram observadas diferenças de desempenho entre Expanding e Rolling, mas elas dependeram do modelo e da métrica considerada. Portanto, os resultados sustentam que a escolha do protocolo temporal pode alterar a avaliação do desempenho, sem indicar uma superioridade uniforme de uma estratégia para todas as condições experimentais.

### 6.3.2 H2 — efeito da informação desagregada

Os resultados são compatíveis com a hipótese H2, uma vez que a inclusão das variáveis desagregadas alterou de forma mensurável o desempenho. A inclusão das variáveis desagregadas modificou as métricas em todas as abordagens avaliadas, embora a direção dessa mudança não tenha sido a mesma entre os modelos. No caso do Gradient Boosting, a alteração agregada foi acompanhada por redução de erro nos dois protocolos, enquanto outros modelos apresentaram efeitos mais discretos ou aumento do erro médio absoluto.

### 6.3.3 H3 — heterogeneidade temporal do efeito do conjunto de variáveis

Os resultados oferecem suporte descritivo à hipótese H3. O efeito do Cenário B variou entre os períodos de teste, com diferenças particularmente marcantes em 2022–2023 e alterações muito menores em 2023–2024. A utilização de diferentes janelas temporais, portanto, não apenas modifica o volume de informação disponível para o treinamento, como também permite identificar que a utilidade preditiva de determinados sinais pode depender do período analisado.

## 6.4. Contribuição do trabalho

A principal contribuição do estudo está no desenho comparativo adotado. Em vez de avaliar uma única técnica ou de realizar uma comparação entre modelos sem considerar a ordem temporal, o trabalho combina diferentes métodos preditivos com protocolos temporais explícitos e dois níveis de informação sobre a evasão.

Esse desenho amplia a análise da evasão agregada no ensino superior brasileiro em relação a estudos cuja unidade de análise é o estudante e cujo objetivo central é estimar associações individuais ou o tempo até o evento. A revisão sistemática de Mançano, Monteiro e Carmo (2026) mostra que a literatura brasileira reúne abordagens diversas, mas identifica análise de sobrevivência e regressões logísticas como métodos recorrentes nos estudos que investigam fatores associados à evasão. O presente trabalho se posiciona nesse campo como uma avaliação preditiva agregada e comparativa, sem substituir as abordagens longitudinais individuais existentes.

## 6.5. Limitações

Os resultados devem ser interpretados considerando as limitações do desenho. A unidade de análise é a UF por período, o que impede extrapolar os achados para previsões individuais de estudantes. Além disso, o número de períodos disponíveis para treinamento e teste é limitado, e cada fold possui apenas 27 observações de teste, correspondentes às UFs brasileiras. Isso reduz a estabilidade de algumas métricas e recomenda cautela especialmente na interpretação das importâncias por permutação.

Outra limitação é que o Cenário B utiliza taxas de evasão desagregadas por grupos, e não variáveis individuais de composição socioeconômica ou trajetória acadêmica. Consequentemente, a presença de determinada variável entre as mais importantes em um modelo não significa que pertencer ao grupo correspondente cause maior ou menor evasão.

Também é necessário considerar que o conjunto de indicadores utilizado resume processos complexos em medidas agregadas. Diferenças institucionais, econômicas, territoriais, acadêmicas e de políticas de permanência entre as UFs não são integralmente capturadas pelas variáveis disponíveis.

## 6.6. Possibilidades de continuidade

Uma extensão natural do trabalho seria incorporar períodos adicionais à medida que novas edições dos Indicadores de Fluxo forem disponibilizadas, mantendo o mesmo protocolo temporal para avaliar a estabilidade dos achados. Também seria possível explorar outras fontes de dados e variáveis institucionais e socioeconômicas compatíveis com a unidade de análise, além de investigar modelos capazes de representar relações não lineares e estruturas hierárquicas.

Outra possibilidade consiste em comparar o cenário agregado desenvolvido neste estudo com uma abordagem em nível individual, utilizando microdados apropriados e protocolos de validação que respeitem a trajetória temporal dos estudantes. Essa extensão permitiria analisar em que medida padrões observados no nível das UFs se mantêm quando a unidade de análise passa a ser o indivíduo.

## 6.7. Encerramento

Os resultados indicam que a previsão da taxa de evasão em nível agregado pode se beneficiar de uma avaliação experimental que considere simultaneamente o modelo, o histórico temporal utilizado no treinamento e o nível de desagregação das informações. Os resultados não permitem identificar uma configuração que mantenha desempenho superior em todas as condições. Eles mostram, em vez disso, que o comportamento preditivo depende das condições em que os modelos são avaliados.

Essa constatação reforça a importância de protocolos temporais explícitos e de análises comparativas na construção de sistemas preditivos aplicados à educação superior. No contexto investigado, a combinação entre diferentes métodos, cenários de informação e períodos de teste permite observar não apenas diferenças médias de desempenho, mas também a heterogeneidade desses efeitos ao longo do tempo.

## 7 Referências

## 7.1 Referências centrais sobre evasão no ensino superior

KLITZKE, Melina; CARVALHAES, Flavio. Fatores associados à evasão de curso na UFRJ: uma análise de sobrevivência. *Educação em Revista*, Belo Horizonte, v. 39, e37576, 2023. DOI: https://doi.org/10.1590/0102-469837576. Disponível em: https://www.scielo.br/j/edur/a/T48zB4dDcZFCSPM6JBbcGKP/. Acesso em: 25 set. 2026.

MANÇANO, Tales; MONTEIRO, Geovânio; CARMO, Erico. Revisão sistemática dos artigos sobre fatores associados à evasão na educação superior no Brasil. *Conversas & Controvérsias*, Porto Alegre, v. 13, n. 1, e48104, 2026. DOI: https://doi.org/10.15448/2178-5694.2026.1.48104. Disponível em: https://revistaseletronicas.pucrs.br/conversasecontroversias/article/view/48104. Acesso em: 25 set. 2026.

NIEROTKA, Rosileia Lucia; BONAMINO, Alicia Maria Catalano de; CARRASQUEIRA, Karina. Acesso, evasão e conclusão no Ensino Superior público: evidências para uma coorte de estudantes. *Ensaio: Avaliação e Políticas Públicas em Educação*, Rio de Janeiro, v. 31, n. 118, 2023. DOI: https://doi.org/10.1590/S0104-40362022003003107. Disponível em: https://www.scielo.br/j/ensaio/a/wyCSCb88RyNtDnynHHxftrp/. Acesso em: 25 set. 2026.

NIEROTKA, Rosileia Lucia; SALATA, Andre; KLITZKE MARTINS, Melina. Fatores associados à evasão no ensino superior: um estudo longitudinal. *Cadernos de Pesquisa*, São Paulo, v. 53, e09961, 2023. DOI: https://doi.org/10.1590/198053149961. Disponível em: https://publicacoes.fcc.org.br/cp/article/view/9961. Acesso em: 25 set. 2026.

SACCARO, Alice; FRANÇA, Marco Túlio Aniceto; JACINTO, Paulo de Andrade. Fatores associados à evasão no ensino superior brasileiro: um estudo de análise de sobrevivência para os cursos das áreas de Ciência, Matemática e Computação e de Engenharia, Produção e Construção em instituições públicas e privadas. *Estudos Econômicos (São Paulo)*, São Paulo, v. 49, n. 2, p. 337-373, 2019. DOI: https://doi.org/10.1590/0101-41614925amp. Disponível em: https://revistas.usp.br/ee/pt_BR/article/view/125387. Acesso em: 25 set. 2026.

SILVA, Fernanda Cristina da; CABRAL, Thiago Luiz de Oliveira; PACHECO, Andressa Sasaki Vasques. Dropout or permanence? Predictive models for higher education management. *Education Policy Analysis Archives*, v. 28, n. 149, 2020. DOI: https://doi.org/10.14507/epaa.28.5387. Disponível em: https://epaa.asu.edu/index.php/epaa/article/view/5387. Acesso em: 25 set. 2026.

ROSA, Chaiane de Medeiros; MILANI, Eder Angelo; SANTOS, Fabiano Fortunato Teixeira dos. Do acesso à evasão: o acompanhamento dos estudantes da UFG utilizando análise de sobrevivência. *Perspectiva*, Florianópolis, v. 39, n. 4, p. 1-20, 2021. DOI: https://doi.org/10.5007/2175-795X.2021.e71241. Disponível em: https://periodicos.ufsc.br/index.php/perspectiva/article/view/71241. Acesso em: 25 set. 2026.

TINTO, Vincent. Dropout from higher education: a theoretical synthesis of recent research. *Review of Educational Research*, v. 45, n. 1, p. 89-125, 1975.

VITELLI, Ricardo Ferreira; FRITSCH, Rosangela. Evasão escolar na educação superior: de que indicador estamos falando? *Estudos em Avaliação Educacional*, São Paulo, v. 27, n. 66, p. 908-937, 2016. DOI: https://doi.org/10.18222/eae.v27i66.4009.

## 7.2 Fonte de dados

BRASIL. Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). *Indicadores de Fluxo da Educação Superior*. Brasília, DF: INEP, 2025. Base com indicadores de fluxo da educação superior para 2010-2024. Disponível em: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/indicadores-de-fluxo-da-educacao-superior. Acesso em: 25 set. 2026.

## 7.3 Referências metodológicas para os modelos

BREIMAN, Leo. Random forests. *Machine Learning*, v. 45, p. 5-32, 2001. DOI: https://doi.org/10.1023/A:1010933404324.

FRIEDMAN, Jerome H. Greedy function approximation: a gradient boosting machine. *The Annals of Statistics*, v. 29, n. 5, p. 1189-1232, 2001. DOI: https://doi.org/10.1214/aos/1013203451.

HOERL, Arthur E.; KENNARD, Robert W. Ridge regression: biased estimation for nonorthogonal problems. *Technometrics*, v. 12, n. 1, p. 55-67, 1970. DOI: https://doi.org/10.1080/00401706.1970.10488634.
