import matplotlib.pyplot as plt
import pandas as pd
from loader import MusicLoader

def plot_top_songs():
    # Load data
    loader = MusicLoader("spotify_data.csv")
    loader.load()
    
    if loader.df is not None:
        print("Generating chart...")
        # Get top 5 longest songs
        top_songs = loader.df.sort_values(by='track_duration_min', ascending=False).head(5)
        
        # Make a bar chart
        plt.figure(figsize=(10, 5))
        plt.bar(top_songs['track_id'], top_songs['track_duration_min'], color='green')
        plt.title('Top 5 Longest Songs')
        plt.xlabel('Song ID')
        plt.ylabel('Minutes')
        plt.show()

if __name__ == "__main__":
    plot_top_songs()