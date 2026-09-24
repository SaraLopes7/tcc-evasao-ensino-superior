import numpy as np
import pandas as pd

from sklearn.inspection import permutation_importance


def avaliar_importancia_gradient_boosting(
    df,
    folds,
    criar_modelo,
    features,
    target="evasao_t",
    n_repeats=20,
    random_state=42
):
    """
    Calcula dois tipos de importância para o Gradient Boosting:

    1. feature_importances_: importância interna do modelo;
    2. permutation importance: perda de desempenho ao embaralhar
       cada variável no conjunto de teste.

    O modelo é treinado separadamente em cada fold.
    """

    importancias_nativas = []
    importancias_permutacao = []

    for fold in folds:

        periodos_treino = fold["periodos_treino"]
        periodo_teste = fold["periodo_teste"]

        treino = df[
            df["ano_inicio"].isin(periodos_treino)
        ].copy()

        teste = df[
            df["ano_inicio"] == periodo_teste
        ].copy()

        X_treino = treino[features]
        y_treino = treino[target]

        X_teste = teste[features]
        y_teste = teste[target]

        modelo = criar_modelo()

        modelo.fit(
            X_treino,
            y_treino
        )

        # Importância interna
        importancias_nativas.append(
            pd.DataFrame({
                "feature": features,
                "importance": modelo.feature_importances_,
                "fold": fold["fold"],
                "periodo_teste": periodo_teste
            })
        )

        # Importância por permutação no conjunto de teste
        perm = permutation_importance(
            modelo,
            X_teste,
            y_teste,
            scoring="neg_mean_absolute_error",
            n_repeats=n_repeats,
            random_state=random_state,
            n_jobs=-1
        )

        importancias_permutacao.append(
            pd.DataFrame({
                "feature": features,
                "importance_mean": perm.importances_mean,
                "importance_std": perm.importances_std,
                "fold": fold["fold"],
                "periodo_teste": periodo_teste
            })
        )

    nativas = pd.concat(
        importancias_nativas,
        ignore_index=True
    )

    permutacao = pd.concat(
        importancias_permutacao,
        ignore_index=True
    )

    resumo_nativo = (
        nativas
        .groupby("feature")["importance"]
        .agg(
            media="mean",
            desvio_padrao="std"
        )
        .sort_values(
            "media",
            ascending=False
        )
        .reset_index()
    )

    resumo_permutacao = (
        permutacao
        .groupby("feature")
        .agg(
            media_importancia=(
                "importance_mean",
                "mean"
            ),
            desvio_padrao=(
                "importance_mean",
                "std"
            )
        )
        .sort_values(
            "media_importancia",
            ascending=False
        )
        .reset_index()
    )

    return (
        nativas,
        permutacao,
        resumo_nativo,
        resumo_permutacao
    )


def classificar_grupo_feature(feature):
    """
    Classifica uma feature do Cenário B por grupo conceitual.
    """

    if feature in {
        "evasao_t_1",
        "conclusao_t_1",
        "retencao_t_1",
        "permanencia_t_1"
    }:
        return "Histórico agregado"

    if feature in {
        "evasao_feminino_t_1",
        "evasao_masculino_t_1"
    }:
        return "Sexo"

    if feature in {
        "evasao_ppi_sim_t_1",
        "evasao_ppi_nao_t_1"
    }:
        return "PPI"

    if feature in {
        "evasao_ate_19_t_1",
        "evasao_20_22_t_1",
        "evasao_23_24_t_1",
        "evasao_25_29_t_1",
        "evasao_30_39_t_1",
        "evasao_40_49_t_1",
        "evasao_50_mais_t_1"
    }:
        return "Faixa etária"

    if feature in {
        "evasao_deficiencia_sim_t_1",
        "evasao_deficiencia_nao_t_1"
    }:
        return "Deficiência"

    return "Outros"