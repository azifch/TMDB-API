from django.urls import path
from . import views

urlpatterns = [
    path('popular/', views.popular_movies, name='popular_movies'),
    path('top-rated/', views.top_rated_movies, name='top_rated_movies'),
    path('search/', views.search_movies, name='search_movies'),
]
