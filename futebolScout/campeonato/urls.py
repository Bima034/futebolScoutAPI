from rest_framework.routers import DefaultRouter
from .views import CampeonatoViewSet

router = DefaultRouter()
router.register(r'campeonatos', CampeonatoViewSet)

urlpatterns = router.urls
