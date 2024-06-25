from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadedfile import InMemoryUploadedFile
from ..models.submission import Submission
from ..models.student_model import Student
import json

@csrf_exempt
def create_submission(request):
    if request.method == 'POST':
        try:
            data = request.POST
            student_cpf = data.get('cpf')
            
            # Encontrar o estudante pelo CPF
            student = Student.objects.get(CPF=student_cpf)
            
            # Receber o arquivo PDF enviado
            document_file = request.FILES['document']

            # Criar uma nova submissão
            submission = Submission.objects.create(
                student=student,
                term_accepted=data.get('term_accepted') == 'True',
                full_name=data.get('full_name'),
                mother_name=data.get('mother_name'),
                father_name=data.get('father_name'),
                blood_type=data.get('blood_type'),
                rh_factor=data.get('rh_factor'),
                gender=data.get('gender'),
                race=data.get('race'),
                birth_date=data.get('birth_date'),
                nationality=data.get('nationality'),
                birth_city=data.get('birth_city'),
                birth_state=data.get('birth_state'),
                birth_country=data.get('birth_country'),
                phone=data.get('phone'),
                email=data.get('email'),
                marital_status=data.get('marital_status'),
                cpf=data.get('cpf'),
                rg_number=data.get('rg_number'),
                rg_issuer=data.get('rg_issuer'),
                rg_state=data.get('rg_state'),
                document=document_file,
                high_school_graduation_year=data.get('high_school_graduation_year'),
                university_name=data.get('university_name'),
                work_city=data.get('work_city'),
                work_state=data.get('work_state'),
                address=data.get('address'),
                neighborhood=data.get('neighborhood'),
                address_complement=data.get('address_complement'),
                address_city=data.get('address_city'),
                address_state=data.get('address_state'),
                address_zip_code=data.get('address_zip_code'),
                indigenous_ethnicity=data.get('indigenous_ethnicity'),
                disability=data.get('disability') == 'True',
                disability_degree=data.get('disability_degree'),
            )

            # Retornar a URL de download do documento
            document_url = request.build_absolute_uri(submission.document.url)

            return JsonResponse({"Message": "Successfully", "document_url": document_url}, status=201)
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
            return JsonResponse({
                "submission": {
                    "id": submission.id,
                    "student": submission.student.to_dict(),
                    "term_accepted": submission.term_accepted,
                    "full_name": submission.full_name,
                    "mother_name": submission.mother_name,
                    "father_name": submission.father_name,
                    "blood_type": submission.blood_type,
                    "rh_factor": submission.rh_factor,
                    "gender": submission.gender,
                    "race": submission.race,
                    "birth_date": submission.birth_date,
                    "nationality": submission.nationality,
                    "birth_city": submission.birth_city,
                    "birth_state": submission.birth_state,
                    "birth_country": submission.birth_country,
                    "phone": submission.phone,
                    "email": submission.email,
                    "marital_status": submission.marital_status,
                    "cpf": submission.cpf,
                    "rg_number": submission.rg_number,
                    "rg_issuer": submission.rg_issuer,
                    "rg_state": submission.rg_state,
                    "high_school_graduation_year": submission.high_school_graduation_year,
                    "university_name": submission.university_name,
                    "work_city": submission.work_city,
                    "work_state": submission.work_state,
                    "address": submission.address,
                    "neighborhood": submission.neighborhood,
                    "address_complement": submission.address_complement,
                    "address_city": submission.address_city,
                    "address_state": submission.address_state,
                    "address_zip_code": submission.address_zip_code,
                    "indigenous_ethnicity": submission.indigenous_ethnicity,
                    "disability": submission.disability,
                    "disability_degree": submission.disability_degree,
                    "document": request.build_absolute_uri(submission.document.url),  # Construindo URL absoluta para o documento
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
                        "full_name": submission.full_name,
                        "mother_name": submission.mother_name,
                        "father_name": submission.father_name,
                        "blood_type": submission.blood_type,
                        "rh_factor": submission.rh_factor,
                        "gender": submission.gender,
                        "race": submission.race,
                        "birth_date": submission.birth_date,
                        "nationality": submission.nationality,
                        "birth_city": submission.birth_city,
                        "birth_state": submission.birth_state,
                        "birth_country": submission.birth_country,
                        "phone": submission.phone,
                        "email": submission.email,
                        "marital_status": submission.marital_status,
                        "cpf": submission.cpf,
                        "rg_number": submission.rg_number,
                        "rg_issuer": submission.rg_issuer,
                        "rg_state": submission.rg_state,
                        "high_school_graduation_year": submission.high_school_graduation_year,
                        "university_name": submission.university_name,
                        "work_city": submission.work_city,
                        "work_state": submission.work_state,
                        "address": submission.address,
                        "neighborhood": submission.neighborhood,
                        "address_complement": submission.address_complement,
                        "address_city": submission.address_city,
                        "address_state": submission.address_state,
                        "address_zip_code": submission.address_zip_code,
                        "indigenous_ethnicity": submission.indigenous_ethnicity,
                        "disability": submission.disability,
                        "disability_degree": submission.disability_degree,
                        "document": request.build_absolute_uri(submission.document.url),  # Construindo URL absoluta para o documento
                        "created_at": submission.created_at,
                    }
                }, safe=False)
            else:
                return JsonResponse({"error": "No submission found for this CPF."}, status=404)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found."}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)

