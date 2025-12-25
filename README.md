## Technical Analysis & Performance
To satisfy the requirements of HAX712X, we have implemented:

- **Reproducibility**: The project uses a clear directory structure. All dependencies are listed in the installation guide.
- **Performance**: The data loader is optimized for CSV files. Loading 8,000+ rows takes less than 1 second on a standard machine.
- **Object-Oriented Design**: We use a `MusicLoader` class for data ingestion and a `MusicVisualizer` class for chart generation, ensuring code reusability.

## Automated Testing (CI/CD)
We use `pytest` to ensure code quality. Tests cover:
- Data file path verification.
- Successful loading of Pandas DataFrames.
- Integrity of the data structure.

## Analysis Results
Our visualization confirms the top 5 longest tracks in the dataset (2009-2025):

![Spotify Chart](results.png)

## Presentation
The final project slides can be found in the `/slide` directory of the repository.*