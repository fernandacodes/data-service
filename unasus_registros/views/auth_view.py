from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import Group
from ..models.user_model import CustomUser, Admin
from ..utils.serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])  # Permite acesso sem autenticação
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user.role == 'student':
            student_group = Group.objects.get(name='Students')
            user.groups.add(student_group)
        elif user.role == 'admin':
            admin_group = Group.objects.get(name='Admins')
            user.groups.add(admin_group)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    if request.user.is_authenticated:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    else:
        return Response({"error": "Usuário não autenticado"}, status=status.HTTP_401_UNAUTHORIZED)