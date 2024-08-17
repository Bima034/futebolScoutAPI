from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listJogador, name='list-jogador'),
    path('detail/', views.detailJogador, name='detail-jogador'),
    path('add/', views.addJogador, name='add-jogador'),
]