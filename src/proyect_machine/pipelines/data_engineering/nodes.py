import pandas as pd
import numpy as np
import ast

# ---- Selección de variables relevantes ----
def seleccionar_variables(movies_metadata: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "id", "title", "budget", "revenue", "runtime",
        "release_date", "popularity", "vote_count", "vote_average", "genres"
    ]
    return movies_metadata[cols]

# ---- Limpieza de datos ----
def limpiar_datos(movies_metadata: pd.DataFrame) -> pd.DataFrame:
    df = movies_metadata.copy()

    # Convertir release_date a datetime
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df["release_year"] = df["release_date"].dt.year

    # Reemplazar valores nulos numéricos por 0
    for col in ["budget", "revenue", "runtime", "vote_count", "vote_average", "popularity"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Eliminar duplicados
    df = df.drop_duplicates()

    return df

# ---- Feature Engineering: género principal ----
def agregar_main_genre(movies_metadata: pd.DataFrame) -> pd.DataFrame:
    df = movies_metadata.copy()

    def get_main_genre(genres):
        try:
            g = ast.literal_eval(genres)
            if g:
                return g[0]["name"]
        except:
            return None

    df["main_genre"] = df["genres"].apply(get_main_genre)
    return df

# ---- Integración con Credits ----
def integrar_credits(movies_metadata: pd.DataFrame, credits: pd.DataFrame) -> pd.DataFrame:
    # unir por id (cast y crew en texto)
    return movies_metadata.merge(credits, on="id", how="left")

# ---- Integración con Ratings ----
def integrar_ratings(movies_with_credits: pd.DataFrame, ratings: pd.DataFrame) -> pd.DataFrame:
    # ratings usa movieId, hay que mapear con id de movies
    # Convertir ambos a int para evitar errores
    movies_with_credits["id"] = pd.to_numeric(movies_with_credits["id"], errors="coerce")
    ratings["movieId"] = pd.to_numeric(ratings["movieId"], errors="coerce")

    # unión (left join: no todas las películas tienen rating)
    return movies_with_credits.merge(ratings, left_on="id", right_on="movieId", how="left")
