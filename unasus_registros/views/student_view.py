from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from..models.student_model import Student

# Função para criar um novo aluno
@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        try:
            body = request.body
            data = json.loads(body.decode('utf-8'))
            cpf = str(data.get('CPF'))
            name = data.get('Name')
            email = data.get('Email')
            phone = data.get('Phone')
            municipality = data.get('Municipality')
            state = data.get('State')
            status = data.get('Status')
            cycle = data.get('Cycle')
            list_ = data.get('List')
            dsei = data.get('DSEI')
            enrollment_number = data.get('EnrollmentNumber')
            tutor_class = data.get('TutorClass')
            date = data.get('Date')
            condition = data.get('Condition')
            request_change_date = data.get('RequestChangeDate')

            aluno = Student.objects.create(
                CPF=cpf,
                Name=name,
                Email=email,
                Phone=phone,
                Municipality=municipality,
                State=state,
                Status=status,
                Cycle=cycle,
                List=list_,
                DSEI=dsei,
                EnrollmentNumber=enrollment_number,
                TutorClass=tutor_class,
                Date=date,
                Condition=condition,
                RequestChangeDate=request_change_date
            )

            return JsonResponse({"message": "Student created successfully."}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed."}, status=405)

# Função para listar todos os alunos
@csrf_exempt
def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students_list = list(students.values())
        return JsonResponse({"students": students_list}, safe=False)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)

# Função para listar um aluno por ID
@csrf_exempt
def get_student_by_cpf(request):
    if request.method == 'POST':
        try:
            body = request.body
            data = json.loads(body.decode('utf-8'))
            cpf = str(data.get('cpf'))
            student = Student.objects.get(CPF=cpf)
            return JsonResponse({"student": student.to_dict()}, safe=False)
        except Student.DoesNotExist:
            return JsonResponse({"error": f"Student with CPF {cpf} does not exist."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)

# Função para atualizar parcialmente um aluno
@csrf_exempt
def update_student(request, student_id):
    if request.method == 'PATCH':
        try:
            student = Student.objects.get(id=student_id)
            data = json.loads(request.body.decode('utf-8'))
            
            for key, value in data.items():
                setattr(student, key, value)
            
            student.save()
            return JsonResponse({"message": f"Student with ID {student_id} updated successfully."})
        except Student.DoesNotExist:
            return JsonResponse({"error": f"Student with ID {student_id} does not exist."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
    
@csrf_exempt
def search_student_by_name(request):
    name = request.GET.get('name', None)
    if not name:
        return JsonResponse({"error": "No name provided."}, status=400)

    students = Student.objects.filter(Name__icontains=name)
    students_list = list(students.values())
    return JsonResponse({"students": students_list}, safe=False)

@csrf_exempt
def search_students_with_submissions(request):
    if request.method == 'GET':
        try:
            students_with_submissions = Student.objects.filter(submission__isnull=False).distinct()
            students_list = list(students_with_submissions.values())
            return JsonResponse({"students": students_list}, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed."}, status=405)
