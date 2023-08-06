import pandas as pd
import streamlit as st
import umap
from sklearn.decomposition import PCA

from vectory.vectory.main import match_query

GREEN = "#f5fff6"
RED = "#fadedc"


@st.cache
def umap_calc(embeddings):
    return umap.UMAP(n_components=2, n_jobs=-1).fit_transform(embeddings)


@st.cache
def pca_calc(embeddings):
    return PCA(n_components=2).fit_transform(embeddings)


@st.cache
def pca_plus_umap_calc(embeddings):
    pca_points = PCA(n_components=50).fit_transform(embeddings)
    return umap.UMAP(n_components=2, n_jobs=-1).fit_transform(pca_points)


@st.cache(allow_output_mutation=True)
def calculate_points(model, embeddings, rows):
    if model == "UMAP":
        dim_2_points = umap_calc(embeddings)
    elif model == "PCA":
        dim_2_points = pca_calc(embeddings)
    elif model == "PCA + UMAP":
        dim_2_points = pca_plus_umap_calc(embeddings)

    metadata = {}
    for rowl in rows:
        for key in rowl:
            aux = metadata.get(key, [])
            aux.append(rowl[key])
            metadata[key] = aux

    data = {
        "d1": dim_2_points[:, 0],
        "d2": dim_2_points[:, 1],
    }
    data = data | metadata
    df = pd.DataFrame(data=data)

    return df


def format(index):
    if index is not None:
        return f"{index.name} ({index.model} ,{index.similarity})"
    return None


def color_positive_green(df):
    if df.coincidence:
        color = GREEN
    else:
        color = RED
    return [f"background-color: {color}"] * len(df)


def map_coincidence(val):
    if val <= 0.1:
        return "<0.1"
    elif val <= 0.2:
        return "<0.2"
    elif val <= 0.3:
        return "<0.3"
    elif val <= 0.4:
        return "<0.4"
    elif val <= 0.5:
        return "<0.5"
    elif val <= 0.6:
        return "<0.6"
    elif val <= 0.7:
        return "<0.7"
    elif val <= 0.8:
        return "<0.8"
    elif val <= 0.9:
        return "<0.9"
    elif val <= 1.0:
        return "<1.0"


def calculate_indices(selected_vector, index):
    results, _ = match_query(indices_name=[index.name], query_id=selected_vector)
    knn_indices, scores = list(zip(*results[list(results)[0]]))
    return knn_indices, scores
