import folium
from folium.plugins import HeatMap
import pandas as pd
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..models.student_model import Student
from unasus_registros.utils.tratar_dados import TratarCidadesBrasil

@csrf_exempt
def generate_heatmap(request):

    dados_brasil = TratarCidadesBrasil()
    
    if request.method == 'GET':

        students = Student.objects.all()
        students_data = pd.DataFrame(list(students.values('Municipality', 'State')))
        
        baseMap = folium.Map(location=[-15.788497, -47.899873], zoom_start=5)
        
        students_by_city = students_data.groupby(['Municipality', 'State']).size().reset_index(name='count')

        students_by_city['latitude'] = students_by_city['Municipality'].map(lambda x: dados_brasil.pesquisar_latitude(x))
        students_by_city['longitude'] = students_by_city['Municipality'].map(lambda x: dados_brasil.pesquisar_longitude(x))
        
        students_by_city.dropna(subset=['latitude', 'longitude'], inplace=True)

        heat_data = students_by_city[['latitude', 'longitude', 'count']].values.tolist()
        
        HeatMap(heat_data, radius=15).add_to(baseMap)

        # Gerar o mapa como string HTML
        map_html = baseMap._repr_html_()

        return HttpResponse(map_html, content_type='text/html')
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
