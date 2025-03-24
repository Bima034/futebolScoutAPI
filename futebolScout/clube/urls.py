from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClubeViewSet

router = DefaultRouter()
router.register(r'clubes', ClubeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listClube, name='list-clube'),
    path('add/', views.addClube, name='add-clube'),
    path("detail/<int:id>", views.detailClube, name="detail-clube"),
    path('edit/<int:id>', views.editClube, name='edit-clube'),
    path('delete/<int:id>', views.deleteClube, name='delete-clube'),
]
'''