from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard-federacao'),
    path('detail/<int:id_federacao>', views.detailFederacao, name='detail-federacao'),
    path('list/', views.listFederacao, name='list-federacao'),
]
