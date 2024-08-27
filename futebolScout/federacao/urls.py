from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.listFederacao, name='list-federacao'),
    path('detail/<int:id_federacao>', views.detailFederacao, name='detail-federacao'),
    path("add/", views.add, name="add-federacao"),
]
