# 🎓 TCC --- Evasão no Ensino Superior

> **Trabalho de Conclusão de Curso · Tipo B --- Validação de solução**

Projeto desenvolvido para investigar, de forma experimental e temporal,
diferentes abordagens preditivas para a **taxa de evasão no ensino
superior brasileiro**.

O trabalho utiliza dados dos **Indicadores de Fluxo da Educação Superior
do INEP** e compara modelos, protocolos de validação temporal e
diferentes conjuntos de variáveis preditoras.

------------------------------------------------------------------------

## 📌 Sobre o projeto

### 🎯 Objetivo

Avaliar comparativamente diferentes abordagens preditivas para a taxa de
evasão no ensino superior brasileiro, considerando:

-   📈 diferentes modelos preditivos;
-   ⏳ protocolos de validação temporal;
-   🔄 **Expanding Window** e **Rolling Window**;
-   🧩 diferentes conjuntos de variáveis preditoras;
-   📊 comportamento dos erros ao longo do tempo e entre UFs;
-   🔎 relevância preditiva das variáveis no Gradient Boosting.

### ❓ Pergunta de pesquisa

> **Em que medida diferentes abordagens preditivas apresentam
> desempenhos distintos na previsão da taxa de evasão no ensino superior
> brasileiro quando avaliadas por protocolos temporais, e qual é o
> efeito da incorporação de informações desagregadas da evasão sobre
> esse desempenho?**

------------------------------------------------------------------------

## 🗃️ Dados

Os dados são provenientes dos **Indicadores de Fluxo da Educação
Superior do INEP**, utilizando a base por Unidade da Federação:

`INDIC_UF_2010_2024.xlsx`

### Indicadores utilizados

-   `TX_EVASAO`
-   `TX_CONCLUSAO`
-   `TX_RETENCAO`
-   `TX_PERMANENCIA`

### 📍 Unidade de análise

> **UF × período de fluxo**

O trabalho **não estima o risco individual de evasão de estudantes**. O
alvo é a **taxa agregada de evasão** de uma UF em determinado período.

Após a construção das variáveis defasadas, a base de modelagem contém
**189 observações**, correspondentes a **27 UFs em 7 períodos-alvo**, de
2017--2018 a 2023--2024.

------------------------------------------------------------------------

## 🧪 Estrutura experimental

O experimento combina:

  Dimensão                  Quantidade
  ----------------------- ------------
  Cenários de variáveis              2
  Protocolos temporais               2
  Abordagens preditivas              5
  Períodos de teste                  3
  UFs por teste                     27

**Total: 20 condições experimentais e 60 avaliações modelo-fold.**

### 🟦 Cenário A --- Indicadores agregados

Quatro preditores referentes ao período anterior:

-   taxa de evasão;
-   taxa de conclusão;
-   taxa de retenção;
-   taxa de permanência.

### 🟪 Cenário B --- Informação agregada + desagregada

Mantém as quatro variáveis do Cenário A e acrescenta **13 taxas de
evasão desagregadas**, organizadas por:

-   👩 sexo;
-   🧑🏽 pertencimento a PPI (pretos, pardos e indígenas);
-   🎂 faixa etária;
-   ♿ deficiência.

O Cenário B possui **17 variáveis preditoras**.

> ⚠️ As informações adicionais representam **taxas de evasão dos
> grupos**, e não a composição demográfica da população estudantil.

------------------------------------------------------------------------

## ⏳ Validação temporal

Os dois protocolos utilizam os mesmos períodos de teste:

``` text
2021–2022
2022–2023
2023–2024
```

### 📈 Expanding Window

O treinamento incorpora **todo o histórico disponível** antes de cada
período de teste.

### 🔄 Rolling Window

O treinamento utiliza uma **janela fixa de quatro períodos**, que
desliza ao longo do tempo.

Em ambos os protocolos, a ordem temporal é preservada e nenhum período
futuro é utilizado no treinamento. As variáveis preditoras utilizam
informações de `t-1`.

------------------------------------------------------------------------

