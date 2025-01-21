import csv
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models import Q

from unasus_registros import models
from ..models.submission import Submission
from ..models.student_model import Student
from django.core.files.storage import default_storage

@csrf_exempt
def has_submission(request, student_cpf): 
    try:
        student = Student.objects.get(CPF=student_cpf)
        if Submission.objects.filter(student=student).exists():
            return JsonResponse({"has_submission": True})
        else:
            return JsonResponse({"has_submission": False})
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found."}, status=404)

@csrf_exempt
def create_submission(request):
    if request.method == 'POST':
        try:
            data = request.POST
            student_cpf = data.get('cpf')
            student = Student.objects.get(CPF=student_cpf)

            # Verificar se já existe uma submissão para o estudante
            if Submission.objects.filter(student=student).exists():
                return JsonResponse({"error": "Student has already submitted."}, status=400)

            # Criar uma nova submissão
            submission = Submission.objects.create(
                student=student,
                term_accepted=data.get('term_accepted') == 'True',
                mother_name=data.get('mother_name'),
                nationality=data.get('nationality'),
                marital_status=data.get('marital_status'),
                father_name=data.get('father_name'),
                blood_type=data.get('blood_type'),
                birth_date=data.get('birth_date'),
                rh_factor=data.get('rh_factor'),
                gender=data.get('gender'),
                ethnicity=data.get('ethnicity'),
                physical_disability=data.get('physical_disability') == 'True',
                disability_details=data.get('disability_details'),
                disability_degree=data.get('disability_degree'),
                psychological_disorder=data.get('psychological_disorder'),
                street_address=data.get('street_address'),
                number=data.get('number'),
                complement=data.get('complement'),
                neighborhood=data.get('neighborhood'),
                city=data.get('city'),
                state=data.get('state'),
                postal_code=data.get('postal_code'),
                rg=data.get('rg'),
                birth_city=data.get('birth_city'),
                birth_state=data.get('birth_state'),
                high_school_graduation_year=data.get('high_school_graduation_year'),
                university_name=data.get('university_name'),
                graduation_year=data.get('graduation_year'),
                graduation_course=data.get('graduation_course'),
                current_ubs_name=data.get('current_ubs_name'),
                ubs_type=data.get('ubs_type'),
                internet_speed=data.get('internet_speed'),
                internet_availability=data.get('internet_availability'),
                energy_availability=data.get('energy_availability'),
            )
            
            document_links = {}
            document_fields = [
                'rg_cpf_copy', 'reservista_cert_copy', 'diploma_copy',
                'marriage_certificate_copy', 'address_proof_copy',
                'residence_internet_copy', 'ubs_internet_copy'
            ]
            for field_name in document_fields:
                file = request.FILES.get(field_name)
                if file:
                    file_name = f"{student_cpf}/{file.name}"
                    file_storage_path = default_storage.save(file_name, file)
                    # Atribuindo o caminho do arquivo ao modelo
                    setattr(submission, field_name, file_storage_path)
                    submission.save()

                    # Gerando a URL completa do arquivo
                    document_links[field_name] = request.build_absolute_uri(default_storage.url(file_storage_path))

            return JsonResponse({"Message": "Successfully created submission", "document_links": document_links}, status=201)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed."}, status=405)
    
@csrf_exempt
def get_all_submissions(request):
    if request.method == 'GET':
        submissions = Submission.objects.all()
        submissions_list = list(submissions.values())
        return JsonResponse({"submissions": submissions_list}, safe=False)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
    
