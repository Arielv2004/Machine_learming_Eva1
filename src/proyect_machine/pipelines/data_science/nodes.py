import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

def resumen_datos(movies_metadata: pd.DataFrame, credits: pd.DataFrame, ratings: pd.DataFrame):
    """Muestra forma, nulos, duplicados y columnas"""
    print("Movies Metadata shape:", movies_metadata.shape)
    print("Credits shape:", credits.shape)
    print("Ratings shape:", ratings.shape)
    
    print("\nNulos Movies Metadata:\n", movies_metadata.isnull().sum())
    print("\nNulos Credits:\n", credits.isnull().sum())
    print("\nNulos Ratings:\n", ratings.isnull().sum())
    
    print("\nDuplicados Movies Metadata:", movies_metadata.duplicated().sum())
    print("Duplicados Credits:", credits.duplicated().sum())
    print("Duplicados Ratings:", ratings.duplicated().sum())
    
    return movies_metadata, credits, ratings


def agregar_genero_principal(movies_metadata: pd.DataFrame):
    """Extrae el primer género de la columna genres"""
    def get_main_genre(genres):
        try:
            g = ast.literal_eval(genres)
            if g: return g[0]['name']
        except: 
            return None
    movies_metadata['main_genre'] = movies_metadata['genres'].apply(get_main_genre)
    return movies_metadata


def visualizar_eda(movies_metadata: pd.DataFrame):
    """Genera gráficos de distribución"""
    # Votos por género
    votes_por_genero = movies_metadata.groupby('main_genre')['vote_count'].sum().reset_index()
    votes_por_genero = votes_por_genero.sort_values('vote_count', ascending=False)

    plt.figure(figsize=(12,6))
    sns.barplot(data=votes_por_genero, x='vote_count', y='main_genre', palette='viridis')
    plt.title('Cantidad de votos por género')
    plt.show()
    
    # Distribución de duración
    plt.figure(figsize=(12,6))
    plt.hist(movies_metadata['runtime'].dropna(), bins=50, color='coral', edgecolor='black')
    plt.title('Distribución de la duración de películas')
    plt.xlabel('Duración (minutos)')
    plt.ylabel('Cantidad de películas')
    max_runtime = int(movies_metadata['runtime'].dropna().max())
    plt.xticks(range(0, max_runtime+20, 20), rotation=45)
    plt.show()
    
    # Boxplot de calificaciones por género
    plt.figure(figsize=(14,6))
    sns.boxplot(data=movies_metadata, x='main_genre', y='vote_average', palette='Set3')
    plt.title('Distribución de calificaciones por género')
    plt.xticks(rotation=90)
    plt.show()
    
    return None
