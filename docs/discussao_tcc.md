# 5 Discussão

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

O estudo também enfatiza a importância da validação temporal. Em problemas de previsão de fenômenos educacionais, o objetivo é estimar valores futuros a partir de informações disponíveis anteriormente. A separação temporal adotada busca aproximar esse cenário e evita que informações de períodos posteriores sejam utilizadas para prever períodos anteriores. Dessa forma, o desempenho reportado deve ser entendido como desempenho out-of-sample sob os períodos de teste especificados, e não como desempenho retrospectivo sobre toda a base.

## 5.9. Limitações e implicações para trabalhos futuros

A primeira limitação é o tamanho temporal da base efetivamente utilizada na modelagem. Embora o indicador de evasão tenha série mais longa, as variáveis auxiliares necessárias para os cenários avaliados estão disponíveis a partir de período mais recente, restringindo a janela comum de modelagem a sete períodos-alvo.

A segunda limitação decorre da unidade de análise. As observações representam UF × período, portanto os resultados descrevem padrões agregados e não permitem inferir comportamentos individuais de estudantes. Essa característica impede, por exemplo, interpretar a importância de uma taxa de evasão feminina como efeito individual do sexo sobre a probabilidade de evasão.

A terceira limitação está relacionada ao número de observações nos conjuntos de teste: 27 UFs por fold. Esse tamanho reduzido pode aumentar a sensibilidade das métricas e das medidas de interpretabilidade a casos específicos. A análise por período e por UF foi incluída justamente para reduzir o risco de interpretar apenas os resultados agregados.

A quarta limitação é que os modelos foram avaliados com configurações de hiperparâmetros definidas no protocolo experimental. O estudo não realizou uma busca exaustiva de hiperparâmetros nem uma comparação de técnicas adicionais de seleção de atributos. Assim, os resultados representam o desempenho das configurações especificadas, e não um limite máximo de desempenho que cada algoritmo poderia atingir.

Por fim, a análise não possui desenho causal. As associações encontradas entre variáveis desagregadas e desempenho preditivo indicam utilidade para a previsão no conjunto estudado, mas não permitem concluir que essas variáveis causem a evasão nem que intervenções sobre elas produziriam determinada alteração na taxa de evasão.

## 5.10. Síntese em relação às hipóteses

Considerando o conjunto dos resultados, H1 encontra suporte descritivo porque a alteração entre Expanding e Rolling produziu diferenças observáveis nas métricas de desempenho, ainda que pequenas e dependentes do modelo e da métrica. H2 também encontra suporte descritivo, uma vez que a inclusão das informações desagregadas alterou o desempenho em relação ao Cenário A, com efeitos distintos entre os métodos. H3 encontra suporte mais evidente, pois o efeito do Cenário B variou de forma substancial entre os períodos de teste, especialmente no Gradient Boosting.

Assim, as hipóteses não apontam para uma única configuração universalmente superior, mas para a existência de dependência entre estratégia temporal, conjunto de variáveis e momento da previsão. Esse resultado é central para a interpretação do experimento e reforça a necessidade de avaliar modelos preditivos de evasão sob protocolos que respeitem a estrutura temporal do problema.
