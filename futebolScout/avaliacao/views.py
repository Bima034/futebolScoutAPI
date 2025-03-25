from rest_framework import viewsets
from .models import AvaliacaoJogador, AvaliacaoFederacao, AvaliacaoCampeonato, AvaliacaoClube
from .serializers import AvaliacaoJogadorSerializer, AvaliacaoFederacaoSerializer, AvaliacaoCampeonatoSerializer, AvaliacaoClubeSerializer  
from .permissions import IsAuthenticatedWithJWT
class AvaliacaoJogadorViewSet(viewsets.ModelViewSet):  
    permission_classes = [IsAuthenticatedWithJWT]
    queryset = AvaliacaoJogador.objects.all()
    serializer_class = AvaliacaoJogadorSerializer
    
class AvaliacaoFederacaoViewSet(viewsets.ModelViewSet):  
    permission_classes = [IsAuthenticatedWithJWT]
    queryset = AvaliacaoFederacao.objects.all()
    serializer_class = AvaliacaoFederacaoSerializer
    
class AvaliacaoCampeonatoViewSet(viewsets.ModelViewSet):  
    permission_classes = [IsAuthenticatedWithJWT]
    queryset = AvaliacaoCampeonato.objects.all()
    serializer_class = AvaliacaoCampeonatoSerializer
    
class AvaliacaoClubeViewSet(viewsets.ModelViewSet):  
    permission_classes = [IsAuthenticatedWithJWT]
    queryset = AvaliacaoClube.objects.all()
    serializer_class = AvaliacaoClubeSerializer