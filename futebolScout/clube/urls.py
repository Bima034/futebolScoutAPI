from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list-clube'),
    path('add/', views.add, name='add-clube'),
    path("detail/<int:id>", views.detail, name="detail-clube"),
    path('edit/<int:id>', views.edit, name='edit-clube'),
    path('delete/<int:id>', views.delete, name='delete-clube'),
]
