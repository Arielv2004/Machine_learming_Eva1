from kedro.pipeline import Pipeline, node
from .nodes import clean_movies_metadata, merge_movies_credits, process_ratings

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=clean_movies_metadata,
                inputs="movies_metadata",
                outputs="movies_cleaned",
                name="clean_movies_metadata_node"
            ),
            node(
                func=merge_movies_credits,
                inputs=["movies_cleaned", "credits"],
                outputs="movies_full",
                name="merge_movies_credits_node"
            ),
            node(
                func=process_ratings,
                inputs="ratings",
                outputs="ratings_processed",
                name="process_ratings_node"
            ),
        ]
    )
