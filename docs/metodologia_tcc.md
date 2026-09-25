# 3 Metodologia

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
