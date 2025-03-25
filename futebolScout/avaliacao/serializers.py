from rest_framework import serializers
from .models import AvaliacaoJogador, AvaliacaoFederacao, AvaliacaoCampeonato, AvaliacaoClube

class AvaliacaoJogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoJogador
        fields = '__all__'
        
class AvaliacaoFederacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoFederacao
        fields = '__all__'
        
class AvaliacaoCampeonatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoCampeonato
        fields = '__all__'
        
class AvaliacaoClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoClube
        fields = '__all__'
        
