from django.urls import path
from .views import pesquisa

urlpatterns = [
    path('', pesquisa, name='pesquisa'),
]
  