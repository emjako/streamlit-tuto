import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging

# Configuration du logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def load_data():
    logger.info("Chargement des données...")
    # Génération de données sinusoïdales
    x_values = np.linspace(0, 10, 100)
    y_values = np.sin(x_values)
    data = pd.DataFrame({'x': x_values, 'y': y_values})
    logger.info("Données chargées avec succès")
    return data

def create_plot(data):
    # Création d'une figure avec matplotlib
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'])
    ax.set_title("Courbe sinusoïdale")
    ax.set_xlabel("x")
    ax.set_ylabel("sin(x)")
    return fig

def main():
    st.title("Mon Application Streamlit")
    st.write("Bienvenue dans ce tutoriel Streamlit complet !")
    
    # Chargement et affichage des données
    data = load_data()
    st.write("Données générées :")
    st.dataframe(data)
    
    # Création et affichage de la datavisualisation
    fig = create_plot(data)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
