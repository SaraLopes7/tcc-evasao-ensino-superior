# 6 Conclusão

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
