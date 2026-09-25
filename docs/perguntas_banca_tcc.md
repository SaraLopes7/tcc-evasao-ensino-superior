# Perguntas prováveis de banca — TCC

Este documento reúne perguntas que podem surgir durante a apresentação e respostas-base coerentes com o desenho experimental e os resultados do trabalho.

## 1. Por que prever a taxa de evasão em nível de UF, e não a evasão de estudantes individuais?

O trabalho foi delimitado para uma unidade de análise agregada por UF e período porque a fonte utilizada disponibiliza indicadores de fluxo nessa estrutura. O objetivo não é estimar o risco individual de evasão, mas avaliar a capacidade preditiva de diferentes abordagens para a taxa agregada de evasão. Essa delimitação também permite manter uma mesma unidade de análise em todos os experimentos.

## 2. Por que a validação não foi feita por divisão aleatória dos dados?

Porque o problema possui estrutura temporal. Uma divisão aleatória poderia colocar observações de períodos futuros no conjunto de treinamento de observações anteriores. Os protocolos Expanding Window e Rolling Window preservam a ordem cronológica e reproduzem de forma mais adequada uma situação em que o passado é utilizado para prever o futuro.

## 3. O que foi feito para evitar data leakage?

As variáveis preditoras de cada período são construídas com informações do período anterior. Além disso, cada fold utiliza somente períodos anteriores no treinamento, e transformações como a padronização da Ridge são ajustadas exclusivamente com os dados de treinamento. Os conjuntos de teste dos dois protocolos utilizam os mesmos períodos e as mesmas UFs.

## 4. Por que utilizar o baseline de persistência?

A persistência estabelece uma referência simples: prever a taxa atual como igual à taxa observada no período anterior. Assim, é possível verificar se os modelos supervisionados extraem informação adicional além da continuidade temporal do próprio indicador de evasão.

## 5. Por que comparar modelos lineares com modelos de árvores?

A comparação permite observar se relações lineares são suficientes para o conjunto de informações utilizado ou se modelos capazes de representar relações não lineares apresentam comportamento diferente. A escolha não pressupõe que modelos mais complexos necessariamente produzam melhor desempenho.

## 6. Por que a Regressão Ridge foi incluída além da Regressão Linear?

A Ridge acrescenta regularização L2 aos coeficientes e pode reduzir efeitos de multicolinearidade e instabilidade quando os preditores carregam informação semelhante. Ela fornece uma alternativa linear regularizada para comparação com a regressão sem regularização.

## 7. Por que o Cenário B tem tantas variáveis de evasão desagregadas?

O objetivo foi testar se informações históricas mais detalhadas sobre a própria evasão acrescentam capacidade preditiva à informação agregada. As variáveis representam taxas de evasão de grupos definidos pela fonte, e não a composição demográfica da população estudantil.

## 8. O resultado do Cenário B significa que sexo, idade ou deficiência causam evasão?

Não. O estudo trabalha com taxas agregadas e avalia desempenho preditivo. Uma variável pode apresentar importância preditiva sem representar uma relação causal. Portanto, os resultados não permitem concluir que pertencer a um determinado grupo provoque maior ou menor evasão individual.

## 9. Por que o Gradient Boosting respondeu melhor à inclusão das variáveis desagregadas?

No experimento, a inclusão dessas informações reduziu o MAE e o RMSE do Gradient Boosting nos dois protocolos. Uma interpretação possível é que a maior capacidade do modelo de representar relações não lineares tenha permitido utilizar parte da informação adicional de maneira mais efetiva. Essa é uma interpretação compatível com os resultados, mas não uma demonstração causal do mecanismo.

## 10. O Cenário B melhorou todos os modelos?

Não. Esse é justamente um dos resultados importantes. O efeito das novas variáveis foi heterogêneo entre os modelos. No agregado, houve redução de erro para o Gradient Boosting, enquanto Regressão Linear, Ridge e Random Forest apresentaram aumento de MAE em relação ao Cenário A.

