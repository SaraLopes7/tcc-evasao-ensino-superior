def criar_folds_temporais(
    df,
    estrategia,
    tamanho_treino=4
):
    """
    Cria folds de validação temporal para dados em painel UF x período.

    Parâmetros
    ----------
    df : pandas.DataFrame
        Base contendo a coluna 'ano_inicio'.
    estrategia : str
        'expanding' ou 'rolling'.
    tamanho_treino : int
        Quantidade de períodos utilizados para treinamento.

    Retorna
    -------
    list[dict]
        Lista contendo a definição de cada fold.
    """

    if estrategia not in {"expanding", "rolling"}:
        raise ValueError(
            "A estratégia deve ser 'expanding' ou 'rolling'."
        )

    periodos = sorted(
        df["ano_inicio"].unique()
    )

    if len(periodos) <= tamanho_treino:
        raise ValueError(
            "Não existem períodos suficientes para criar os folds."
        )

    folds = []

    for teste_idx in range(
        tamanho_treino,
        len(periodos)
    ):

        periodo_teste = periodos[teste_idx]

        if estrategia == "expanding":

            indices_treino = range(
                0,
                teste_idx
            )

        else:  # rolling

            inicio = teste_idx - tamanho_treino

            indices_treino = range(
                inicio,
                teste_idx
            )

        periodos_treino = [
            periodos[i]
            for i in indices_treino
        ]

        treino = df[
            df["ano_inicio"].isin(periodos_treino)
        ]

        teste = df[
            df["ano_inicio"] == periodo_teste
        ]

        folds.append({
            "fold": len(folds) + 1,
            "periodos_treino": periodos_treino,
            "periodo_teste": periodo_teste,
            "n_treino": len(treino),
            "n_teste": len(teste),
            "ufs_treino": treino["uf"].nunique(),
            "ufs_teste": teste["uf"].nunique()
        })

    return folds