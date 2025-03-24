from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Pessoa
from .serializers import PessoaSerializer
from .permissions import IsAuthenticatedOrCreateOnly  # importa a permissão

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [IsAuthenticatedOrCreateOnly]

    def isGestor(self, user):
        return user.groups.filter(name='Gestores').exists()

    def isTorcedor(self, user):
        return user.groups.filter(name='Torcedores').exists()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if self.isGestor(user):
                return Pessoa.objects.all()
            elif self.isTorcedor(user):
                return Pessoa.objects.filter(id=user.id)
        return Pessoa.objects.none()

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username,
        })
    
def isTorcedor(user):
    return user.groups.filter(name='torcedor').exists()

def isGestor(user):
    return user.groups.filter(name='gestor').exists()