# TCC — Evasão no Ensino Superior

Projeto de TCC sobre **evasão nas instituições de ensino superior**, desenvolvido no formato **Tipo B — Validação de solução**.

O trabalho investiga, por meio de um protocolo experimental temporal, diferentes abordagens de modelagem para previsão da taxa de evasão nas unidades federativas brasileiras e compara o efeito da ampliação do conjunto de variáveis preditoras.

---

## 1. Objetivo do projeto

O projeto busca produzir evidências sobre o desempenho de diferentes métodos de previsão da evasão no ensino superior, considerando:

- comparação entre modelos lineares e não lineares;
- validação temporal sem uso de informação futura;
- comparação entre estratégias **Expanding Window** e **Rolling Window**;
- análise do comportamento dos erros ao longo do tempo;
- comparação entre um cenário com indicadores agregados e outro enriquecido com informações desagregadas da evasão;
- análise exploratória da importância das variáveis no modelo Gradient Boosting.

O desenho foi motivado, entre outros pontos, pela intenção de explorar **diversificação metodológica** em relação à predominância de técnicas tradicionais observada na literatura sobre evasão.

---

## 2. Formato de entrega

O trabalho segue o formato:

> **Tipo B — Validação de solução**

A estrutura experimental procura estabelecer explicitamente:

1. critério de avaliação;
2. baseline;
3. dados e amostra;
4. métricas;
5. análise de erros;
6. implicações dos resultados.

A revisão de literatura permanece como requisito transversal do trabalho.

---

## 3. Fonte dos dados

Os dados utilizados são provenientes dos **Indicadores de Fluxo da Educação Superior disponibilizados pelo INEP**, especificamente a base por Unidade da Federação (`INDIC_UF_2010_2024.xlsx`).

Foram utilizadas as informações dos indicadores:

- `TX_EVASAO`;
- `TX_CONCLUSAO`;
- `TX_RETENCAO`;
- `TX_PERMANENCIA`.

A unidade observacional da base analítica é:

> **UF × período de fluxo**.

A base final contém **27 UFs** e, após a construção das variáveis defasadas e exclusão das primeiras observações sem histórico anterior, **189 observações**, correspondentes a 7 períodos de fluxo.

---

## 4. Estrutura do projeto

```text
tcc-evasao-ensino-superior/
│
├── data/
│   ├── raw/
│   │   └── INDIC_UF_2010_2024.xlsx
│   │
│   └── processed/
│       ├── base_modelo_uf.csv
│       └── base_modelo_uf_cenario_b.csv
│
├── notebooks/
│   ├── 01_construcao_base_uf.ipynb
│   ├── 01b_construcao_cenario_b.ipynb
│   ├── 02_protocolo_validacao.ipynb
│   ├── 03_comparacao_modelos.ipynb
│   ├── 04_comparacao_cenario_b.ipynb
│   ├── 05_comparacao_cenarios.ipynb
│   └── 06_interpretabilidade_cenario_b.ipynb
│
├── results/
│   └── tables/
│       ├── resultados_cenario_a.csv
│       ├── resultados_cenario_b.csv
│       ├── resultados_por_fold_cenario_a.csv
│       ├── resultados_por_fold_cenario_b.csv
│       ├── previsoes_gb_cenario_a_expanding.csv
│       ├── previsoes_gb_cenario_b_expanding.csv
│       ├── importancias_gb_cenario_b_expanding.csv
│       ├── comparacao_cenarios_detalhada.csv
│       ├── resumo_efeito_cenario_b.csv
│       └── resumo_gb_efeito_importancias.csv
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── validation.py
│   ├── evaluation.py
│   └── interpretation.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 5. Construção da base

### Cenário A

O primeiro conjunto experimental utiliza quatro variáveis preditoras, todas defasadas em um período:

```text
evasao_t_1
conclusao_t_1
retencao_t_1
permanencia_t_1
```

O alvo é:

```text
evasao_t
```

A utilização de `t-1` foi adotada para evitar que informações do próprio período de teste sejam utilizadas na previsão.

### Cenário B

O segundo cenário amplia o conjunto de preditores para **17 variáveis**, mantendo as quatro variáveis agregadas do Cenário A e acrescentando taxas de evasão defasadas segundo:

- sexo;
- PPI;
- faixa etária;
- deficiência.

As 13 novas variáveis são:

```text
evasao_feminino_t_1
evasao_masculino_t_1

evasao_ppi_sim_t_1
evasao_ppi_nao_t_1

