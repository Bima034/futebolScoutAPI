from django.urls import path
from . import views, apis
urlpatterns = [
    path('', views.listFederacao, name='list-federacao'),
    path('detail/<int:id_federacao>', views.detailFederacao, name='detail-federacao'),
    path("add/", views.addJogador, name="add-federacao"),
    path("delete/<int:id_federacao>", views.deleteJogador, name="delete-federacao"),
    path("edit/<int:id_federacao>", views.editJogador, name=""),
    # path("get_afiliadas/<str:localidade>", apis.get_afiliadas, name="get-afiliadas-federacao"),
    path("get_lista_possiveis_afiliadas/<str:localidade>/<int:id_federacao>", apis.AfiliadasPossiveis.as_view(), name="get-lista-possiveis-afiliadas-federacao"),
]
