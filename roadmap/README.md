# Project Roadmap: Global Music Trends (2009-2025)

## 1. Project Description
We analyze the evolution of global music trends using Spotify data (2009-2025). We will look at features like "danceability," "energy," and "valence" to see how listener preferences have changed.

## 2. Architecture
- **`spotify_project/`**: Main Python code.
    - `dataloader.py`: Downloads/cleans data.
    - `visualization.py`: Creates charts.
- **`slide/`**: Presentation slides.
- **`data/`**: Storage for the CSV file.

## 3. Data Strategy
- **Source:** Kaggle (Spotify Global Music Dataset 2009-2025).
- **Tool:** We will use the `pooch` library or `pandas` to load the data.

## 4. Timeline
- **Oct 25:** Roadmap and Git setup (Done).
- **Nov 15:** Data cleaning code working.
- **Nov 30:** Visualizations working.
- **Dec 10:** Final presentation ready.