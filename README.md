# Movie Recommendation System

This project is a content-based movie recommendation system built with Python and Flask. It uses a dataset of movies and their metadata to suggest similar movies based on user input.

## Features
- Web interface to input your favorite movie
- Recommends top 30 similar movies
- Uses TF-IDF vectorization and cosine similarity on movie metadata (genres, keywords, tagline, cast, director)

## Dataset
The system uses a `movies.csv` file with the following relevant columns:
- `index`
- `title`
- `genres`
- `keywords`
- `tagline`
- `cast`
- `director`

Other columns are present but not directly used for recommendations.

## Requirements
- Python 3.x
- Flask
- numpy
- pandas
- scikit-learn

Install dependencies with:
```bash
pip install Flask numpy pandas scikit-learn
```

## Usage
1. Place `movies.csv` in the project directory.
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open your browser and go to `http://127.0.0.1:5000/`.
4. Enter a movie name to get recommendations.

## File Structure
- `app.py` - Main Flask application
- `movies.csv` - Movie dataset
- `templates/` - HTML templates for the web interface
    - `index.html` - Home page
    - `recommendations.html` - Recommendations page
- `requirement.txt` - Python dependencies

## Example
Enter a movie name (e.g., "Inception") and receive a list of 30 similar movies based on content features.

## License
This project is for educational purposes.
