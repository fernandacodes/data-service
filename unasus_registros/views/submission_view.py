from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
import json
from ..models.submission import *

@csrf_exempt
def create_submission(request):
    if request.method == 'POST':
        try:
            student_cpf = request.POST.get('cpf')
            term_accepted = request.POST.get('term_accepted')
            guardian_name = request.POST.get('guardian_name')
            mother_name = request.POST.get('mother_name')
            father_name = request.POST.get('father_name')
            birth_date = request.POST.get('birth_date')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            rg_number = request.POST.get('rg_number')
            rg_issuer = request.POST.get('rg_issuer')
            state = request.POST.get('state')
            university = request.POST.get('university')
            neighborhood = request.POST.get('neighborhood')
            city = request.POST.get('city')
            uf = request.POST.get('uf')
            total_score = request.POST.get('total_score')
            partial_score = request.POST.get('partial_score')

            # Receber o arquivo PDF enviado
            document_file = request.FILES['document']

            # Encontrar o estudante pelo CPF
            student = Student.objects.get(CPF=student_cpf)

            # Salvar o arquivo no banco de dados
            submission = Submission.objects.create(
                student=student,
                term_accepted=term_accepted,
                guardian_name=guardian_name,
                mother_name=mother_name,
                father_name=father_name,
                birth_date=birth_date,
                phone=phone,
                email=email,
                rg_number=rg_number,
                rg_issuer=rg_issuer,
                state=state,
                university=university,
                neighborhood=neighborhood,
                city=city,
                uf=uf,
                total_score=total_score,
                partial_score=partial_score,
                document=document_file  # Salvar o arquivo PDF no campo 'document'
            )

            # Retornar a URL de download do documento
            document_url = request.build_absolute_uri(submission.document.url)

            return JsonResponse({"Message": "Sucessfuly"}, status=201)
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
                    "guardian_name": submission.guardian_name,
                    "mother_name": submission.mother_name,
                    "father_name": submission.father_name,
                    "birth_date": submission.birth_date,
                    "phone": submission.phone,
                    "email": submission.email,
                    "cpf": submission.cpf,
                    "rg_number": submission.rg_number,
                    "rg_issuer": submission.rg_issuer,
                    "state": submission.state,
                    "university": submission.university,
                    "neighborhood": submission.neighborhood,
                    "city": submission.city,
                    "uf": submission.uf,
                    "total_score": submission.total_score,
                    "partial_score": submission.partial_score,
                    "document": request.build_absolute_uri(submission.document.url),  # Construindo URL absoluta para o documento
                    "created_at": submission.created_at,
                }
            }, safe=False)
        except Submission.DoesNotExist:
            return JsonResponse({"error": f"Submission with ID {submission_id} does not exist."}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)

