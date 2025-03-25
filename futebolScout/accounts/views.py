from rest_framework import viewsets
from rest_framework.response import Response
from .models import Pessoa
from .serializers import PessoaSerializer
from .permissions import IsAuthenticatedOrCreateOnly
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

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


class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]  # Permite o acesso sem autenticação

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data.get('access')

        return Response({
            'token': access_token,  # só retorna o access
            'user_id': request.user.id,
            'username': request.user.username,
        })

    
def isTorcedor(user):
    return user.groups.filter(name='torcedor').exists()

def isGestor(user):
    return user.groups.filter(name='gestor').exists()