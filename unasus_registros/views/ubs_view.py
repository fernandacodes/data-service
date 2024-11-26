from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models.ubs import Ubs
import json

@csrf_exempt
def create_ubs(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            ubs = Ubs.objects.create(
                name= data.get('name'),
                total_students=data.get("total_students"),
                city=data.get('city'),
                state=data.get('state'),
                ibge_code=data.get('ibge_code'),
                city_profile=data.get('city_profile'),
                vulnerability_profile=data.get('vulnerability_profile'),
                ine=data.get('ine'),
                cnes_code=data.get('cnes_code'),
                ubs_type=data.get('ubs_type'),
                condition=data.get('condition'),
                offering=data.get('offering'),
                action_date=data.get('action_date')
            )
            
            return JsonResponse({"message": "Successfully created UBS entry"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed."}, status=405)


@csrf_exempt
def get_ubs_by_id(request, ubs_id):
    if request.method == 'GET':
        try:
            ubs = Ubs.objects.get(id=ubs_id)
            return JsonResponse({
                "ubs": {
                    "id": ubs.id,
                    "name":ubs.name,
                    "total_students":ubs.total_students,
                    "city": ubs.city,
                    "state": ubs.state,
                    "ibge_code": ubs.ibge_code,
                    "city_profile": ubs.city_profile,
                    "vulnerability_profile": ubs.vulnerability_profile,
                    "ine": ubs.ine,
                    "cnes_code": ubs.cnes_code,
                    "ubs_type": ubs.ubs_type,
                    "condition": ubs.condition,
                    "offering": ubs.offering,
                    "action_date": ubs.action_date,
                }
            }, safe=False)
        except Ubs.DoesNotExist:
            return JsonResponse({"error": "UBS not found."}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
    
@csrf_exempt
def get_ubs_by_city(request, city_name):
    if request.method == 'GET':
        try:
            ubs_list = list(Ubs.objects.filter(city=city_name).values())
            return JsonResponse({"ubs_list": ubs_list}, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def get_ubs_by_state(request, state_name):
    if request.method == 'GET':
        try:
            ubs_list = list(Ubs.objects.filter(state=state_name).values())
            return JsonResponse({"ubs_list": ubs_list}, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)



@csrf_exempt
def get_all_ubs(request):
    if request.method == 'GET':
        ubs_list = list(Ubs.objects.all().values())
        return JsonResponse({"ubs_list": ubs_list}, safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def update_ubs(request, ubs_id):
    if request.method == 'PUT':
        try:
            ubs = Ubs.objects.get(id=ubs_id)
            data = json.loads(request.body.decode('utf-8'))
            ubs.total_students = data.get('total_students', ubs.total_students)            
            ubs.city = data.get('city', ubs.city)
            ubs.name = data.get('name', ubs.name)
            ubs.state = data.get('state', ubs.state)
            ubs.ibge_code = data.get('ibge_code', ubs.ibge_code)
            ubs.city_profile = data.get('city_profile', ubs.city_profile)
            ubs.vulnerability_profile = data.get('vulnerability_profile', ubs.vulnerability_profile)
            ubs.ine = data.get('ine', ubs.ine)
            ubs.cnes_code = data.get('cnes_code', ubs.cnes_code)
            ubs.ubs_type = data.get('ubs_type', ubs.ubs_type)
            ubs.condition = data.get('condition', ubs.condition)
            ubs.offering = data.get('offering', ubs.offering)
            ubs.action_date = data.get('action_date', ubs.action_date)

            ubs.save()

            return JsonResponse({"message": "Successfully updated UBS entry"}, status=200)
        except Ubs.DoesNotExist:
            return JsonResponse({"error": "UBS not found."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def delete_ubs(request, ubs_id):
    if request.method == 'DELETE':
        try:
            ubs = Ubs.objects.get(id=ubs_id)
            ubs.delete()
            return JsonResponse({"message": "Successfully deleted UBS entry"}, status=200)
        except Ubs.DoesNotExist:
            return JsonResponse({"error": "UBS not found."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed."}, status=405)
