from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('list/', views.listJogador, name='list-jogador'),
    path('detail/', views.detailJogador, name='detail-jogador'),
    path('add/', views.addJogador, name='add-jogador'),
]