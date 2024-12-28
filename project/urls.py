from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from unasus_registros.utils.map import generate_heatmap
from unasus_registros.views.call_view import *
from unasus_registros.views.doctor_View import *
from unasus_registros.views.especialy_view import *
from unasus_registros.views.submission_view import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from unasus_registros.views.auth_view import *
from unasus_registros.views.student_view import *
from unasus_registros.views.teleConsultation_view import *
from unasus_registros.views.ubs_view import *

urlpatterns = [
    path('api/generate_heatmap/', generate_heatmap, name='generate_heatmap'),
    path('api/register/', register_user),
    path('api/token/', obtain_jwt_token),
    path('api/user/', get_user),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/admin/', admin.site.urls),

    # Student routes
    path('api/students/', create_student, name='create_student'),
    path('api/students/all/', get_all_students, name='get_all_students'),
    path('api/students/cpf/', get_student_by_cpf, name='get_student_by_cpf'),
    path('api/students/update/<int:student_id>/', update_student, name='update_student'),
    path('api/students/with-submissions/', search_students_with_submissions, name='search_students_with_submissions'),
    path('api/students/search/', search_student_by_name, name='search_student_by_name'),
    path('api/students/without-submissions/export/', export_students_without_submissions, name='export_students_without_submissions'),
    path('api/students/with-submissions/export/', export_students_with_submissions, name='export_students_with_submissions'),


    # Submission routes
    path('api/submissions/cpf/<str:student_cpf>/', get_submission_by_cpf, name='get_submission_by_cpf'),
    path('api/submissions/', create_submission, name='create_submission'),
    path('api/submissions/all/', get_all_submissions, name='get_all_submissions'),
    path('api/submissions/<int:submission_id>/', get_submission_by_id, name='get_submission_by_id'),
    path('api/submissions/has_submission/<str:student_cpf>/', has_submission, name='has_submission'),  
    path('api/submissions/delete/<str:student_cpf>/', delete_submission, name='delete_submission'),

    # UBS routes
    path('api/ubs/create/', create_ubs, name='create_ubs'),
    path('api/ubs/<int:ubs_id>/', get_ubs_by_id, name='get_ubs_by_id'),
    path('api/ubs/', get_all_ubs, name='get_all_ubs'),
    path('api/ubs/update/<int:ubs_id>/', update_ubs, name='update_ubs'),
    path('api/ubs/delete/<int:ubs_id>/', delete_ubs, name='delete_ubs'),
    path('api/ubs/city/<str:city_name>/', get_ubs_by_city, name='get_ubs_by_city'),
    path('api/ubs/state/<str:state_name>/', get_ubs_by_state, name='get_ubs_by_state'),

    # Teleconsultation routes
    path('api/teleconsultations_by_month/<int:ubs_id>/<int:year>/<int:month>/', teleconsultations_by_month),
    path('api/teleconsultations_by_month/<int:ubs_id>/', teleconsultations_by_month),
    path('api/teleconsultations/', teleconsultations_create, name='create_teleconsultation'),
    path('api/teleconsultations/all/', list_all_teleconsultations, name='list_teleconsultation'),

    # Doctor routes
    path('api/doctors/', doctor_get_all, name='doctor-get-all'),
    path('api/doctors/<int:id>/', doctor_get_by_id, name='doctor-get-by-id'),
    path('api/doctors/create/', doctor_create, name='doctor-create'),
    path('api/doctors/<int:id>/update/', doctor_update, name='doctor-update'),
    path('api/doctors/<int:id>/delete/', doctor_delete, name='doctor-delete'),

    # Specialty routes
    path('api/specialties/', specialty_get_all, name='specialty-get-all'),
    path('api/specialties/create/', specialty_create, name='specialty-create'),
    path('api/specialties/<int:id>/', specialty_get_by_id, name='specialty-get-by-id'),
    path('api/specialties/<int:id>/update/', specialty_update, name='specialty-update'),
    path('api/specialties/<int:id>/delete/', specialty_delete, name='specialty-delete'),

    # Call routes
    path('api/calls/', get_calls, name='get_calls'),  # Ler todos os chamados
    path('api/calls/<int:call_id>/', get_call_by_id, name='get_call_by_id'),  # Ler por ID
    path('api/calls/create/', create_call, name='create_call'),  # Cadastrar
    path('api/calls/<int:call_id>/update/', update_call, name='update_call'),  # Atualizar
    path('api/calls/<int:call_id>/delete/', delete_call, name='delete_call'),  # Deletar

    # Gerar gráfico por UBS
    path('api/calls/report/<int:ubs_id>/<int:year>/<int:month>/', get_calls_report_by_ubs, name='get_calls_report_by_ubs'),

    # Gerar gráfico geral para todas as UBS
    path('api/calls/report/overall/<int:year>/<int:month>/', get_overall_calls_report, name='get_overall_calls_report'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
