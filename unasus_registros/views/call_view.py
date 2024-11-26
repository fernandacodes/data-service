from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
import json
from unasus_registros.models.call import Call
from unasus_registros.models.ubs import Ubs

@csrf_exempt
def get_calls(request):
    calls = Call.objects.all()
    return JsonResponse(list(calls.values()), safe=False)

@csrf_exempt
def get_call_by_id(request, call_id):
    call = get_object_or_404(Call, id=call_id)
    return JsonResponse(call.to_dict())

@csrf_exempt
def create_call(request):
    data = json.loads(request.body)
    ubs = get_object_or_404(Ubs, id=data.get('ubs'))

    call = Call(
        subject=data.get('subject'),
        description=data.get('description'),
        status=data.get('status', 'open'),
        priority=data.get('priority'),
        reporter_name=data.get('reporter_name'),
        reporter_email=data.get('reporter_email'),
        ubs=ubs
    )
    call.save()  # Adicionado para salvar o objeto
    return JsonResponse(call.to_dict(), status=201)  # Corrigido para retornar o objeto criado

@csrf_exempt
def update_call(request, call_id):
    call = get_object_or_404(Call, id=call_id)
    data = json.loads(request.body)

    call.subject = data.get('subject', call.subject)
    call.description = data.get('description', call.description)
    call.status = data.get('status', call.status)
    call.priority = data.get('priority', call.priority)
    call.reporter_name = data.get('reporter_name', call.reporter_name)
    call.reporter_email = data.get('reporter_email', call.reporter_email)
    call.ubs = get_object_or_404(Ubs, id=data.get('ubs_id', call.ubs.id))

    call.save()
    return JsonResponse(call.to_dict())

@csrf_exempt
def delete_call(request, call_id):
    call = get_object_or_404(Call, id=call_id)
    call.delete()
    return JsonResponse({"message": "Call deleted successfully"}, status=204)

@csrf_exempt
def get_calls_report_by_ubs(request, ubs_id, year, month):
    ubs = get_object_or_404(Ubs, id=ubs_id)
    calls = Call.objects.filter(
        ubs=ubs, 
        created_at__year=year, 
        created_at__month=month
    ).values('status').annotate(total=Count('status'))

    return JsonResponse({
        "ubs": ubs.name,
        "year": year,
        "month": month,
        "calls": list(calls)
    })

@csrf_exempt
def get_overall_calls_report(request, year, month):
    calls = Call.objects.filter(
        created_at__year=year,
        created_at__month=month
    ).values('status').annotate(total=Count('status'))

    # Reorganize data by status
    report = {}
    for call in calls:
        status = call['status']
        report[status] = call['total']

    return JsonResponse({
        "year": year,
        "month": month,
        "report": report
    })
