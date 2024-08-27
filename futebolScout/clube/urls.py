from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard-clube'),
    path('add/', views.add, name='add-clube'),
    path("detail/<int:id>", views.detail, name="detail-clube"),
]
