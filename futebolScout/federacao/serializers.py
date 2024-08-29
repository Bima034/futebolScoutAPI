from .models import Federacao
from rest_framework import serializers

class FederacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Federacao
        fields = ['nome', 'id']