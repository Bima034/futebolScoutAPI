from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.createUser, name='createUser'),
]
