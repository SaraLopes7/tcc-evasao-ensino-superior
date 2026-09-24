import pandas as pd

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)
from sklearn.linear_model import Ridge
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

FEATURES = [
    "evasao_t_1",
    "conclusao_t_1",
    "retencao_t_1",
    "permanencia_t_1"
]

TARGET = "evasao_t"


def calcular_metricas(y_true, y_pred):
    """
    Calcula as métricas utilizadas no experimento.
    """

    mae = mean_absolute_error(
        y_true,
        y_pred
    )

    rmse = mean_squared_error(
        y_true,
        y_pred
    ) ** 0.5

    r2 = r2_score(
        y_true,
        y_pred
    )

    return {
        "mae": mae,
        "rmse": rmse,
        "r2": r2
    }


def avaliar_persistencia(df, folds):
    """
    Avalia o baseline de persistência.

    A previsão para t é igual à taxa de evasão observada
    em t-1.
    """

    resultados = []
    previsoes = []

    for fold in folds:

        periodo_teste = fold["periodo_teste"]

        teste = df[
            df["ano_inicio"] == periodo_teste
        ].copy()

        y_true = teste[TARGET]
        y_pred = teste["evasao_t_1"]

        metricas = calcular_metricas(
            y_true,
            y_pred
        )

        resultados.append({
            "fold": fold["fold"],
            "periodo_teste": periodo_teste,
            **metricas,
            "n_teste": len(teste)
        })

        resultado_teste = teste[
            ["uf", "ano_fluxo", TARGET]
        ].copy()

        resultado_teste["previsao"] = y_pred
        resultado_teste["erro"] = (
            resultado_teste[TARGET]
            - resultado_teste["previsao"]
        )
        resultado_teste["erro_abs"] = (
            resultado_teste["erro"].abs()
        )
        resultado_teste["fold"] = fold["fold"]

        previsoes.append(
            resultado_teste
        )

    resultados = pd.DataFrame(
        resultados
    )

    previsoes = pd.concat(
        previsoes,
        ignore_index=True
    )

    metricas_gerais = calcular_metricas(
        previsoes[TARGET],
        previsoes["previsao"]
    )

    return (
        resultados,
        previsoes,
        metricas_gerais
    )


def avaliar_modelo(
    df,
    folds,
    modelo,
    features=None
):
    """
    Avalia um modelo supervisionado nos folds temporais fornecidos.

    Parâmetros
    ----------
    df : pandas.DataFrame
        Base de dados utilizada no experimento.

    folds : list[dict]
        Folds temporais previamente definidos.

    modelo : callable
        Função que cria e retorna um modelo novo.

    features : list[str] | None
        Lista de variáveis preditoras.
        Quando None, utiliza as features padrão do Cenário A.

    Retorna
    -------
    resultados : pandas.DataFrame
        Métricas por fold.

    previsoes : pandas.DataFrame
        Previsões e erros por observação.

    metricas_gerais : dict
        Métricas agregadas sobre todas as previsões out-of-sample.
    """

    if features is None:
        features = FEATURES

    resultados = []
    previsoes = []

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
        y_treino = treino[TARGET]

        X_teste = teste[features]
        y_teste = teste[TARGET]

        modelo_fold = modelo()

        modelo_fold.fit(
            X_treino,
            y_treino
        )

        y_pred = modelo_fold.predict(
            X_teste
        )

        metricas = calcular_metricas(
            y_teste,
            y_pred
        )

        resultados.append({
            "fold": fold["fold"],
            "periodo_teste": periodo_teste,
            **metricas,
            "n_treino": len(treino),
            "n_teste": len(teste)
        })

        resultado_teste = teste[
            ["uf", "ano_fluxo", TARGET]
        ].copy()

        resultado_teste["previsao"] = y_pred

        resultado_teste["erro"] = (
            resultado_teste[TARGET]
            - resultado_teste["previsao"]
        )

        resultado_teste["erro_abs"] = (
            resultado_teste["erro"].abs()
        )

        resultado_teste["fold"] = fold["fold"]

        previsoes.append(
            resultado_teste
        )

    resultados = pd.DataFrame(
        resultados
    )

    previsoes = pd.concat(
        previsoes,
        ignore_index=True
    )

    metricas_gerais = calcular_metricas(
        previsoes[TARGET],
        previsoes["previsao"]
    )

    return (
        resultados,
        previsoes,
        metricas_gerais
    )


def criar_ridge(alpha=1.0):
    """
    Cria o modelo Ridge com padronização.
    """

    return Pipeline([
        (
            "scaler",
            StandardScaler()
        ),
        (
            "ridge",
            Ridge(alpha=alpha)
        )
    ])


def criar_random_forest(
    n_estimators=300,
    min_samples_leaf=3,
    random_state=42
):
    """
    Cria o modelo Random Forest com configuração fixa.
    """

    return RandomForestRegressor(
        n_estimators=n_estimators,
        min_samples_leaf=min_samples_leaf,
        random_state=random_state,
        n_jobs=-1
    )


def criar_gradient_boosting(
    n_estimators=100,
    learning_rate=0.05,
    max_depth=2,
    min_samples_leaf=3,
    random_state=42
):
    """
    Cria o modelo Gradient Boosting com configuração fixa.
    """

    return GradientBoostingRegressor(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        max_depth=max_depth,
        min_samples_leaf=min_samples_leaf,
        random_state=random_state
    )

def criar_linear_regression():
    """
    Cria o modelo de Regressão Linear sem regularização.
    """
    return LinearRegression()