from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    seleccionar_variables,
    limpiar_datos,
    agregar_main_genre,
    integrar_credits,
    integrar_ratings,
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=seleccionar_variables,
            inputs="movies_metadata",
            outputs="movies_selected",
            name="seleccionar_variables_node",
        ),
        node(
            func=limpiar_datos,
            inputs="movies_selected",
            outputs="movies_clean",
            name="limpiar_datos_node",
        ),
        node(
            func=agregar_main_genre,
            inputs="movies_clean",
            outputs="movies_with_genre",
            name="agregar_main_genre_node",
        ),
        node(
            func=integrar_credits,
            inputs=["movies_with_genre", "credits"],
            outputs="movies_with_credits",
            name="integrar_credits_node",
        ),
        node(
            func=integrar_ratings,
            inputs=["movies_with_credits", "ratings"],
            outputs="movies_final",
            name="integrar_ratings_node",
        ),
    ])
