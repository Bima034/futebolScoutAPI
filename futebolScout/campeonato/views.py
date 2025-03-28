from rest_framework import viewsets
from .models import Campeonato
from .serializers import CampeonatoSerializer
from .permissions import IsAuthenticatedWithJWT
class CampeonatoViewSet(viewsets.ModelViewSet):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer
    permission_classes = [IsAuthenticatedWithJWT]
