from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet, LoginView

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
]
