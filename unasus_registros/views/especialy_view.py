import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from unasus_registros.models.especialty import Specialty

@csrf_exempt
@require_http_methods(["POST"])
def specialty_create(request):
    try:
        data = json.loads(request.body)
        specialty = Specialty(
            name=data['name']
        )
        specialty.save()
        return JsonResponse({'message': 'Specialty created successfully!'}, status=201)
    except (json.JSONDecodeError, KeyError, ValidationError) as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["GET"])
def specialty_get_by_id(request, id):
    specialty = get_object_or_404(Specialty, pk=id)
    data = {
        'id': specialty.id,
        'name': specialty.name
    }
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["GET"])
def specialty_get_all(request):
    specialties = Specialty.objects.all()
    data = list(specialties.values(
        'id', 'name'
    ))
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def specialty_update(request, id):
    specialty = get_object_or_404(Specialty, pk=id)
    try:
        data = json.loads(request.body)
        specialty.name = data.get('name', specialty.name)
        specialty.save()
        return JsonResponse({'message': 'Specialty updated successfully!'})
    except (json.JSONDecodeError, KeyError, ValidationError) as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def specialty_delete(request, id):
    specialty = get_object_or_404(Specialty, pk=id)
    specialty.delete()
    return JsonResponse({'message': 'Specialty deleted successfully!'})
