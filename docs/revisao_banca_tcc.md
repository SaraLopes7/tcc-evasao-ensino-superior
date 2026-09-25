# Revisão de integração e leitura de banca — TCC Evasão no Ensino Superior

## 1. Situação geral

A documentação apresenta coerência entre problema de pesquisa, objetivos, hipóteses, metodologia, resultados, discussão e conclusão. A unidade de análise está delimitada de forma consistente como UF × período, e o texto distingue adequadamente previsão de taxa agregada de evasão de previsão de risco individual de estudantes.

O desenho experimental também está coerente entre os capítulos: dois cenários de variáveis, dois protocolos temporais, cinco abordagens de previsão e três períodos de teste.

## 2. Correções realizadas nesta revisão

### 2.1 Metodologia

Foram corrigidos problemas de estrutura que poderiam comprometer a apresentação acadêmica:

- numeração irregular de subseções, como “3.61”, “3.81” e “3.141”, substituída pela hierarquia convencional “3.6.1”, “3.8.1” e “3.14.1”;
- trecho duplicado na descrição da estrutura do experimento removido;
- referências a nomes internos de arquivos e identificadores de variáveis retiradas do texto corrido;
- descrição do Cenário B convertida para linguagem acadêmica, preservando as dimensões efetivamente utilizadas;
- PPI definido como pretos, pardos e indígenas;
- termos em inglês reduzidos ou apresentados apenas quando úteis à terminologia metodológica;
- hiperparâmetros mantidos apenas quando contribuem para a reprodutibilidade do experimento;
- descrição dos controles de vazamento de dados preservada sem transformar a seção em documentação de código.

### 2.2 Fundamentação teórica

A revisão passou a explicitar melhor a conexão entre os trabalhos brasileiros já levantados e o desenho do estudo. Foram incorporadas referências que já faziam parte da matriz de literatura, incluindo Saccaro, França e Jacinto (2019), Rosa, Milani e Santos (2021), Nierotka, Salata e Klitzke (2023) e Vitelli e Fritsch (2016).

Também foi mantida a distinção entre associação estatística, previsão e causalidade.

### 2.3 Referências

A referência de Tinto (1975), citada na fundamentação, foi incluída na bibliografia. As referências de Breiman (2001), Friedman (2001) e Hoerl e Kennard (1970) passaram a ser citadas na metodologia, vinculando cada modelo à sua referência metodológica.

A edição de 2012 de Tinto, que não estava sendo citada no texto principal, foi retirada da lista final para evitar referências sem uso explícito.

### 2.4 Resultados e discussão

Os identificadores técnicos de variáveis foram substituídos, sempre que possível, por descrições em linguagem natural, como “taxa de evasão entre mulheres no período anterior” e “taxa de evasão entre estudantes de 20 a 22 anos no período anterior”. Isso preserva a precisão dos resultados sem dar ao capítulo aparência de saída de notebook.

## 3. Pontos que a banca provavelmente poderá questionar

### 3.1 Por que a unidade de análise é UF × período?

A resposta está na própria delimitação do trabalho: o objetivo é prever uma taxa agregada de evasão e comparar estratégias preditivas em escala federativa, não estimar o risco individual de estudantes.

### 3.2 Por que utilizar apenas sete períodos-alvo?

A limitação decorre da interseção temporal necessária entre os quatro indicadores utilizados e da construção das defasagens. O texto já registra essa limitação e evita apresentar o número reduzido de períodos como característica ideal do desenho.

### 3.3 Por que não realizar tuning extensivo dos modelos?

A escolha foi manter hiperparâmetros previamente definidos para preservar condições comuns de comparação. Isso deve ser apresentado como uma decisão experimental, e não como afirmação de que os hiperparâmetros utilizados sejam ótimos.

### 3.4 Por que comparar modelos tão diferentes?

Porque a pergunta não é somente qual algoritmo produz determinada métrica, mas como abordagens lineares e não lineares se comportam quando submetidas aos mesmos períodos, variáveis, métricas e protocolos temporais.

### 3.5 O Cenário B realmente representa características demográficas?

Não no sentido de composição da população. O Cenário B utiliza taxas históricas de evasão desagregadas por grupos. Essa distinção precisa ser mantida durante a apresentação oral para evitar interpretação individual ou causal.

### 3.6 A importância das variáveis permite afirmar que determinado grupo causa mais evasão?

Não. A importância é interpretada exclusivamente como relevância preditiva dentro do modelo e da amostra avaliados.

## 4. Pontos para a montagem do documento final

Ainda falta a etapa editorial do TCC propriamente dito:

1. aplicar o modelo de formatação exigido pela instituição;
2. inserir capa, folha de rosto, resumo, abstract e sumário;
3. transformar as tabelas em tabelas numeradas e padronizadas;
4. inserir as figuras realmente necessárias, evitando gráficos meramente decorativos;
5. revisar chamadas de tabelas e figuras no texto;
6. fazer a conferência final entre citações e referências;
7. revisar paginação, títulos, espaçamento e referências segundo o manual institucional.

## 5. Veredito da revisão de integração

Não foi identificada contradição metodológica substantiva entre os capítulos. Os principais problemas encontrados eram de apresentação, terminologia e integração bibliográfica, e foram corrigidos nesta rodada.

O experimento continua descrito exatamente como realizado: 189 observações na base final, 27 UFs, sete períodos-alvo, três períodos de teste, dois protocolos temporais, dois cenários de variáveis e cinco abordagens de previsão.

A documentação está pronta para ser incorporada ao manuscrito principal, restando a adaptação às normas da instituição e a revisão final de banca.
