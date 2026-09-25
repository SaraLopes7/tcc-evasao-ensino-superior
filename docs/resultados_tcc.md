# 4 Resultados

## 4.1. Caracterização da base experimental

A base final de modelagem foi composta por 189 observações, correspondentes a 27 unidades federativas brasileiras acompanhadas em sete períodos de fluxo, de 2017–2018 a 2023–2024. Para cada UF e período-alvo, a variável dependente corresponde à taxa de evasão no período corrente (evasao_t), enquanto as variáveis preditoras foram construídas a partir das informações do período anterior (t-1).

A avaliação preditiva foi realizada em três períodos de teste: 2021–2022, 2022–2023 e 2023–2024. Cada fold de teste contém 27 observações, uma para cada UF. Assim, os cinco métodos avaliados foram submetidos a três avaliações temporais em cada um dos dois protocolos e em cada um dos dois cenários, totalizando 20 combinações modelo–protocolo–cenário e 60 avaliações fold-modelo–protocolo–cenário.

O Cenário A utilizou quatro preditores agregados. O Cenário B manteve esses quatro preditores e incorporou 13 variáveis adicionais de evasão desagregadas por sexo, pertencimento ao grupo de pretos, pardos e indígenas (PPI), faixa etária e deficiência, totalizando 17 preditores.

## 4.2. Desempenho no Cenário A

A Tabela 1 apresenta o desempenho agregado das previsões *out-of-sample* do Cenário A, obtido pela concatenação das previsões dos três períodos de teste.

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

Esse resultado estabelece uma referência para interpretar os modelos supervisionados. Nas avaliações *out-of-sample* agregadas, as quatro abordagens supervisionadas apresentaram MAE inferior ao baseline de persistência nos dois protocolos.

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

Para aprofundar a avaliação, foram analisados os erros das previsões *out-of-sample* do Cenário A. No caso da Ridge, o erro foi definido como real − previsão, de modo que valores positivos indicam subestimação e valores negativos indicam superestimação.

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
