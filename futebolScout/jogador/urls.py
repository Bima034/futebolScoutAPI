from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('list', views.listJogador, name='listJogador'),
    path('detail', views.detailJogador, name='detailJogador'),
]