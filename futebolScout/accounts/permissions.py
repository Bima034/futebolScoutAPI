from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedOrCreateOnly(BasePermission):
    """
    Permite criar (POST) sem autenticação, mas exige login para os outros métodos.
    """
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated
