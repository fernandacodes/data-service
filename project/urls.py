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
    path('generate_heatmap/', generate_heatmap, name='generate_heatmap'),
    path('api/register/', register_user),
    path('api/token/', obtain_jwt_token),
    path('api/user/', get_user),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('admin/', admin.site.urls),
    
    # Student routes
    path('students/', create_student, name='create_student'),
    path('students/all/', get_all_students, name='get_all_students'),
    path('students/cpf/', get_student_by_cpf, name='get_student_by_cpf'),
    path('students/update/<int:student_id>/', update_student, name='update_student'),
    path('students/with-submissions/', search_students_with_submissions, name='search_students_with_submissions'),
    path('students/search/', search_student_by_name, name='search_student_by_name'),

    # Submission routes
    path('submissions/cpf/<str:student_cpf>/', get_submission_by_cpf, name='get_submission_by_cpf'),
    path('submissions/', create_submission, name='create_submission'),
    path('submissions/all/', get_all_submissions, name='get_all_submissions'),
    path('submissions/<int:submission_id>/', get_submission_by_id, name='get_submission_by_id'),

    # UBS routes
    path('ubs/create/', create_ubs, name='create_ubs'),
    path('ubs/<int:ubs_id>/', get_ubs_by_id, name='get_ubs_by_id'),
    path('ubs/', get_all_ubs, name='get_all_ubs'),
    path('ubs/update/<int:ubs_id>/', update_ubs, name='update_ubs'),
    path('ubs/delete/<int:ubs_id>/', delete_ubs, name='delete_ubs'),
    path('ubs/city/<str:city_name>/', get_ubs_by_city, name='get_ubs_by_city'),
    path('ubs/state/<str:state_name>/', get_ubs_by_state, name='get_ubs_by_state'),

    # Teleconsultation routes
    path('teleconsultations_by_month/<int:ubs_id>/<int:year>/<int:month>/', teleconsultations_by_month),
    path('teleconsultations_by_month/<int:ubs_id>/', teleconsultations_by_month),
    path('teleconsultations/', teleconsultations_create, name='create_teleconsultation'),
    path('teleconsultations/all/', list_all_teleconsultations, name='list_teleconsultation'),

    # Doctor routes
    path('doctors/', doctor_get_all, name='doctor-get-all'),
    path('doctors/<int:id>/', doctor_get_by_id, name='doctor-get-by-id'),
    path('doctors/create/', doctor_create, name='doctor-create'),
    path('doctors/<int:id>/update/', doctor_update, name='doctor-update'),
    path('doctors/<int:id>/delete/', doctor_delete, name='doctor-delete'),

    # Specialty routes
    path('specialties/', specialty_get_all, name='specialty-get-all'),
    path('specialties/create/', specialty_create, name='specialty-create'),
    path('specialties/<int:id>/', specialty_get_by_id, name='specialty-get-by-id'),
    path('specialties/<int:id>/update/', specialty_update, name='specialty-update'),
    path('specialties/<int:id>/delete/', specialty_delete, name='specialty-delete'),

    path('calls/', get_calls, name='get_calls'),  # Ler todos os chamados
    path('calls/<int:call_id>/', get_call_by_id, name='get_call_by_id'),  # Ler por ID
    path('calls/create/', create_call, name='create_call'),  # Cadastrar
    path('calls/<int:call_id>/update/', update_call, name='update_call'),  # Atualizar
    path('calls/<int:call_id>/delete/', delete_call, name='delete_call'),  # Deletar

    # Gerar gráfico por UBS
    path('calls/report/<int:ubs_id>/<int:year>/<int:month>/', get_calls_report_by_ubs, name='get_calls_report_by_ubs'),

    # Gerar gráfico geral para todas as UBS
    path('calls/report/overall/<int:year>/<int:month>/', get_overall_calls_report, name='get_overall_calls_report'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
