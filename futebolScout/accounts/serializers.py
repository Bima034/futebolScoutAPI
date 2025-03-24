from rest_framework import serializers
from .models import Pessoa
from django.contrib.auth.models import Group

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        groups = validated_data.pop('groups', [])
        permissions = validated_data.pop('user_permissions', [])
        user = Pessoa(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()

        if groups:
            user.groups.set(groups)
            
        
        if permissions:
            user.user_permissions.set(permissions)
            
        return user
