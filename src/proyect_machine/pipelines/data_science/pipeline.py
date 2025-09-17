from kedro.pipeline import Pipeline, node
from . import nodes

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=nodes.resumen_datos,
                inputs=["movies_metadata", "credits", "ratings"],
                outputs=["movies_metadata_eda", "credits_eda", "ratings_eda"],
                name="resumen_datos_node"
            ),
            node(
                func=nodes.agregar_genero_principal,
                inputs="movies_metadata_eda",
                outputs="movies_metadata_genre",
                name="agregar_genero_principal_node"
            ),
            node(
                func=nodes.visualizar_eda,
                inputs="movies_metadata_genre",
                outputs=None,
                name="visualizar_eda_node"
            )
        ]
    )