## 🤖 Modelos avaliados

  Modelo                     Papel
  -------------------------- ----------------------------
  📌 **Persistência**        Baseline
  📐 **Regressão Linear**    Modelo linear
  🛡️ **Regressão Ridge**     Modelo linear regularizado
  🌲 **Random Forest**       Modelo baseado em árvores
  🚀 **Gradient Boosting**   Modelo baseado em árvores

Os modelos supervisionados são treinados novamente em cada fold
temporal.

------------------------------------------------------------------------

## 📏 Métricas e análises

### Métricas

-   **MAE** --- erro absoluto médio;
-   **RMSE** --- raiz do erro quadrático médio;
-   **R²** --- coeficiente de determinação.

### Análises adicionais

-   🔍 análise por fold temporal;
-   🗺️ análise de erros por UF;
-   ↕️ direção dos erros;
-   📊 comportamento dos erros segundo a magnitude da evasão observada;
-   🆚 comparação entre Cenário A e Cenário B;
-   🔎 importância das variáveis no Gradient Boosting.

> A análise de importância representa **relevância preditiva**, sem
> inferências causais.

------------------------------------------------------------------------

## 📊 Principais resultados

### 🟦 Cenário A

  Modelo              Protocolo        MAE     RMSE        R²
  ------------------- ----------- -------- -------- ---------
  Persistência        Expanding     1,9840   2,5240   -0,2399
  Persistência        Rolling       1,9840   2,5240   -0,2399
  Regressão Linear    Expanding     1,5891   2,1761    0,0783
  Regressão Linear    Rolling       1,5988   2,1127    0,1312
  Ridge               Expanding     1,5823   2,1419    0,1071
  Ridge               Rolling       1,6214   2,1102    0,1333
  Random Forest       Expanding     1,7317   2,2991   -0,0288
  Random Forest       Rolling       1,7138   2,2549    0,0104
  Gradient Boosting   Expanding     1,8782   2,4053   -0,1261
  Gradient Boosting   Rolling       1,8422   2,3523   -0,0770

No conjunto avaliado, os métodos lineares apresentaram menores erros
agregados que os modelos baseados em árvores no Cenário A.

### 🟪 Cenário B

  Modelo              Protocolo        MAE     RMSE        R²
  ------------------- ----------- -------- -------- ---------
  Persistência        Expanding     1,9840   2,5240   -0,2399
  Persistência        Rolling       1,9840   2,5240   -0,2399
  Regressão Linear    Expanding     1,6713   2,1564    0,0949
  Regressão Linear    Rolling       1,7276   2,1426    0,1065
  Ridge               Expanding     1,6553   2,1557    0,0955
  Ridge               Rolling       1,6732   2,1042    0,1383
  Random Forest       Expanding     1,8504   2,3208   -0,0483
  Random Forest       Rolling       1,8628   2,3174   -0,0452
  Gradient Boosting   Expanding     1,7686   2,3054   -0,0345
  Gradient Boosting   Rolling       1,7867   2,3035   -0,0327

A inclusão das variáveis desagregadas alterou o desempenho dos métodos,
mas o efeito não foi uniforme.

No Gradient Boosting, houve redução do erro médio nos dois protocolos. O
efeito temporal mais expressivo ocorreu em **2022--2023**; em 2021--2022
ocorreu deterioração e, em 2023--2024, a diferença foi pequena.

### 🔎 Interpretabilidade

Na análise do Gradient Boosting com Expanding Window, a **taxa de evasão
entre mulheres no período anterior** apresentou a maior importância
média por permutação entre as variáveis desagregadas, seguida pela taxa
de evasão na faixa de 20--22 anos.

Essas importâncias representam **utilidade preditiva contextual**, e não
efeitos causais.

------------------------------------------------------------------------

## 🧠 Hipóteses

### H1 --- Protocolo temporal

A escolha entre Expanding Window e Rolling Window produz diferenças
mensuráveis no desempenho preditivo.

**Resultado:** houve diferenças observáveis, mas a magnitude e a direção
dependeram do modelo e da métrica.

