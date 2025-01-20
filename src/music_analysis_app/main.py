# main.py
import streamlit as st
import pandas as pd
from visualizations import update_main_for_viz

def main():
    # Configuration de la page
    st.set_page_config(
        page_title="Analyse Musicale Interactive",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Styles CSS
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 10em;
            font-weight: bold;
            color: #002855;
            text-align: center;
        }
        .sub-title {
            font-size: 1.2em;
            color: #003366;
            text-align: center;
            margin-top: -10px;
        }
        .image-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        .stButton button {
            background-color: #002855;
            color: white;
            font-size: 1.1em;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            border: none;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #004080;
        }
        .visualization-container {
            margin-top: 2rem;
            padding: 1rem;
            background-color: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image("spotify.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    # En-tête
    st.markdown('<p class="main-title">🎵 <b>Analyse Musicale Interactive</b></p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Plongez dans l\'univers des tendances musicales et révélez les styles qui boostent vos ventes au maximum !</p>', unsafe_allow_html=True)

    st.write("---")
    st.write("""
    Bienvenue ! Cette application vous permet de plonger dans les données musicales pour analyser 
    les genres populaires et les caractéristiques des morceaux (énergie, tempo, dansabilité, etc.).
    """)
    st.write("""
    **Notre objectif** : Aider les entreprises de production musicale à identifier les styles qui 
    captivent le public et génèrent le plus de ventes.
    """)

    # Initialiser l'état pour le contrôle d'affichage des visualisations
    if 'show_visualizations' not in st.session_state:
        st.session_state.show_visualizations = False

    # Bouton pour afficher/masquer les visualisations
    st.write('<div class="button-container">', unsafe_allow_html=True)
    if st.button("📊 Explorer les Visualisations"):
        st.session_state.show_visualizations = not st.session_state.show_visualizations
    st.write('</div>', unsafe_allow_html=True)

    # Afficher les visualisations si le bouton a été cliqué
    if st.session_state.show_visualizations:
        st.markdown("""
        <div class="visualization-container">
            <h2>📈 Tableau de bord des visualisations</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Lire directement le fichier CSV
        try:
            df = pd.read_csv('data/spotify_tracks_cleaned.csv')
            update_main_for_viz()
        except Exception as e:
            st.error(f"Erreur lors du chargement des données : {str(e)}")

    st.write("---")
    st.info("💡 **Astuce** : Utilisez le dashboard pour explorer les données et prendre des décisions éclairées !")

if __name__ == "__main__":
    main()
