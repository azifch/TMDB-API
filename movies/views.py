from django.http import JsonResponse
from .utils import fetch_tmdb_data

def popular_movies(request):
    data = fetch_tmdb_data('movie/popular')
    return JsonResponse(data)

def top_rated_movies(request):
    data = fetch_tmdb_data('movie/top_rated')
    return JsonResponse(data)

def search_movies(request):
    query = request.GET.get('query')
    data = fetch_tmdb_data(f'search/movie?query={query}')
    return JsonResponse(data)

