from django.urls import path, include
from .views import *

urlpatterns =[

    path('cars/', CarViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='user_profile_list'),
    path('cars/<int:pk>/', CarViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='car_detail'),

    path('bets/', BetVewSets.as_view({'get': 'list', 'post': 'create'}),
         name='bet_list'),
    path('bets/<int:pk>/',BetVewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='bet_detail'),

]