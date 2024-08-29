from rest_framework.response import Response
from .models import Federacao
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .serializers import FederacaoSerializer

class AfiliadasPossiveis(APIView):
    def get(self, request, localidade, id_federacao=0):
        federacao = Federacao.objects.filter(localidade=localidade).exclude(id=id_federacao)
        serializer = FederacaoSerializer(federacao, many=True)
        return Response({'afiliadas': serializer.data})
    
    def post(self, request, localidade, id_federacao=0):
        return Response('Método não permitido', status=405)
    
