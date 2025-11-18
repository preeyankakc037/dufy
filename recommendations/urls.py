# recommendations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.discover_view, name='home'),
    path('discover/', views.discover_view, name='discover'),
    path('genre/', views.genre_view, name='genre'),                    # ← WAS MISSING
    path('top-charts/', views.top_charts_view, name='top_charts'),
    path('trending/', views.trending_view, name='trending'),
    path('favourites/', views.favourites_view, name='favourites'),
    path('playlists/', views.playlist_view, name='playlists'),
    path('signup/', views.signup_view, name='signup'),
    path('health/', views.health_check, name='health'),
    
    # API
    path('api/recommend/', views.get_recommendations, name='recommend'),
]