from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from unasus_registros.utils.map import generate_heatmap
from unasus_registros.views.submission_view import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from unasus_registros.views.auth_view import *
from unasus_registros.views.student_view import *

urlpatterns = [
    path('generate_heatmap/', generate_heatmap, name='generate_heatmap'),
    path('api/register/', register_user),
    path('api/token/', obtain_jwt_token),
    path('api/user/', get_user),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('admin/', admin.site.urls),
    path('students/', create_student, name='create_student'),
    path('students/all/', get_all_students, name='get_all_students'), 
    path('students/cpf/', get_student_by_cpf, name='get_student_by_cpf'),  
    path('students/update/<int:student_id>/', update_student, name='update_student'), 
    path('students/with-submissions/', search_students_with_submissions, name='search_students_with_submissions'),  
    path('submissions/cpf/<str:student_cpf>/', get_submission_by_cpf, name='get_submission_by_cpf'), 
    path('submissions/', create_submission, name='create'),
    path('submissions/all/', get_all_submissions, name='get_all_submissions'),
    path('submissions/<int:submission_id>/', get_submission_by_id, name='get_submission_by_id'),
    path('students/search/', search_student_by_name, name='search_student_by_name')

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
