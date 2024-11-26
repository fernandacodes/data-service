import json
from django.db.models import Count
from django.http import JsonResponse
from django.db.models.functions import TruncMonth
from django.views.decorators.csrf import csrf_exempt

from unasus_registros.models.teleConsultation_model import Teleconsultation

def teleconsultations_by_month(request, ubs_id, year=None, month=None):
    teleconsultations = Teleconsultation.objects.filter(ubs_id=ubs_id)
    if year and month:
        teleconsultations = teleconsultations.filter(date__year=year, date__month=month)

    teleconsultations = (
        teleconsultations
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Count('id'))
        .order_by('month')
    )

    return JsonResponse(list(teleconsultations), safe=False)

@csrf_exempt
def list_all_teleconsultations(request):
    if request.method == 'GET':
        try:
            # Retrieve all teleconsultations
            teleconsultations = Teleconsultation.objects.all().values(
                'id', 'ubs_id', 'doctor_id', 'date', 'patient_name'
            )
            
            # Convert the queryset to a list of dictionaries
            teleconsultations_list = list(teleconsultations)

            return JsonResponse(teleconsultations_list, safe=False)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método não permitido.'}, status=405)

@csrf_exempt
def teleconsultations_create(request):
    if request.method == 'POST':
        try:
            # Parse JSON request body
            data = json.loads(request.body)

            # Extract fields from the request data
            ubs_id = data.get('ubs')
            doctor_id = data.get('doctor')
            date = data.get('date')
            patient_name = data.get('patient_name')

            # Validate required fields
            if not all([ubs_id, doctor_id, date, patient_name]):
                return JsonResponse({'error': 'Todos os campos são obrigatórios.'}, status=400)

            # Create a new Teleconsultation instance
            teleconsultation = Teleconsultation(
                ubs_id=ubs_id,
                doctor_id=doctor_id,
                date=date,
                patient_name=patient_name
            )
            teleconsultation.save()

            return JsonResponse({'message': 'Teleconsulta cadastrada com sucesso!'}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método não permitido.'}, status=405)
