# serializers.py
from rest_framework import serializers
from ..models.user_model import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'cpf', 'first_name', 'last_name', 'role']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
