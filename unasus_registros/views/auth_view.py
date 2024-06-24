from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import Group
from ..models.user_model import CustomUser, Admin
from ..utils.serializer import StudentSerializer, UserSerializer
from rest_framework_jwt.views import VerifyJSONWebTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from ..models.student_model import Student
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    user_data = request.data.get('user', {})
    student_data = request.data.get('student', {})

    # Serializa os dados do usuário
    user_serializer = UserSerializer(data=user_data)
    if user_serializer.is_valid():
        user = user_serializer.save()

        # Verifica se o papel do usuário é 'student'
        if user.role == 'student':
            student_group = Group.objects.get(name='Students')
            user.groups.add(student_group)

            # Serializa e salva os dados do aluno associado
            student_data['user'] = user.id
            student_serializer = StudentSerializer(data=student_data)
            if student_serializer.is_valid():
                student_serializer.save()
            else:
                # Se houver erros na validação do aluno, exclui o usuário recém-criado
                user.delete()
                return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Verifica se o papel do usuário é 'admin'
        elif user.role == 'admin':
            admin_group = Group.objects.get(name='Admins')
            user.groups.add(admin_group)

        user.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])  # Permite acesso sem autenticação
def get_user(request):
    try:
        # Obtém o token do cabeçalho da requisição
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response({'error': 'Authorization header not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        # O token está no formato "Bearer <token>"
        token_str = auth_header.split()[1]
        
        # Decodifica o token
        data = {'token': token_str}
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        user = valid_data['user']
        
        # Serializa os dados do usuário
        serializer = UserSerializer(user)
        
        # Adiciona dados específicos de Student ou Admin se necessário
        user_data = serializer.data
       
        return Response(user_data, status=status.HTTP_200_OK)
    
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
