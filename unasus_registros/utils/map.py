import folium
from folium.plugins import HeatMap
import pandas as pd
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models.student_model import Student

@csrf_exempt
def generate_heatmap(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students_data = pd.DataFrame(list(students.values('Municipality', 'State')))
        
        cidades_info = pd.read_csv('https://raw.githubusercontent.com/kelvins/municipios-brasileiros/main/csv/municipios.csv')
        
        baseMap = folium.Map(location=[-15.788497, -47.899873], zoom_start=5)
        
        students_by_city = students_data.groupby(['Municipality', 'State']).size().reset_index(name='count')

        students_by_city['latitude'] = students_by_city['Municipality'].apply(lambda x: pesquisar_latitude(x, cidades_info))
        students_by_city['longitude'] = students_by_city['Municipality'].apply(lambda x: pesquisar_longitude(x, cidades_info))
        
        students_by_city.dropna(subset=['latitude', 'longitude'], inplace=True)

        heat_data = students_by_city[['latitude', 'longitude', 'count']].values.tolist()
        
        HeatMap(heat_data, radius=15).add_to(baseMap)

        map_html = baseMap._repr_html_()

        return HttpResponse(map_html, content_type='text/html')
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)

def pesquisar_latitude(cidade, cidades_info):
    """
    Pesquisa a latitude de uma cidade na Base DEFAULT.

    Args:
        cidade (string): Nome de uma determinada Cidade.
        cidades_info (DataFrame): DataFrame com informações das cidades.

    Returns:
        float: Latitude de uma cidade
    """
    cidade = cidade.capitalize() 
    if cidade in cidades_info['nome'].values:
        latitude = cidades_info[cidades_info['nome'] == cidade]['latitude'].values[0]
        return latitude
    return None

def pesquisar_longitude(cidade, cidades_info):
    """
    Pesquisa a Longitude de uma cidade na Base DEFAULT.

    Args:
        cidade (string): Nome de uma determinada Cidade.
        cidades_info (DataFrame): DataFrame com informações das cidades.

    Returns:
        float: Longitude de uma cidade
    """
    cidade = cidade.capitalize() 
    if cidade in cidades_info['nome'].values:
        longitude = cidades_info[cidades_info['nome'] == cidade]['longitude'].values[0]
        return longitude
    return None