evasao_ate_19_t_1
evasao_20_22_t_1
evasao_23_24_t_1
evasao_25_29_t_1
evasao_30_39_t_1
evasao_40_49_t_1
evasao_50_mais_t_1

evasao_deficiencia_sim_t_1
evasao_deficiencia_nao_t_1
```

A base do Cenário B também possui **189 observações**, **27 UFs** e **23 colunas** no total.

---

## 6. Validação temporal

Foram definidos dois protocolos:

### Expanding Window

O treinamento incorpora todo o histórico disponível antes do período de teste.

### Rolling Window

O treinamento utiliza uma janela fixa de quatro períodos anteriores ao período de teste.

Os dois protocolos utilizam exatamente os mesmos períodos de teste:

```text
2021–2022
2022–2023
2023–2024
```

Cada conjunto de teste possui as mesmas **27 UFs**.

As validações implementadas verificam que:

- nenhum período futuro é incluído no treinamento;
- os dois protocolos utilizam os mesmos períodos de teste;
- cada conjunto de teste contém 27 UFs;
- as estruturas dos folds são consistentes.

---

## 7. Modelos avaliados

O benchmark atual contém cinco abordagens:

1. **Persistência** — baseline em que a previsão de `t` é a taxa de evasão observada em `t-1`;
2. **Regressão Linear**;
3. **Regressão Ridge**;
4. **Random Forest Regressor**;
5. **Gradient Boosting Regressor**.

Os modelos supervisionados são treinados novamente em cada fold temporal.

A Ridge utiliza padronização dentro de um `Pipeline`, garantindo que o ajuste do scaler ocorra apenas com os dados de treinamento de cada fold.

---

## 8. Métricas

São utilizadas três métricas:

- **MAE** — erro absoluto médio;
- **RMSE** — raiz do erro quadrático médio;
- **R²** — coeficiente de determinação.

Além das métricas agregadas, são analisados:

- resultados por fold;
- erros absolutos por UF e período;
- direção dos erros (`real - previsão`);
- comportamento dos erros por faixa da taxa observada de evasão;
- efeito da inclusão das novas features do Cenário B.

---

## 9. Resultados já obtidos — Cenário A

Resultados agregados atuais:

| Modelo | Protocolo | MAE | RMSE | R² |
|---|---|---:|---:|---:|
| Persistência | Expanding | 1.9840 | 2.5240 | -0.2399 |
| Persistência | Rolling | 1.9840 | 2.5240 | -0.2399 |
| Regressão Linear | Expanding | 1.5891 | 2.1761 | 0.0783 |
| Regressão Linear | Rolling | 1.5988 | 2.1127 | 0.1312 |
| Ridge | Expanding | 1.5823 | 2.1419 | 0.1071 |
| Ridge | Rolling | 1.6214 | 2.1102 | 0.1333 |
| Random Forest | Expanding | 1.7317 | 2.2991 | -0.0288 |
| Random Forest | Rolling | 1.7138 | 2.2549 | 0.0104 |
| Gradient Boosting | Expanding | 1.8782 | 2.4053 | -0.1261 |
| Gradient Boosting | Rolling | 1.8422 | 2.3523 | -0.0770 |

O baseline de persistência apresentou MAE de aproximadamente **1.984**.

As abordagens lineares apresentaram os menores erros agregados no Cenário A, enquanto os modelos baseados em árvores não apresentaram ganho equivalente sobre as abordagens lineares.

---

## 10. Comportamento dos erros

Na análise do Expanding Window, foram observadas evidências de que o erro absoluto tende a aumentar quando a taxa observada de evasão é maior.

Para a Ridge, a correlação entre a taxa de evasão observada e o erro absoluto foi aproximadamente:

```text
0.4658
```

As correlações correspondentes observadas foram:

```text
Persistência       0.3336
Ridge              0.4658
Random Forest      0.5319
Gradient Boosting  0.5195
```

A análise por tercis da taxa de evasão indicou aumento do erro absoluto nas observações do tercil superior para todos os métodos.

Também foi observado um padrão de direção do erro: as previsões tendem a se aproximar de uma faixa intermediária, com maior ocorrência de erros negativos em níveis mais baixos de evasão e de erros positivos em níveis mais altos. Esse comportamento é tratado como padrão preditivo observado, e não como efeito causal.

---

## 11. Comparação Cenário A × Cenário B

O Cenário B adicionou 13 variáveis desagregadas às quatro variáveis agregadas do Cenário A.

O efeito dessa inclusão não foi uniforme entre os modelos.

### Principais resultados observados

- **Persistência:** não muda, pois não utiliza as novas variáveis.
- **Regressão Linear:** efeito misto; não houve melhoria consistente nos dois protocolos.
- **Ridge:** efeito misto; pequenas melhorias em algumas métricas/protocolos e pioras em outras.
- **Random Forest:** piora consistente do MAE nos dois protocolos.
- **Gradient Boosting:** redução do MAE médio nos dois protocolos, além de redução de RMSE e aumento de R².

No Gradient Boosting, o efeito temporal mostrou que o principal ganho ocorreu em **2022–2023**. No Expanding Window:

```text
2021–2022 → ΔMAE = +0.1404
2022–2023 → ΔMAE = -0.4674
2023–2024 → ΔMAE = -0.0020
```

No Rolling Window:

```text
2021–2022 → ΔMAE = +0.1404
2022–2023 → ΔMAE = -0.3270 (aprox.)
2023–2024 → ΔMAE = +0.02 (aprox.)
```

Portanto, a melhoria agregada observada para o Gradient Boosting não deve ser interpretada como uma melhoria uniforme em todos os períodos.

---

## 12. Interpretabilidade do Cenário B

A análise de interpretabilidade foi realizada no **Gradient Boosting** utilizando o protocolo Expanding Window.

Foram utilizadas duas abordagens:

1. importância interna do modelo;
2. **Permutation Importance** calculada nos conjuntos de teste dos folds.

Entre as variáveis com maior importância média por permutação destacaram-se:

```text
1. evasao_feminino_t_1
2. evasao_20_22_t_1
3. evasao_ate_19_t_1
4. evasao_ppi_nao_t_1
5. permanencia_t_1
```

A variável `evasao_feminino_t_1` apresentou o comportamento mais consistente entre os folds:

```text
2021–2022 → 0.1152
2022–2023 → 0.1443
2023–2024 → 0.1708
```

e foi positiva nos três folds.

Já `evasao_20_22_t_1` apresentou importância média elevada, mas maior variação temporal:

```text
2021–2022 → 0.1841
2022–2023 → 0.1380
2023–2024 → -0.0003
```

A interpretação dessas importâncias é **preditiva e exploratória**, não causal. A análise deve ser interpretada com cautela devido ao pequeno tamanho dos conjuntos de teste (27 UFs por período) e à possibilidade de correlação entre variáveis desagregadas.

---

## 13. Próxima etapa do projeto

A próxima etapa prevista é concluir a análise do efeito do Cenário B sobre o **Gradient Boosting em nível de UF**, verificando se o ganho observado em 2022–2023 foi distribuído entre várias unidades federativas ou concentrado em poucos casos.

Depois disso, o projeto deverá avançar para a consolidação dos resultados, discussão das ameaças à validade e preparação da documentação final do TCC.

---

## 14. Reprodutibilidade

O projeto foi estruturado para execução em **VS Code**, utilizando ambiente virtual Python e notebooks Jupyter/Colab por meio da extensão do VS Code.

As funções reutilizáveis foram separadas em módulos Python dentro de `src/` para evitar duplicação de código e facilitar a reprodução dos experimentos.

Os notebooks possuem responsabilidades separadas:

- `01_construcao_base_uf.ipynb` — construção da base principal;
- `01b_construcao_cenario_b.ipynb` — construção da base ampliada;
- `02_protocolo_validacao.ipynb` — definição e validação dos folds temporais;
- `03_comparacao_modelos.ipynb` — experimento do Cenário A;
- `04_comparacao_cenario_b.ipynb` — experimento do Cenário B;
- `05_comparacao_cenarios.ipynb` — comparação A × B;
- `06_interpretabilidade_cenario_b.ipynb` — análise de importância das variáveis.

Resultados intermediários e tabelas são exportados para `results/tables/`.

---

## 15. Estado atual

**Status:** experimento principal em desenvolvimento.

Já concluído:

- construção e validação da base por UF;
- construção das variáveis temporais e `t-1`;
- definição dos protocolos Expanding e Rolling;
- baseline de persistência;
- comparação dos cinco modelos;
- construção e avaliação do Cenário B;
- comparação A × B;
- análise inicial de erros;
- análise inicial de interpretabilidade do Gradient Boosting;
- organização do projeto em notebooks e módulos Python;
- versionamento do projeto em repositório GitHub.

Em andamento:

- análise do efeito do Cenário B por UF;
- consolidação dos resultados e discussão metodológica;
- preparação da apresentação e documentação final.
