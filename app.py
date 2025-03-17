import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging

# Configuration du logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def generate_data(n=100, noise=0.1):
    """Génère des données sinusoïdales avec bruit."""
    logger.info(f"Génération de données avec n={n} et noise={noise}")
    x = np.linspace(0, 10, n)
    y = np.sin(x) + np.random.normal(0, noise, size=n)
    df = pd.DataFrame({'x': x, 'y': y})
    logger.info("Données générées avec succès")
    return df

# Page d'accueil
def page_home():
    st.title("Accueil")
    st.write("Bienvenue dans l'application Streamlit avancée !")
    st.markdown("Utilisez la barre latérale pour naviguer entre les pages.")

    # Boutons d'action sur la page d'accueil
    if st.button("Afficher un message de bienvenue"):
        st.success("Bienvenue dans votre application Streamlit avancée !")
    if st.button("Générer de nouvelles données"):
        st.session_state['data'] = generate_data(n=200, noise=0.05)
        st.info("Nouvelles données générées et stockées dans l'état de l'application.")

# Page de visualisation
def page_visualisation():
    st.title("Visualisation de données")
    st.write("Explorez différentes visualisations interactives.")

    # Vérifier si des données existent déjà, sinon en générer par défaut
    if 'data' not in st.session_state:
        st.session_state['data'] = generate_data()

    data = st.session_state['data']
    
    # Bouton pour afficher les données brutes
    if st.button("Afficher les données brutes"):
        st.subheader("Données brutes")
        st.dataframe(data)

    # Bouton pour afficher un graphique Matplotlib
    if st.button("Afficher graphique Matplotlib"):
        fig, ax = plt.subplots()
        ax.plot(data['x'], data['y'], label="Données")
        ax.set_title("Graphique Matplotlib")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        st.pyplot(fig)

    # Bouton pour afficher un graphique interactif avec Streamlit
    if st.button("Afficher graphique interactif"):
        st.subheader("Graphique interactif")
        st.line_chart(data.set_index('x'))

    # Checkbox pour re-générer les données
    if st.checkbox("Re-générer les données"):
        st.session_state['data'] = generate_data()
        st.success("Données re-générées !")

# Page d'analyse
def page_analysis():
    st.title("Analyse des données")
    st.write("Réalisez des analyses statistiques sur les données.")

    if 'data' not in st.session_state:
        st.session_state['data'] = generate_data()
    data = st.session_state['data']

    # Bouton pour afficher des statistiques descriptives
    if st.button("Afficher statistiques descriptives"):
        st.subheader("Statistiques descriptives")
        st.write(data.describe())

    # Bouton pour effectuer une régression linéaire simple
    if st.button("Afficher régression linéaire"):
        coeffs = np.polyfit(data['x'], data['y'], deg=1)
        poly_eq = np.poly1d(coeffs)
        st.write("Coefficients de régression :", coeffs)
        fig, ax = plt.subplots()
        ax.scatter(data['x'], data['y'], label="Données")
        ax.plot(data['x'], poly_eq(data['x']), color='red', label="Régression linéaire")
        ax.set_title("Analyse de régression")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        st.pyplot(fig)

    # Bouton pour afficher un nuage de points
    if st.button("Afficher dispersion des données"):
        st.subheader("Nuage de points")
        st.scatter_chart(data)

# Page des paramètres
def page_settings():
    st.title("Paramètres")
    st.write("Ajustez les paramètres de génération des données.")

    # Slider pour ajuster le nombre de points et le niveau de bruit
    n = st.slider("Nombre de points", 50, 500, 100)
    noise = st.slider("Niveau de bruit", 0.0, 1.0, 0.1)

    if st.button("Mettre à jour les données"):
        st.session_state['data'] = generate_data(n=n, noise=noise)
        st.success("Données mises à jour avec succès !")

def main():
    st.sidebar.title("Navigation")
    # Navigation entre plusieurs pages
    page = st.sidebar.radio("Aller à", ["Accueil", "Visualisation", "Analyse", "Paramètres"])
    
    if page == "Accueil":
        page_home()
    elif page == "Visualisation":
        page_visualisation()
    elif page == "Analyse":
        page_analysis()
    elif page == "Paramètres":
        page_settings()

if __name__ == '__main__':
    main()
