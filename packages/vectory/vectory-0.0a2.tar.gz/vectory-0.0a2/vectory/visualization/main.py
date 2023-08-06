import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from bokeh.models import CategoricalColorMapper, ColumnDataSource, CustomJS, HoverTool
from bokeh.palettes import RdYlBu10, turbo
from bokeh.plotting import figure
from PIL import Image, ImageOps
from streamlit_bokeh_events import streamlit_bokeh_events

from vectory.db.bulk import KNNBulkOperations
from vectory.db.models import Dataset, ElasticSearchIndex, EmbeddingSpace
from vectory.es.utils import load_csv_with_headers, load_embeddings_from_numpy
from vectory.visualization.utils import (
    calculate_indices,
    calculate_points,
    color_positive_green,
    map_coincidence,
)

img = Image.open("icon.png")
mask = Image.open("mask.png").convert("L")
icon = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
icon.putalpha(mask)
keys = iter([i for i in range(50)])

st.set_page_config(page_title="Vectory", page_icon=icon, layout="wide")


def selection(dataset):
    embedding_spaces = [
        emb_space.name
        for emb_space in EmbeddingSpace.select().where(
            EmbeddingSpace.dataset == dataset
        )
    ]
    selected_emb_space = st.selectbox(
        "Choose which embedding space you want to analyse",
        [None] + embedding_spaces,
        key=next(keys),
    )
    embeddings = None
    rows = None
    index = None
    model = None
    similarity = None
    selected_vector = None
    headers = []
    embedding_space_name = None
    if selected_emb_space is not None:
        embedding_space = EmbeddingSpace.get(name=selected_emb_space)
        embedding_space_name = embedding_space.name
        embeddings = load_embeddings_from_numpy(embedding_space.npz_path)
        rows, _, headers = load_csv_with_headers(embedding_space.dataset.csv_path)

    model = st.selectbox(
        "Choose a model to use for embedding kNN search",
        ["lsh", "exact"],
        key=next(keys),
    )
    similarity = st.selectbox(
        "Choose a similarity function to use for kNN search",
        ["cosine", "l2"],
        key=next(keys),
    )
    label = st.selectbox(
        "Choose a label to color the data points",
        [None] + ["coincidence"] + headers,
        key=next(keys),
    )
    dimensional_reduction_model = st.selectbox(
        "Choose which a model to do the dimensional reduction",
        ["UMAP", "PCA", "PCA + UMAP"],
        key=next(keys),
    )

    radius = st.slider(
        "Select plotted points radius",
        min_value=0.001,
        max_value=0.1,
        step=0.001,
        value=0.006,
        format="%.3f",
        key=next(keys),
    )

    if selected_emb_space is not None and dimensional_reduction_model is not None:
        index = ElasticSearchIndex.select().where(
            ElasticSearchIndex.embedding_space == embedding_space,
            ElasticSearchIndex.model == model,
            ElasticSearchIndex.similarity == similarity,
        )
        try:
            index = next(iter(index))
        except StopIteration:
            st.warning(
                "There isn't any loaded index from the embedding space"
                + f"'{embedding_space.name}', with model: '{model}'"
                + f"and similarity: '{similarity}'"
            )
            st.stop()

    return (
        dimensional_reduction_model,
        embeddings,
        rows,
        index,
        radius,
        label,
        selected_vector,
        similarity,
        embedding_space_name,
    )


