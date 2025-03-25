from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class IsAuthenticatedWithJWT(BasePermission):
    """
    Permissão personalizada para garantir que o usuário esteja autenticado com um token JWT válido.
    Bloqueia os métodos POST, DELETE e PUT se não houver um token válido.
    """
    def has_permission(self, request, view):
        if request.method == 'POST' or request.method == 'DELETE' or request.method == 'PUT' or request.method == 'PATCH':
            auth = JWTAuthentication()

            # Tenta autenticar o usuário com o token JWT
            auth = auth.authenticate(request)

            # Verifica se o usuário não foi autenticado
            if auth is None:
                raise AuthenticationFailed('Token JWT inválido ou ausente.')

            return True
        return True
