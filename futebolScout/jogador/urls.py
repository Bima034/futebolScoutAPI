from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('list/', views.listJogador, name='list-jogador'),
    path('detail/<int:jogador_id>/', views.detailJogador, name='detail-jogador'),
    path('add/', views.addJogador, name='add-jogador'),
    path('edit/<int:jogador_id>/', views.editJogador, name='edit-jogador'),
    path("delete/<int:jogador_id>/", views.deleteJogador, name="delete-jogador"),
]