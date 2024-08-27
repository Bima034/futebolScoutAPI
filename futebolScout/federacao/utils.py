from .models import Federacao

def query_set_federacao_pais(pais):
    federacao = Federacao.objects.filter(localidade=pais)
    return federacao