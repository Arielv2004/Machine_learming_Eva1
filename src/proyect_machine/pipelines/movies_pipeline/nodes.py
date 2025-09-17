import pandas as pd

def clean_movies_metadata(movies: pd.DataFrame) -> pd.DataFrame:
    """Limpieza básica de movies_metadata"""
    movies = movies.dropna(subset=['title', 'release_date'])
    return movies

def merge_movies_credits(movies: pd.DataFrame, credits: pd.DataFrame) -> pd.DataFrame:
    """Combina metadata con créditos"""
    return movies.merge(credits, left_on='id', right_on='movie_id', how='left')

def process_ratings(ratings: pd.DataFrame) -> pd.DataFrame:
    """Procesa ratings"""
    return ratings.groupby('movieId').mean().reset_index()
