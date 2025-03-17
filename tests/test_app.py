import pytest
import pandas as pd
import numpy as np
from app import load_data, create_plot

def test_load_data():
    data = load_data()
    # Vérifier que le DataFrame n'est pas vide et possède les colonnes 'x' et 'y'
    assert isinstance(data, pd.DataFrame)
    assert 'x' in data.columns
    assert 'y' in data.columns
    assert not data.empty

def test_create_plot():
    # Créer des données de test
    x_values = np.linspace(0, 10, 100)
    y_values = np.sin(x_values)
    data = pd.DataFrame({'x': x_values, 'y': y_values})
    fig = create_plot(data)
    # Vérifier que la figure possède bien un titre attendu
    assert fig is not None
    assert fig.axes[0].get_title() == "Courbe sinusoïdale"
