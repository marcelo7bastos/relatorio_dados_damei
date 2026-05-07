from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

import pandas as pd


@dataclass(frozen=True)
class PoliticaMunicipalSpec:
    politica: str
    arquivo_csv: str
    coluna_valor: str
    titulo_mapa: str


POLITICAS_SPECS_PADRAO: list[PoliticaMunicipalSpec] = [
    PoliticaMunicipalSpec(
        politica="CAF",
        arquivo_csv="caf_municipio_tratado.csv",
        coluna_valor="ufpa",
        titulo_mapa="CAF — Top 3 municípios (UFPA)",
    ),
    PoliticaMunicipalSpec(
        politica="PRONAF",
        arquivo_csv="pronaf_atual_municipio_tratado.csv",
        coluna_valor="valor_total_contratos",
        titulo_mapa="PRONAF — Top 3 municípios (valor total dos contratos)",
    ),
    PoliticaMunicipalSpec(
        politica="Mais Alimentos",
        arquivo_csv="mais_alimentos_municipio_tratado.csv",
        coluna_valor="valor_total_contratos",
        titulo_mapa="Mais Alimentos — Top 3 municípios (valor total dos contratos)",
    ),
    PoliticaMunicipalSpec(
        politica="ATER",
        arquivo_csv="ater_atual_municipio_tratado.csv",
        coluna_valor="familias_com_ater_recebida_no_ano",
        titulo_mapa="ATER — Top 3 municípios (famílias com ATER recebida no ano)",
    ),
    PoliticaMunicipalSpec(
        politica="Garantia-Safra",
        arquivo_csv="garantia_safra_municipio_tratado.csv",
        coluna_valor="agricultores_com_pagamento_liberado",
        titulo_mapa="Garantia-Safra — Top 3 municípios (agricultores com pagamento liberado)",
    ),
    PoliticaMunicipalSpec(
        politica="PNCF",
        arquivo_csv="pncf_municipio_tratado.csv",
        coluna_valor="valor_liberado",
        titulo_mapa="PNCF — Top 3 municípios (valor liberado)",
    ),
    PoliticaMunicipalSpec(
        politica="PNRA - Reforma Agrária",
        arquivo_csv="pnra_municipio_tratado.csv",
        coluna_valor="total_numero_familias_pnra",
        titulo_mapa="PNRA — Top 3 municípios (total de famílias)",
    ),
]


def _normalizar_codigo_municipio(df: pd.DataFrame) -> pd.Series:
    """Retorna uma série 'codarea' (7 dígitos) a partir das colunas mais comuns."""
    candidatos = ["codarea", "cod_ibge_municipio", "cod_ibge"]
    for col in candidatos:
        if col in df.columns:
            serie = df[col].astype(str).str.replace(r"\.0$", "", regex=True).str.strip()
            # completa com zeros à esquerda (códigos IBGE de município são 7 dígitos)
            return serie.str.zfill(7)
    raise KeyError(f"Não foi possível encontrar código do município em colunas {candidatos}.")


def _coluna_nome_municipio(df: pd.DataFrame) -> str:
    for col in ["nome_municipio", "municipio", "nm_municipio"]:
        if col in df.columns:
            return col
    return "nome_municipio"


def valores_municipais_por_valor(
    df_municipio: pd.DataFrame,
    coluna_valor: str,
    filtro_uf: Optional[str] = None,
) -> pd.DataFrame:
    """Agrega (soma) o valor por município e devolve um DF (codarea, nome_municipio, valor)."""
    df = df_municipio.copy()
    if filtro_uf and "uf" in df.columns:
        df["uf"] = df["uf"].astype(str).str.strip().str.upper()
        df = df[df["uf"] == filtro_uf.upper()].copy()

    if df.empty:
        return pd.DataFrame(columns=["codarea", "nome_municipio", "valor"])

    nome_col = _coluna_nome_municipio(df)
    df["codarea"] = _normalizar_codigo_municipio(df)
    df[nome_col] = df[nome_col].astype(str).str.strip()

    if coluna_valor not in df.columns:
        raise KeyError(f"Coluna '{coluna_valor}' não encontrada. Colunas disponíveis: {sorted(df.columns)}")

    df[coluna_valor] = pd.to_numeric(df[coluna_valor], errors="coerce").fillna(0)

    agg = (
        df.groupby(["codarea", nome_col], as_index=False)
        .agg(valor=(coluna_valor, "sum"))
        .rename(columns={nome_col: "nome_municipio"})
    )
    return agg


