# views.py
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from unasus_registros.models.doctor import Doctor

@csrf_exempt
@require_http_methods(["POST"])
def doctor_create(request):
    try:
        data = json.loads(request.body)
        doctor = Doctor(
            name=data['name'],
            specialty_id=data['specialty'],
            registration_number=data['registration_number'],
            email=data['email'],
            phone=data['phone'],
            ubs_id=data['ubs']
        )
        doctor.save()
        return JsonResponse({'message': 'Doctor created successfully!'}, status=201)
    except (json.JSONDecodeError, KeyError, ValidationError) as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["GET"])
def doctor_get_by_id(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    data = {
        'id': doctor.id,
        'name': doctor.name,
        'specialty': doctor.specialty.id,
        'registration_number': doctor.registration_number,
        'email': doctor.email,
        'phone': doctor.phone,
        'ubs': doctor.ubs.id,
    }
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["GET"])
def doctor_get_all(request):
    doctors = Doctor.objects.all()
    data = list(doctors.values(
        'id', 'name', 'specialty', 'registration_number', 'email', 'phone', 'ubs'
    ))
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def doctor_update(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    try:
        data = json.loads(request.body)
        doctor.name = data.get('name', doctor.name)
        doctor.specialty_id = data.get('specialty', doctor.specialty_id)
        doctor.registration_number = data.get('registration_number', doctor.registration_number)
        doctor.email = data.get('email', doctor.email)
        doctor.phone = data.get('phone', doctor.phone)
        doctor.ubs_id = data.get('ubs', doctor.ubs_id)
        doctor.save()
        return JsonResponse({'message': 'Doctor updated successfully!'})
    except (json.JSONDecodeError, KeyError, ValidationError) as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def doctor_delete(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    doctor.delete()
    return JsonResponse({'message': 'Doctor deleted successfully!'})
