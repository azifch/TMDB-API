import requests

def fetch_tmdb_data(endpoint):
    API_KEY = '43acd04418dbfb5c524f0894485ed07f'
    base_url = 'https://api.themoviedb.org/3'
    url = f'{base_url}/{endpoint}?api_key={API_KEY}'
    response = requests.get(url)
    return response.json()