def top3_municipios_por_valor(
    df_municipio: pd.DataFrame,
    coluna_valor: str,
    filtro_uf: Optional[str] = None,
) -> pd.DataFrame:
    """Calcula top 3 municípios por soma do valor."""
    return (
        valores_municipais_por_valor(df_municipio, coluna_valor, filtro_uf=filtro_uf)
        .sort_values("valor", ascending=False)
        .head(3)
        .reset_index(drop=True)
    )


def _carregar_malha_municipios_uf_geopandas(codigo_ibge_uf: int):
    import geopandas as gpd
    import json
    from urllib.request import urlopen

    url = (
        f"https://servicodados.ibge.gov.br/api/v2/malhas/{int(codigo_ibge_uf)}"
        "?resolucao=5&qualidade=4&formato=application/vnd.geo+json"
    )
    # Observação: em alguns ambientes (ex.: Windows + pyogrio), ler GeoJSON direto por URL pode falhar.
    # Fazemos download do GeoJSON e montamos o GeoDataFrame a partir de features.
    with urlopen(url) as resp:
        raw = resp.read()
    # IBGE pode responder com gzip mesmo sem cabeçalho exposto aqui.
    if raw[:2] == b"\x1f\x8b":
        import gzip

        raw = gzip.decompress(raw)
    payload = json.loads(raw.decode("utf-8"))
    gdf = gpd.GeoDataFrame.from_features(payload.get("features", []), crs="EPSG:4326")
    if "codarea" not in gdf.columns:
        raise ValueError(f"GeoDataFrame inesperado; colunas: {list(gdf.columns)}")
    gdf["codarea"] = gdf["codarea"].astype(str).str.strip().str.zfill(7)
    return gdf


