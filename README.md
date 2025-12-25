# Spotify Evolution Project (2009-2025)
**Course:** HAX712X - Software Development

## Project Description
This project analyzes the "Spotify Global Music Dataset" to investigate track characteristics across different tracks from 2009 to 2025. We focus on track duration and data integrity.

## Project Structure
- `spotify_project/`: Contains the core logic (`loader.py` and `visualization.py`).
- `data/`: Contains the Spotify CSV datasets.
- `test/`: Contains automated tests (pytest).
- `slide/`: Contains the final project presentation.
- `roadmap/`: Contains the initial project plan.

## How to Run
1. **Install requirements:** 
   `pip install pandas matplotlib pytest`
2. **Run the visualization:** 
   `python spotify_project/visualization.py`
3. **Run automated tests:** 
   `python -m pytest`

## Key Technical Features
- **Object-Oriented Programming**: Data loading is encapsulated in a `MusicLoader` class.
- **Data Analysis**: Automated sorting and visualization of track durations.
- **Robustness**: Unit tests ensure data paths and loading functions work correctly.