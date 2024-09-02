from django.urls import path
from . import views

urlpatterns = [
    path('', views.listCampeonato, name='list-campeonato'),
    path('add/', views.addCampeonato, name='add-campeonato'),
    path("detail/<int:id>", views.detailCampeonato, name="detail-campeonato"),
    path('edit/<int:id>', views.editCampeonato, name='edit-campeonato'),
    path('delete/<int:id>', views.deleteCampeonato, name='delete-campeonato'),
]