def gerar_mapa_top3_municipios(
    *,
    codigo_ibge_uf: int,
    nome_uf: str,
    titulo: str,
    valores_municipais: pd.DataFrame,
    top3: pd.DataFrame,
    output_png: Path,
):
    """Gera um PNG com a malha municipal da UF com viridis apenas no top 3 e rótulos externos."""
    import matplotlib.pyplot as plt

    gdf = _carregar_malha_municipios_uf_geopandas(codigo_ibge_uf)
    output_png.parent.mkdir(parents=True, exist_ok=True)

    gdf = gdf.copy()
    valores = valores_municipais.copy()
    valores["codarea"] = valores["codarea"].astype(str).str.strip().str.zfill(7)
    valores["valor"] = pd.to_numeric(valores["valor"], errors="coerce").fillna(0)

    gdf = gdf.merge(valores[["codarea", "valor"]], on="codarea", how="left")
    gdf["valor"] = pd.to_numeric(gdf["valor"], errors="coerce").fillna(0)

    gdf["is_top3"] = False
    if not top3.empty:
        gdf.loc[gdf["codarea"].isin(top3["codarea"].astype(str)), "is_top3"] = True

    fig, ax = plt.subplots(1, 1, figsize=(8.2, 6.2), dpi=200)
    ax.set_axis_off()

    # Base em cinza para todos os municípios.
    gdf.plot(ax=ax, color="#E6E6E6", edgecolor="#BDBDBD", linewidth=0.2)

    # Viridis apenas para o top 3 (escala baseada nos próprios top 3).
    gdf_top = gdf[gdf["is_top3"]].copy()
    if not gdf_top.empty:
        vmin = float(gdf_top["valor"].min())
        vmax = float(gdf_top["valor"].max())
        if vmax == vmin:
            vmax = vmin + 1.0

        gdf_top.plot(
            ax=ax,
            column="valor",
            cmap="viridis",
            vmin=vmin,
            vmax=vmax,
            edgecolor="#0B2239",
            linewidth=0.6,
        )

        # Contorno extra para dar contraste.
        gdf_top.plot(ax=ax, facecolor="none", edgecolor="#111827", linewidth=0.9)

    ax.set_title(f"{titulo}\n{nome_uf}", fontsize=12)

    if top3.empty:
        ax.text(
            0.02,
            0.02,
            "Sem dados municipais suficientes para calcular top 3.",
            transform=ax.transAxes,
            fontsize=9,
            color="#333333",
            bbox=dict(facecolor="white", edgecolor="#DDDDDD", boxstyle="round,pad=0.25"),
        )
    else:
        # Texto (legenda) com município + valor.
        linhas = []
        for i, row in enumerate(top3.itertuples(index=False), start=1):
            valor = float(row.valor) if pd.notna(row.valor) else 0.0
            linhas.append(
                f"{i}. {row.nome_municipio}: {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            )
        ax.text(
            0.02,
            0.02,
            "Top 3:\n" + "\n".join(linhas),
            transform=ax.transAxes,
            fontsize=9,
            color="#333333",
            bbox=dict(facecolor="white", edgecolor="#DDDDDD", boxstyle="round,pad=0.25"),
        )

        # Rótulos externos com linha apontando ao município.
        if not gdf_top.empty:
            gdf_top["ponto"] = gdf_top.geometry.representative_point()
            top_map = top3.set_index("codarea")["nome_municipio"].to_dict()

            minx, miny, maxx, maxy = gdf.total_bounds
            dx = (maxx - minx) * 0.06
            dy = (maxy - miny) * 0.04
            offsets = [(-dx, dy), (dx, dy), (dx, -dy)]

            for i, row in enumerate(gdf_top.itertuples(index=False), start=0):
                nome = top_map.get(getattr(row, "codarea"), getattr(row, "codarea"))
                pt = getattr(row, "ponto")
                ox, oy = offsets[i % len(offsets)]
                ax.annotate(
                    text=str(nome),
                    xy=(pt.x, pt.y),
                    xytext=(pt.x + ox, pt.y + oy),
                    ha="center",
                    va="center",
                    fontsize=7.5,
                    color="#111827",
                    bbox=dict(facecolor="white", edgecolor="#E5E7EB", boxstyle="round,pad=0.15"),
                    arrowprops=dict(arrowstyle="-", color="#111827", lw=0.8, shrinkA=2, shrinkB=2),
                )

    fig.tight_layout()
    fig.savefig(output_png, bbox_inches="tight")
    plt.close(fig)


def gerar_mapas_top3_politicas(
    *,
    politicas_dir: Path,
    output_dir: Path,
    uf_sigla: str,
    codigo_ibge_uf: int,
    nome_uf: str,
    specs: Iterable[PoliticaMunicipalSpec] = POLITICAS_SPECS_PADRAO,
) -> list[Path]:
    """Gera mapas PNG para cada política e retorna a lista de caminhos gerados."""
    mapas_dir = output_dir / "mapas" / uf_sigla.upper()
    mapas_dir.mkdir(parents=True, exist_ok=True)

    gerados: list[Path] = []
    for spec in specs:
        caminho_csv = politicas_dir / spec.arquivo_csv
        if not caminho_csv.exists():
            continue

        df = pd.read_csv(caminho_csv, sep=";", encoding="utf-8-sig")
        valores_municipais = valores_municipais_por_valor(df, spec.coluna_valor, filtro_uf=uf_sigla)
        top3 = valores_municipais.sort_values("valor", ascending=False).head(3).reset_index(drop=True)
        output_png = mapas_dir / f"mapa_top3_{spec.politica.lower().replace(' ', '_').replace('-', '_')}.png"
        gerar_mapa_top3_municipios(
            codigo_ibge_uf=codigo_ibge_uf,
            nome_uf=nome_uf,
            titulo=spec.titulo_mapa,
            valores_municipais=valores_municipais,
            top3=top3,
            output_png=output_png,
        )
        gerados.append(output_png)

    return gerados