## 11. Então o Gradient Boosting foi o melhor modelo?

A conclusão do trabalho não deve ser apresentada dessa forma. O Gradient Boosting apresentou redução de erro associada à inclusão das variáveis desagregadas, especialmente em 2022–2023, mas o desempenho depende do cenário, do protocolo e do período. O estudo foi desenhado para comparar condições, e não para estabelecer um único modelo universalmente superior.

## 12. O que explica a importância da variável de evasão entre mulheres no Gradient Boosting?

Os resultados de importância indicam que essa variável teve contribuição preditiva consistente no modelo analisado. Entretanto, isso não permite interpretar a variável como causa da evasão. Ela representa a taxa histórica de evasão observada entre mulheres na UF, e sua importância pode refletir informação compartilhada com outras características e padrões temporais.

## 13. Por que algumas importâncias por permutação foram negativas?

Uma importância negativa significa que, naquele fold, embaralhar a variável não aumentou o erro e pode até ter produzido uma pequena redução do erro. Isso não deve ser interpretado como um efeito negativo ou causal da variável. Como cada teste possui apenas 27 observações, pequenas flutuações também podem influenciar essa medida.

## 14. Por que o R² de alguns modelos é negativo?

R² negativo pode ocorrer quando as previsões apresentam desempenho inferior à referência baseada na média dos valores observados no conjunto avaliado. Portanto, não significa que o modelo seja matematicamente inválido; indica que, naquele conjunto de teste, ele não explicou a variabilidade melhor que essa referência.

## 15. Por que os resultados de 2022–2023 chamam tanta atenção?

Porque nesse período a inclusão das variáveis desagregadas produziu uma alteração particularmente grande no Gradient Boosting. No protocolo Expanding, o MAE mudou em -0,4674 ponto em relação ao Cenário A, e 21 das 27 UFs apresentaram redução do erro absoluto. Isso também sustenta a hipótese de que o efeito das informações adicionais varia temporalmente.

## 16. O que o trabalho acrescenta à literatura?

A contribuição está principalmente no desenho comparativo. O estudo combina diferentes abordagens preditivas, dois protocolos temporais e dois conjuntos de informação sob os mesmos períodos de teste e métricas. Dessa forma, examina como o desempenho varia quando se altera o histórico de treinamento ou o nível de detalhamento das informações, sem alegar que modelos preditivos sejam inéditos na literatura sobre evasão.

## 17. Qual é a principal limitação do trabalho?

A principal limitação é a unidade de análise agregada e a janela temporal relativamente curta para modelagem. Cada fold possui 27 observações de teste e existem apenas três períodos out-of-sample. Isso limita a estabilidade de algumas métricas e impede generalizações para o risco individual dos estudantes.

## 18. O trabalho permite afirmar que um modelo funcionará melhor em períodos futuros?

Não. Os resultados permitem descrever o comportamento observado nos períodos avaliados. A variação temporal observada, especialmente no efeito do Cenário B, recomenda cautela ao extrapolar os resultados para períodos futuros.

## 19. Se a fonte tem dados desde 2010, por que a modelagem começa depois?

A janela comum foi determinada pela disponibilidade simultânea dos indicadores necessários para construir os cenários. Como os modelos utilizam informações do período anterior e precisam das quatro dimensões agregadas, a interseção temporal disponível para o experimento começa em 2017–2018.

## 20. Qual é a mensagem principal que você defenderia na apresentação?

A mensagem central é que o desempenho preditivo da evasão agregada depende da combinação entre modelo, histórico temporal e conjunto de informações. O enriquecimento das variáveis pode alterar o desempenho, mas não produz uma melhoria uniforme. Por isso, avaliações preditivas desse tipo devem respeitar a ordem temporal e comparar diferentes configurações sob condições controladas.
