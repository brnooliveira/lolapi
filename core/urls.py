from django.urls import path
from .views import summoner_view, summoner_list

urlpatterns = [
    path('summoner/<str:summoner_name>/', summoner_view, name='summoner-view'),
    path('summoners/', summoner_list, name='summoner-list'),
]