@csrf_exempt
def get_submission_by_id(request, submission_id):
    if request.method == 'GET':
        try:
            submission = Submission.objects.get(id=submission_id)
            document_fields = [
                'rg_cpf_copy', 'reservista_cert_copy', 'diploma_copy',
                'marriage_certificate_copy', 'address_proof_copy',
                'residence_internet_copy', 'ubs_internet_copy'
            ]
            document_links = {field: request.build_absolute_uri(getattr(submission, field).url) if getattr(submission, field) else None for field in document_fields}

            return JsonResponse({
                "submission": {
                    "id": submission.id,
                    "student": submission.student.to_dict(),
                    "term_accepted": submission.term_accepted,
                    "nationality": submission.nationality,
                    "mother_name": submission.mother_name,
                    "father_name": submission.father_name,
                    "blood_type": submission.blood_type,
                    "rh_factor": submission.rh_factor,
                    "gender": submission.gender,
                    "ethnicity": submission.ethnicity,
                    "physical_disability": submission.physical_disability,
                    "disability_details": submission.disability_details,
                    "disability_degree": submission.disability_degree,
                    "psychological_disorder": submission.psychological_disorder,
                    "street_address": submission.street_address,
                    "number": submission.number,
                    "complement": submission.complement,
                    "neighborhood": submission.neighborhood,
                    "city": submission.city,
                    "state": submission.state,
                    "postal_code": submission.postal_code,
                    "rg": submission.rg,
                    "birth_city": submission.birth_city,
                    "birth_state": submission.birth_state,
                    "high_school_graduation_year": submission.high_school_graduation_year,
                    "university_name": submission.university_name,
                    "graduation_year": submission.graduation_year,
                    "graduation_course": submission.graduation_course,
                    "current_ubs_name": submission.current_ubs_name,
                    "ubs_type": submission.ubs_type,
                    **document_links,
                    "internet_speed": submission.internet_speed,
                    "internet_availability": submission.internet_availability,
                    "energy_availability": submission.energy_availability,
                    "created_at": submission.created_at,
                }
            }, safe=False)
        except Submission.DoesNotExist:
            return JsonResponse({"error": f"Submission with ID {submission_id} does not exist."}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def get_submission_by_cpf(request, student_cpf):
    if request.method == 'GET':
        try:
            student = Student.objects.get(CPF=student_cpf)
            submission = Submission.objects.filter(student=student).first()  # Pega a primeira submissão encontrada
            if submission:
                return JsonResponse({
                    "submission": {
                        "id": submission.id,
                        "student": submission.student.to_dict(),
                        "term_accepted": submission.term_accepted,
                        "mother_name": submission.mother_name,
                        "birth_date": submission.birth_date,
                        "marital_status": submission.marital_status,
                        "father_name": submission.father_name,
                        "nationality": submission.nationality,
                        "blood_type": submission.blood_type,
                        "rh_factor": submission.rh_factor,
                        "gender": submission.gender,
                        "ethnicity": submission.ethnicity,
                        "physical_disability": submission.physical_disability,
                        "disability_details": submission.disability_details,
                        "disability_degree": submission.disability_degree,
                        "psychological_disorder": submission.psychological_disorder,
                        "street_address": submission.street_address,
                        "number": submission.number,
                        "complement": submission.complement,
                        "neighborhood": submission.neighborhood,
                        "city": submission.city,
                        "state": submission.state,
                        "postal_code": submission.postal_code,
                        "rg": submission.rg,
                        "birth_city": submission.birth_city,
                        "birth_state": submission.birth_state,
                        "high_school_graduation_year": submission.high_school_graduation_year,
                        "university_name": submission.university_name,
                        "graduation_year": submission.graduation_year,
                        "graduation_course": submission.graduation_course,
                        "current_ubs_name": submission.current_ubs_name,
                        "ubs_type": submission.ubs_type,
                        "rg_cpf_copy": request.build_absolute_uri(submission.rg_cpf_copy.url) if submission.rg_cpf_copy else None,
                        "reservista_cert_copy": request.build_absolute_uri(submission.reservista_cert_copy.url) if submission.reservista_cert_copy else None,
                        "diploma_copy": request.build_absolute_uri(submission.diploma_copy.url) if submission.diploma_copy else None,
                        "marriage_certificate_copy": request.build_absolute_uri(submission.marriage_certificate_copy.url) if submission.marriage_certificate_copy else None,
                        "address_proof_copy": request.build_absolute_uri(submission.address_proof_copy.url) if submission.address_proof_copy else None,
                        "residence_internet_copy": request.build_absolute_uri(submission.residence_internet_copy.url) if submission.residence_internet_copy else None,
                        "ubs_internet_copy": request.build_absolute_uri(submission.ubs_internet_copy.url) if submission.ubs_internet_copy else None,
                        "internet_speed": submission.internet_speed,
                        "internet_availability": submission.internet_availability,
                        "energy_availability": submission.energy_availability,
                    }
                }, safe=False)
            else:
                return JsonResponse({"error": "No submission found for this CPF."}, status=404)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found."}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
    
@csrf_exempt
def export_students_without_submissions(request):
    if request.method == 'GET':
        # Selecionar alunos que não têm submissões
        students_without_submissions = Student.objects.filter(
            ~Q(id__in=Submission.objects.values_list('student_id', flat=True))
        )

        # Configurar a resposta HTTP para exportação CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="alunos_sem_submissao.csv"'

        # Configurar o escritor CSV
        writer = csv.writer(response)
        writer.writerow([
            'CPF', 'Nome', 'Email', 'Telefone', 'Município', 'Estado',
            'Situação', 'Ciclo', 'Lista', 'DSEI', 'Número de Matrícula',
            'Turma do Tutor', 'Data', 'Condição', 'Data de Solicitação de Mudança', 'UBS'
        ])

        # Preencher as linhas do CSV
        for student in students_without_submissions:
            writer.writerow([
                student.CPF,
                student.Name,
                student.Email,
                student.Phone,
                student.Municipality,
                student.State,
                student.Status,
                student.Cycle,
                student.List,
                'Sim' if student.DSEI else 'Não',
                student.EnrollmentNumber,
                student.TutorClass,
                student.Date,
                student.Condition,
                student.RequestChangeDate.strftime('%d/%m/%Y') if student.RequestChangeDate else '',
                student.ubs.city if student.ubs else ''
            ])

        return response
    else:
        return JsonResponse({"error": "Método não permitido."}, status=405)

@csrf_exempt
def export_students_with_submissions(request):
    if request.method == 'GET':
        # Definição do SQL para incluir todos os campos de Submission
        sql_query = """
        SELECT 
            s.id AS student_id,
            s."CPF",
            s."Name",
            s."Email",
            sub.*
        FROM unasus_registros_student s
        INNER JOIN unasus_registros_submission sub
            ON sub.student_id = s.id;
        """

        # Executando a query no banco
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            columns = [col[0] for col in cursor.description]  # Obtem os nomes das colunas
            results = cursor.fetchall()

        # Mapeamento de cabeçalhos para português
        column_headers_ptbr = {
            "student_id": "ID do Aluno",
            "CPF": "CPF",
            "Name": "Nome",
            "Email": "Email",
            "timestamp": "Data e Hora da Submissão",
            "term_accepted": "Termo Aceito",
            "birthplace": "Local de Nascimento",
            "nationality": "Nacionalidade",
            "birth_date": "Data de Nascimento",
            "marital_status": "Estado Civil",
            "mother_name": "Nome da Mãe",
            "father_name": "Nome do Pai",
            "gender": "Gênero",
            "blood_type": "Tipo Sanguíneo",
            "rh_factor": "Fator RH",
            "ethnicity": "Etnia",
            "physical_disability": "Deficiência Física",
            "disability_details": "Detalhes da Deficiência",
            "disability_degree": "Grau da Deficiência",
            "psychological_disorder": "Transtorno Psicológico",
            "street_address": "Endereço",
            "number": "Número",
            "complement": "Complemento",
            "neighborhood": "Bairro",
            "city": "Cidade",
            "state": "Estado",
            "postal_code": "CEP",
            "rg": "RG",
            "birth_city": "Cidade de Nascimento",
            "birth_state": "Estado de Nascimento",
            "high_school_graduation_year": "Ano de Conclusão do Ensino Médio",
            "university_name": "Nome da Universidade",
            "graduation_year": "Ano de Graduação",
            "graduation_course": "Curso de Graduação",
            "current_ubs_name": "Nome da UBS Atual",
            "ubs_type": "Tipo de UBS",
            "rg_cpf_copy": "Cópia do RG/CPF",
            "reservista_cert_copy": "Cópia do Certificado de Reservista",
            "diploma_copy": "Cópia do Diploma",
            "marriage_certificate_copy": "Cópia do Certificado de Casamento",
            "address_proof_copy": "Comprovante de Endereço",
            "residence_internet_copy": "Comprovante de Internet Residencial",
            "ubs_internet_copy": "Comprovante de Internet da UBS",
            "internet_speed": "Velocidade da Internet",
            "internet_availability": "Disponibilidade de Internet",
            "energy_availability": "Disponibilidade de Energia",
        }

        # Traduzir os nomes das colunas para português
        column_headers = [column_headers_ptbr.get(col, col) for col in columns]

        # Configurar a resposta HTTP para exportação CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students_with_submissions_ptbr.csv"'

        # Configurar o escritor CSV
        writer = csv.writer(response)
        writer.writerow(column_headers)  # Escreve os nomes traduzidos das colunas no cabeçalho

        # Escrever os dados no CSV
        for row in results:
            writer.writerow(row)

        return response
    else:
        return JsonResponse({"error": "Método não permitido."}, status=405)

@csrf_exempt
def delete_submission(request, student_cpf):
    if request.method == 'DELETE':
        try:
            # Verifica se o estudante existe
            student = Student.objects.get(CPF=student_cpf)
            
            # Obtém a submissão associada ao estudante
            submission = Submission.objects.filter(student=student).first()
            
            if not submission:
                return JsonResponse({"error": "No submission found for this student."}, status=404)
            
            # Lista de campos de arquivos na submissão
            document_fields = [
                'rg_cpf_copy', 'reservista_cert_copy', 'diploma_copy',
                'marriage_certificate_copy', 'address_proof_copy',
                'residence_internet_copy', 'ubs_internet_copy'
            ]

            # Remove os arquivos associados do S3
            for field in document_fields:
                file_path = getattr(submission, field)
                if file_path:
                    default_storage.delete(file_path)
            
            submission.delete()
            
            return JsonResponse({"message": "Submission and associated documents successfully deleted."}, status=200)
        
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed."}, status=405)
