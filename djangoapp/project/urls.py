from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from unasus_registros.views.student_view import (
    create_student,
    get_all_students,
    get_student_by_cpf,
    update_student
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', create_student, name='create_student'),
    path('students/all/', get_all_students, name='get_all_students'),  # Endpoint para listar todos os alunos
    path('students/<int:cpf>/', get_student_by_cpf, name='get_student_by_cpf'),  # Endpoint para listar um aluno por ID
    path('students/update/<int:student_id>/', update_student, name='update_student'),  # Endpoint para atualizar um aluno
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