### H2 --- Ampliação informacional

A inclusão de informações desagregadas modifica o desempenho preditivo
em relação ao cenário baseado apenas em indicadores agregados.

**Resultado:** a inclusão modificou as métricas, com efeitos distintos
entre os métodos.

### H3 --- Heterogeneidade temporal

O efeito do conjunto de variáveis não é necessariamente uniforme entre
os períodos de teste.

**Resultado:** houve variação relevante entre os períodos, especialmente
para o Gradient Boosting.

------------------------------------------------------------------------

## 📁 Estrutura do projeto

``` text
tcc-evasao-ensino-superior/
│
├── 📂 data/
│   ├── 📂 raw/
│   │   └── INDIC_UF_2010_2024.xlsx
│   └── 📂 processed/
│       ├── base_modelo_uf.csv
│       └── base_modelo_uf_cenario_b.csv
│
├── 📂 notebooks/
│   ├── 01_construcao_base_uf.ipynb
│   ├── 01b_construcao_cenario_b.ipynb
│   ├── 02_protocolo_validacao.ipynb
│   ├── 03_comparacao_modelos.ipynb
│   ├── 04_comparacao_cenario_b.ipynb
│   ├── 05_comparacao_cenarios.ipynb
│   └── 06_interpretabilidade_cenario_b.ipynb
│
├── 📂 results/
│   └── 📂 tables/
│
├── 📂 src/
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

------------------------------------------------------------------------

## 📚 Documentação acadêmica

-   📄 `tcc_final.md` --- manuscrito consolidado;
-   📝 `tcc_final_senac_pe.docx` --- versão editável formatada;
-   📕 `tcc_final_senac_pe.pdf` --- versão diagramada em PDF;
-   🔎 `revisao_banca_tcc.md` --- revisão crítica do manuscrito;
-   🎤 `perguntas_banca_tcc.md` --- preparação para apresentação e
    banca.

------------------------------------------------------------------------

## 🔁 Reprodutibilidade

O projeto foi desenvolvido em **VS Code**, utilizando ambiente virtual
Python e notebooks Jupyter pela extensão do VS Code.

As funções reutilizáveis foram organizadas em módulos Python dentro de
`src/`, reduzindo duplicação e facilitando a reprodução dos
experimentos.

  -----------------------------------------------------------------------------
  Notebook                                  Responsabilidade
  ----------------------------------------- -----------------------------------
  `01_construcao_base_uf.ipynb`             Construção da base principal

  `01b_construcao_cenario_b.ipynb`          Construção da base ampliada

  `02_protocolo_validacao.ipynb`            Definição e validação dos folds
                                            temporais

  `03_comparacao_modelos.ipynb`             Experimento do Cenário A

  `04_comparacao_cenario_b.ipynb`           Experimento do Cenário B

  `05_comparacao_cenarios.ipynb`            Comparação entre cenários

  `06_interpretabilidade_cenario_b.ipynb`   Análise de importância das
                                            variáveis
  -----------------------------------------------------------------------------

Os resultados intermediários e tabelas experimentais são exportados para
`results/tables/`.

------------------------------------------------------------------------

## ✅ Estado final

  Etapa                       Status
  --------------------------- --------------------------
  🧪 Projeto experimental     **Concluído**
  📚 Documentação acadêmica   **Consolidada**
  ✍️ Manuscrito               **Concluído e revisado**
  📄 DOCX                     **Gerado**
  📕 PDF                      **Gerado**
  🎤 Apresentação             **Preparada**

A etapa restante é exclusivamente institucional, caso necessária, como
preenchimento de orientador(a), ficha catalográfica, folha de aprovação,
ajustes específicos solicitados pela coordenação e preparação da
apresentação oral.

------------------------------------------------------------------------

::: {align="center"}
### 🎓 Trabalho de Conclusão de Curso

**Evasão no Ensino Superior Brasileiro**

*Validação temporal · Modelagem preditiva · Análise comparativa*
:::
