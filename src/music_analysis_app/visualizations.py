import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

def plot_music_visualizations(df):
    """
    Crée des visualisations différentes pour analyser les données musicales Spotify.
    """

    # 1. Top 10 des Morceaux par Score de Popularité
    st.subheader("1. Top 10 des Morceaux par Score de Popularité")
    top_10_tracks = df[['track_name', 'popularity', 'album_name', 'artists', 'duration_ms', 'track_genre']] \
        .drop_duplicates(subset=['track_name']) \
        .sort_values(by='popularity', ascending=False).head(10)
    st.write(top_10_tracks)
    
    st.markdown("""
        Cette visualisation montre les 10 morceaux les plus populaires, 
        avec leurs détails comme le nom de l'album et de l'artiste, le genre et la durée.
    """)

    # 2. Top 10 des Artistes avec les Morceaux les Plus Populaires
    st.subheader("2. Top 10 des Artistes avec les Morceaux les Plus Populaires")
    top_10_artists = df.groupby('artists').agg({'popularity': 'mean'}).sort_values(by='popularity', ascending=False).head(10)
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top_10_artists, x='popularity', y=top_10_artists.index, palette='viridis', dodge=False)
    plt.title('Top 10 des Artistes avec les Morceaux les Plus Populaires')
    plt.xlabel('Popularité Moyenne des Morceaux')
    plt.ylabel('Nom de l\'Artiste')
    st.pyplot(fig2)

    # 3. Top 20 des Genres les Plus Populaires
    st.subheader("3. Top 20 des Genres les Plus Populaires")
    top_20_genres = df.groupby('track_genre').agg({'popularity': 'mean'}).sort_values(by='popularity', ascending=False).head(20)
    
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top_20_genres, x='popularity', y=top_20_genres.index, palette='viridis', dodge=False)
    plt.title('Top 20 des Genres les Plus Populaires')
    plt.xlabel('Popularité Moyenne des Morceaux')
    plt.ylabel('Genre Musical')
    st.pyplot(fig3)

    # 4. Distribution de la Popularité en Fonction de la Durée des Morceaux (Amélioré)
    st.subheader("4. Distribution de la Popularité en Fonction de la Durée des Morceaux")
    fig4, ax4 = plt.subplots(figsize=(12, 6))
    sns.scatterplot(
    data=df, 
    x='duration_ms', 
    y='popularity', 
    hue='popularity', 
    size='popularity',
    sizes=(20, 200), 
    palette='coolwarm', 
    alpha=0.7, 
    ax=ax4 )
    best_durations = df.groupby('duration_ms')['popularity'].mean().sort_values(ascending=False).head(3).index

    ax4.set_title("Relation entre Durée des Morceaux et Popularité")
    ax4.set_xlabel("Durée (ms)")
    ax4.set_ylabel("Popularité")
    ax4.legend(title="Popularité", loc='upper left', bbox_to_anchor=(1, 1))
    st.pyplot(fig4)
    st.markdown("""Cette image est un graphique de dispersion montrant la relation entre la durée des morceaux (en millisecondes) et leur popularité. Chaque point représente un morceau, avec sa position sur l\'axe horizontal indiquant sa durée et sur l\'axe vertical sa popularité. 
                La couleur des points varie selon un gradient, 
                du bleu (faible popularité) au rouge (forte popularité).
                Le graphique indique que les morceaux de durée courte ont tendance à être populaires.
                D’après ce graphique, on peut dire que les morceaux courts sont plus souvent populaires, mais il serait prudent d’analyser d'autres facteurs pour mieux comprendre les raisons derrière cette tendance.
                """)

    # 5. Heatmap des Corrélations entre les Caractéristiques
    st.subheader("5. Corrélations entre les Caractéristiques")
    numeric_columns = ['popularity', 'danceability', 'energy', 'loudness', 
                       'acousticness', 'instrumentalness', 'valence', 'tempo']
    correlation_matrix = df[numeric_columns].corr()
    fig5, ax5 = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f', ax=ax5)
    plt.title('Corrélations entre les Caractéristiques')
    st.pyplot(fig5)
    st.markdown("""Popularité indépendante des caractéristiques audio : La popularité pourrait être davantage influencée par des éléments externes 
                que par les attributs mesurés ici.
                Il est possible que des combinaisons complexes (comme "danceability" + "valence") influencent la popularité.
                """)

    st.markdown("""
        ### 📊 Insights Clés
- Une liste du Top 10 des Artistes et Chansons les Plus Populaires
- 🔥 Les morceaux courts ont tendance à être plus populaires, bien que la durée ne soit pas le seul facteur influençant leur succès.
- 🎵 Les caractéristiques "energy" et "loudness" sont fortement corrélées (**0.76**), indiquant que les morceaux plus bruyants sont souvent plus énergiques.
- 📉 La popularité montre des corrélations très faibles avec les caractéristiques audio, suggérant que des facteurs externes (comme le genre, la promotion ou l'artiste) jouent un rôle plus important.
""")

def update_main_for_viz():
    """
    La fonction à appeler dans main.py pour afficher toutes les visualisations
    """
    try:
        df = pd.read_csv('data/spotify_tracks_cleaned.csv')
        plot_music_visualizations(df)
    except Exception as e:
        st.error(f"Erreur lors du chargement ou de la visualisation des données : {str(e)}")
