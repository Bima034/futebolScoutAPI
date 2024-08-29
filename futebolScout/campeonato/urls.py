from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list-campeonato'),
    path('add/', views.add, name='add-campeonato'),
    path("detail/<int:id>", views.detail, name="detail-campeonato"),
    path('edit/<int:id>', views.edit, name='edit-campeonato'),
    path('delete/<int:id>', views.delete, name='delete-campeonato'),
]
