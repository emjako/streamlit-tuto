import pytest
import pandas as pd
from app import generate_data, page_home, page_visualisation, page_analysis, page_settings

# Import de streamlit pour pouvoir remplacer ses fonctions durant les tests
import streamlit as st

@pytest.fixture(autouse=True)
def disable_streamlit_functions(monkeypatch):
    # Remplacer les fonctions d'affichage de Streamlit par des fonctions factices pour éviter les erreurs
    monkeypatch.setattr(st, 'title', lambda x: None)
    monkeypatch.setattr(st, 'write', lambda x: None)
    monkeypatch.setattr(st, 'header', lambda x: None)
    monkeypatch.setattr(st, 'subheader', lambda x: None)
    monkeypatch.setattr(st, 'dataframe', lambda x: None)
    monkeypatch.setattr(st, 'pyplot', lambda x: None)
    monkeypatch.setattr(st, 'line_chart', lambda x: None)
    monkeypatch.setattr(st, 'scatter_chart', lambda x: None)
    monkeypatch.setattr(st, 'success', lambda x: None)
    monkeypatch.setattr(st, 'info', lambda x: None)
    monkeypatch.setattr(st, 'markdown', lambda x: None)
    monkeypatch.setattr(st, 'checkbox', lambda x: False)
    monkeypatch.setattr(st, 'button', lambda x: False)
    monkeypatch.setattr(st, 'slider', lambda label, min_value, max_value, value: value)
    
    # Simuler la sidebar de Streamlit
    dummy_sidebar = type('DummySidebar', (), {})()
    dummy_sidebar.title = lambda x: None
    dummy_sidebar.radio = lambda label, options: options[0]
    monkeypatch.setattr(st, 'sidebar', dummy_sidebar)
    
    # Initialiser st.session_state comme dictionnaire vide
    monkeypatch.setattr(st, 'session_state', {})

def test_generate_data():
    """Vérifie que la fonction generate_data retourne un DataFrame correct."""
    data = generate_data(50, noise=0.1)
    assert isinstance(data, pd.DataFrame)
    assert 'x' in data.columns
    assert 'y' in data.columns
    assert len(data) == 50

def test_page_home_runs():
    """Teste que la page d'accueil s'exécute sans erreur."""
    page_home()

def test_page_visualisation_runs():
    """Teste que la page de visualisation s'exécute sans erreur."""
    page_visualisation()

def test_page_analysis_runs():
    """Teste que la page d'analyse s'exécute sans erreur."""
    page_analysis()

def test_page_settings_runs():
    """Teste que la page des paramètres s'exécute sans erreur."""
    page_settings()