def show_embedding_space(df, index, radius, label):
    if label == "coincidence" and "coincidence" not in (df.columns):
        label = None
    if label is not None:
        source = ColumnDataSource(data=dict(x=[], y=[], label=[]))

        source.data = dict(
            x=df.d1.tolist(),
            y=df.d2.tolist(),
            label=df[f"{label}"].tolist(),
        )

        labels = df[f"{label}"].unique().tolist()
        if label == "coincidence":
            labels = [
                "<0.1",
                "<0.2",
                "<0.3",
                "<0.4",
                "<0.5",
                "<0.6",
                "<0.7",
                "<0.8",
                "<0.9",
                "<1.0",
            ]
            palette = RdYlBu10
        else:
            n_colors = len(labels)
            palette = turbo(n_colors)

        color_mapper = CategoricalColorMapper(factors=labels, palette=palette)

        p_1 = figure(
            title="Embedding spaces plot",
            x_axis_label="d1",
            y_axis_label="d2",
            tools="tap, box_zoom, wheel_zoom ,zoom_out,reset",
        )

        p_1.circle(
            x="x",
            y="y",
            source=source,
            radius=radius,
            alpha=0.6,
            selection_color="red",
            color={"field": "label", "transform": color_mapper},
            nonselection_color="grey",
            legend_field="label",
        )

        source.selected.js_on_change(
            "indices",
            CustomJS(
                args=dict(source=source),
                code="""
        document.dispatchEvent(
            new CustomEvent("Selection", {detail: {indices: cb_obj.indices}})
        )
        source_2.selected.indices = source.selected.indices;
        source_2.change.emit();
        """,
            ),
        )
    else:
        st.text(label)
        source = ColumnDataSource(data=dict(x=[], y=[]))

        source.data = dict(
            x=df.d1.tolist(),
            y=df.d2.tolist(),
        )

        p_1 = figure(
            title="Embedding spaces plot",
            x_axis_label="d1",
            y_axis_label="d2",
            tools="tap, box_zoom, wheel_zoom ,zoom_out,reset",
        )

        p_1.circle(
            x="x",
            y="y",
            source=source,
            radius=radius,
            alpha=0.6,
            selection_color="red",
            nonselection_color="grey",
        )

        source.selected.js_on_change(
            "indices",
            CustomJS(
                args=dict(source=source),
                code="""
        document.dispatchEvent(
            new CustomEvent("Selection", {detail: {indices: cb_obj.indices}})
        )
        source_2.selected.indices = source.selected.indices;
        source_2.change.emit();
        """,
            ),
        )

    event_result = streamlit_bokeh_events(
        events="Selection",
        bokeh_plot=p_1,
        key=next(keys),
        debounce_time=100,
        refresh_on_update=False,
    )

    if event_result is not None and (
        event_result["Selection"].get("indices", []) != []
    ):
        #  if more than one index is selected, take the first one
        selected_vector = df.iloc[event_result["Selection"].get("indices", [])[0]][
            index.embedding_space.dataset.id_field
        ]
    else:
        selected_vector = None
    return selected_vector


def show_query(
    df, selected_vector, index, most_similar_indices, scores, other_space_ids
):
    radius = 0.02
    st.subheader("Selected Points summary:")

    selected_vector_df = df.loc[
        df[str(index.embedding_space.dataset.id_field)] == selected_vector
    ]
    most_similar_indices_df = df.loc[
        df[f"{index.embedding_space.dataset.id_field}"].isin(most_similar_indices)
    ]
    most_similar_indices_df["scores"] = scores
    most_similar_indices_df["coincidence"] = df.apply(
        lambda row: row[index.embedding_space.dataset.id_field] in other_space_ids,
        axis=1,
    )

    st.text("Most similar indices")
    most_similar_indices_df_styled = most_similar_indices_df.copy()
    most_similar_indices_df_styled.drop(["d1", "d2"], inplace=True, axis=1)
    most_similar_indices_df_styled = most_similar_indices_df_styled.style.apply(
        color_positive_green, axis=1
    )

    st.table(most_similar_indices_df_styled)

    grey_points = ColumnDataSource(data=dict(x=[], y=[]))

    p_2 = figure(
        title="Embedding spaces plot",
        x_axis_label="d1",
        y_axis_label="d2",
        tools="box_zoom, wheel_zoom ,zoom_out,reset",
    )
    grey_points.data = dict(
        x=df.d1.tolist(),
        y=df.d2.tolist(),
    )

    p_2.circle(
        x="x",
        y="y",
        source=grey_points,
        radius=radius,
        color="gray",
        alpha=0.2,
    )

    most_similar_points = ColumnDataSource(
        data=dict(
            x=most_similar_indices_df.d1.tolist(),
            y=most_similar_indices_df.d2.tolist(),
            id=most_similar_indices_df[
                f"{index.embedding_space.dataset.id_field}"
            ].tolist(),
        )
    )

    p_2.circle(
        x="x",
        y="y",
        source=most_similar_points,
        color="red",
        radius=radius,
        name="most_similar_indices",
    )

    selected_vector = ColumnDataSource(
        data=dict(
            x=selected_vector_df.d1.tolist(),
            y=selected_vector_df.d2.tolist(),
            id=selected_vector_df[f"{index.embedding_space.dataset.id_field}"].tolist(),
        )
    )

    p_2.circle(
        x="x",
        y="y",
        source=selected_vector,
        color="green",
        radius=radius,
        name="selected_index",
    )
    hover = HoverTool(
        names=["selected_index", "most_similar_indices"],
        tooltips=[
            ("id", "@id"),
        ],
    )
    grey_points.selected.js_on_change(
        "indices",
        CustomJS(
            args=dict(
                source=grey_points,
            ),
            code="""
        grey_points.change.emit()
        document.dispatchEvent(
            new CustomEvent("Selection_2", {detail: {indices: cb_obj.indices}})
        )
        """,
        ),
    )
    p_2.add_tools(hover)
    streamlit_bokeh_events(
        events="Selection_2",
        bokeh_plot=p_2,
        key=next(keys),
        debounce_time=100,
        refresh_on_update=False,
    )


