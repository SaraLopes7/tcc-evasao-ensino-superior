import pandas as pd


def preparar_indicador(
    arquivo,
    nome_aba,
    prefixo,
    possui_deficiencia=True,
    inicio_dados=8
):
    """Lê e padroniza uma aba dos Indicadores de Fluxo da Educação Superior."""

    df_raw = pd.read_excel(
        arquivo,
        sheet_name=nome_aba,
        header=None
    )

    colunas = [
        "ano_fluxo",
        "uf",
        f"{prefixo}_total",
        f"{prefixo}_feminino",
        f"{prefixo}_masculino",
        f"{prefixo}_ppi_sim",
        f"{prefixo}_ppi_nao",
        f"{prefixo}_ate_19",
        f"{prefixo}_20_22",
        f"{prefixo}_23_24",
        f"{prefixo}_25_29",
        f"{prefixo}_30_39",
        f"{prefixo}_40_49",
        f"{prefixo}_50_mais"
    ]

    if possui_deficiencia:
        colunas.extend([
            f"{prefixo}_deficiencia_sim",
            f"{prefixo}_deficiencia_nao"
        ])

    df = df_raw.iloc[inicio_dados:].copy()
    df.columns = colunas
    df["ano_fluxo"] = df["ano_fluxo"].ffill()
    df = df[df["uf"].notna()].copy()

    colunas_taxa = colunas[2:]
    df[colunas_taxa] = df[colunas_taxa].apply(
        pd.to_numeric,
        errors="coerce"
    )

    return df.reset_index(drop=True)