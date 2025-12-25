import pandas as pd
import os

class MusicLoader:
    def __init__(self, filename):
        # This finds where your project is on the computer
        base_path = os.path.dirname(os.path.dirname(__file__))
        # This points to the 'data' folder
        self.filepath = os.path.join(base_path, 'data', filename)
        self.df = None

    def load(self):
        """Loads the CSV file into a table."""
        if os.path.exists(self.filepath):
            print(f"Loading data from: {self.filepath}")
            try:
                # specific encoding helps with special characters in song names
                self.df = pd.read_csv(self.filepath, encoding='utf-8') 
                print("✅ Success! Data loaded.")
                print(f"📊 The dataset has {self.df.shape[0]} rows and {self.df.shape[1]} columns.")
                print("Here are the first 3 rows:")
                print(self.df.head(3))
            except Exception as e:
                print(f"❌ Error reading CSV: {e}")
        else:
            print(f"❌ File not found at: {self.filepath}")

# This part runs when you press the Play button
if __name__ == "__main__":
    # We use the filename you renamed earlier
    loader = MusicLoader("spotify_data.csv")
    loader.load()