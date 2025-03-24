from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JogadorViewSet

router = DefaultRouter()
router.register(r'jogadores', JogadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listJogador, name='list-jogador'),
    path('detail/<int:jogador_id>/', views.detailJogador, name='detail-jogador'),
    path('add/', views.addJogador, name='add-jogador'),
    path('edit/<int:jogador_id>/', views.editJogador, name='edit-jogador'),
    path("delete/<int:jogador_id>/", views.deleteJogador, name="delete-jogador"),
]
'''