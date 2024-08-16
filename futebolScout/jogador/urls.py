from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listJogador, name='list-jogador'),
    path('detail/<int:id_jogador>', views.detailJogador, name='detail-jogador'),
]