def main():
    st.title("ESA: Embedding Spaces Analysis")

    dataset = st.selectbox(
        "Choose a dataset:", [None] + [dataset.name for dataset in Dataset.select()]
    )

    col1, col2 = st.columns(2)

    if dataset is not None:
        dataset = Dataset.select().where(Dataset.name == dataset)
        with col1:
            (
                dimensional_reduction_model_1,
                embeddings_1,
                rows_1,
                index_1,
                radius_1,
                label_1,
                selected_vector_1,
                similarity_1,
                embedding_space_1_name,
            ) = selection(dataset)
        with col2:
            (
                dimensional_reduction_model_2,
                embeddings_2,
                rows_2,
                index_2,
                radius_2,
                label_2,
                selected_vector_2,
                similarity_2,
                embedding_space_2_name,
            ) = selection(dataset)

        if "submit" not in st.session_state:
            st.session_state.submit = False
        submit = st.button("Submit")
        if submit:
            st.session_state.submit = True

        if st.session_state.submit:

            df_1 = calculate_points(dimensional_reduction_model_1, embeddings_1, rows_1)
            df_2 = calculate_points(dimensional_reduction_model_2, embeddings_2, rows_2)

            knn = []
            try:
                knn = KNNBulkOperations(embedding_space_1_name).space_similarity(
                    embedding_space_1_name,
                    "euclidean",
                    embedding_space_2_name,
                    "euclidean",
                )
                assert knn != {}
                knn_class = [map_coincidence(i) for i in knn.values()]
                df_1["coincidence"] = knn_class
                df_2["coincidence"] = knn_class
            except AssertionError:
                if "coincidence" in df_1.columns:
                    df_1.drop(["coincidence"], inplace=True, axis=1)
                if "coincidence" in df_2.columns:
                    df_2.drop(["coincidence"], inplace=True, axis=1)
                st.warning(
                    "Attention: in order to see the knn coincidence histogram and use"
                    + "the coincidence as a color label"
                    + ", please calculate the space similarity first"
                )

            if "selected_vector" not in st.session_state:
                st.session_state.selected_vector = None
            selected_vec_1_changed = False
            with col1:
                selected_vector_1 = show_embedding_space(
                    df_1, index_1, radius_1, label_1
                )
                if selected_vector_1 == st.session_state.selected_vector:
                    selected_vec_1_changed = False
                else:
                    selected_vec_1_changed = True
                    st.session_state.selected_vector = selected_vector_1
                st.write(f"Selected point id: {selected_vector_1}")
            with col2:
                selected_vector_2 = show_embedding_space(
                    df_2, index_2, radius_2, label_2
                )
                if selected_vector_2 is not None and not selected_vec_1_changed:
                    st.session_state.selected_vector = selected_vector_2
                selected_vec_1_changed = False
                st.write(f"Selected point id: {selected_vector_2}")

            if knn != []:
                coincidence_range = np.arange(0.0, 1.1, 0.1)
                bar_heights, _ = np.histogram(list(knn.values()), coincidence_range)
                bins = [
                    "<0.1",
                    "<0.2",
                    "<0.3",
                    "<0.4",
                    "<0.5",
                    "<0.6",
                    "<0.7",
                    "<0.8",
                    "<0.9",
                    "<1.0",
                ]
                df = pd.DataFrame(
                    {
                        "Frecuency": bar_heights / len(knn),
                        "IoU": bins,
                    }
                )

                value_color_mapping = zip(bins, RdYlBu10)
                fig = px.bar(
                    df,
                    x="IoU",
                    y="Frecuency",
                    color="IoU",
                    color_discrete_map=dict(value_color_mapping),
                )

                st.plotly_chart(fig, use_container_width=True)

            if (
                df_1 is not None
                and index_1 is not None
                and df_2 is not None
                and index_2 is not None
            ):
                selected_vector = st.selectbox(
                    "Select an index to query",
                    [st.session_state.selected_vector]
                    + [
                        id for id in df_1[f"{index_1.embedding_space.dataset.id_field}"]
                    ],
                    key=next(keys),
                )
            show = st.button("Match query")

            if show:
                most_similar_indices_1, scores_1 = calculate_indices(
                    selected_vector, index_1
                )
                most_similar_indices_2, scores_2 = calculate_indices(
                    selected_vector, index_2
                )
                intersection = set(most_similar_indices_1) & set(most_similar_indices_1)
                if df_1 is not None:
                    with col1:
                        show_query(
                            df_1,
                            selected_vector,
                            index_1,
                            most_similar_indices_1,
                            scores_1,  # , intersection
                            most_similar_indices_2,
                        )
                if df_2 is not None:
                    with col2:
                        show_query(
                            df_2,
                            selected_vector,
                            index_2,
                            most_similar_indices_2,
                            scores_2,  # , intersection
                            most_similar_indices_1,
                        )


if __name__ == "__main__":
    main()
