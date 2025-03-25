from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AvaliacaoCampeonatoViewSet, AvaliacaoFederacaoViewSet, AvaliacaoClubeViewSet, AvaliacaoJogadorViewSet

router = DefaultRouter()
router.register(r'avaliacoes-jogadores', AvaliacaoJogadorViewSet)
router.register(r'avaliacoes-campeonatos', AvaliacaoCampeonatoViewSet)
router.register(r'avaliacoes-federacoes', AvaliacaoFederacaoViewSet)
router.register(r'avaliacoes-clubes', AvaliacaoClubeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]