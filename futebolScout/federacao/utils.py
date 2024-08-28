from .models import Federacao

def query_set_federacao_pais():
    federacao = Federacao.objects.all()
    
    return federacao