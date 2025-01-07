# My Django Movie Project

## Project Overview
This project fetches movie data from the TMDB API and provides custom endpoints for popular movies, top-rated movies, and movie search.

## How to Run the Application Locally
1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python manage.py runserver`

## API Endpoints
- **Popular Movies**: `/movies/popular/`
- **Top Rated Movies**: `/movies/top-rated/`
- **Search Movies**: `/movies/search/?query=<movie_name>`

## How to Deploy the Application
(Typical deployment steps here)

## How to Generate an API Key
1. Sign up on the TMDB website.
2. Navigate to the API section and generate an API key.
3. Add the key to your `utils.py` file.

