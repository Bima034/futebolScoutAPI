from .models import Federacao

def query_set_federacao_pais(pais, id=None):
    federacao = Federacao.objects.filter(localidade=pais).exclude(id=id)
    
    return federacao