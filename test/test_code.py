import os
import pytest
import pandas as pd
from spotify_project.loader import MusicLoader

def test_file_exists():
    """ Check if the data file is actually in the folder """
    base_path = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(base_path, 'data', 'spotify_data.csv')
    assert os.path.exists(filepath) == True

def test_loader_load_dataframe():
    """ Check if the loader actually creates a DataFrame """
    loader = MusicLoader("spotify_data.csv")
    loader.load()
    assert loader.df is not None
    assert isinstance(loader.df, pd.DataFrame)