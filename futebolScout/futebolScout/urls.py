"""
URL configuration for futebolScout project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
#from jogador.views import dashboard
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="FutebolScout API",
        default_version='v1',
        description="A API do FutebolScout fornece acesso a informações detalhadas sobre jogadores, clubes, campeonatos e federações. "
                        "Ela permite a integração com sistemas externos para gerenciar e consultar dados relacionados ao futebol.",
        terms_of_service="https://www.seusite.com/termos/",
        contact=openapi.Contact(email="contato@seusite.com"),
        license=openapi.License(name="Sua Licença"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    path('admin/', admin.site.urls),
    #path('', dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('jogador/', include('jogador.urls')),
    path('jogador/', include('jogador.urls')),
    path('federacao/', include('federacao.urls')),
    #path('clube/', include('clube.urls')),
    path('clube/', include('clube.urls')),
    #path('campeonato/', include('campeonato.urls')),
    #path('federacao/', include('federacao.urls')),
    path('campeonato/', include('campeonato.urls')),
    path('pesquisa/', include('pesquisa.urls')),
    path('api-auth/', include('rest_framework.urls')),  # para login no navegador do DRF
    #path('avaliacao/', include('avaliacao.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
