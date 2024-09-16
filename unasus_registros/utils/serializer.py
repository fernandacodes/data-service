# serializers.py
from rest_framework import serializers

from unasus_registros.models.especialty import Specialty
from ..models.user_model import CustomUser
from ..models.student_model import Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'cpf', 'first_name', 'last_name', 'role']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# serializers.py
from rest_framework import serializers

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
