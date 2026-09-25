# 2 Fundamentação teórica

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

