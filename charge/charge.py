import csv
import requests
import logging
from tqdm import tqdm
from tratar_dados import TratarCidadesBrasil

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_api_url():
    base_url = 'http://localhost:8000/api/register/' 
    environment = 'local' 
    
    if environment == 'production':
        base_url = 'http://15.228.45.143:8000/api/register/' 
    
    return base_url

tratar_cidades = TratarCidadesBrasil()

def register_students(data):
    url = get_api_url()
    try:
        response = requests.post(url, json=data)
        response.raise_for_status() 
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao enviar requisição para {url}: {e}")
        if e.response is not None:
            logger.error(f"Resposta do servidor: {e.response.content}")
        return None

def generate_password(row):
    if row['Matricula']:
        return row['Matricula']
    else:
        return row['CPF'] + row['Data'].replace('-', '')

def generate_enrollment_number(row):
    if row['Matricula']:
        return row['Matricula']
    else:
        return 'X'

def send_requests_from_csv(csv_file):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        total_rows = sum(1 for row in reader) 

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        progress_bar = tqdm(total=total_rows, desc='Enviando Requisições', unit='req')

        for row in reader:
            password = generate_password(row)
            enrollment_number = generate_enrollment_number(row)
            
            municipio_padronizado = tratar_cidades.tratar_cidade(
                tratar_cidades.listar_cidades(), 
                row['Município']
            )
            
            student_data = {
                'user': {
                    'username': row['CPF'],  
                    'password': password, 
                    'email': row['Email'],
                    'cpf': row['CPF'],
                    'first_name': row['Nome'].split()[0],
                    'last_name': " ".join(row['Nome'].split()[1:]),
                    'role': 'student'
                },
                'student': {
                    'CPF': row['CPF'],
                    'Name': row['Nome'],
                    'Email': row['Email'],
                    'Phone': row['Telefone'],
                    'Municipality': municipio_padronizado,
                    'State': row['UF'],
                    'Status': row['Situação'],
                    'Cycle': row['Ciclo'],
                    'List': row['Lista'],
                    'DSEI': row['DSEI'].lower() in ['true', '1', 't', 'yes', 'y', 'sim', 's'],
                    'EnrollmentNumber': enrollment_number,
                    'TutorClass': row['TurmaTutor'],
                    'Date': row['Data'],
                    'Condition': row['Condição'],
                    'RequestChangeDate': row.get('RequestChangeDate')
                }
            }

            logger.info(f"Enviando dados do aluno: {student_data}")
            response = register_students(student_data)

            if response and response.status_code == 201:
                progress_bar.set_postfix({'status': 'success'})
            else:
                progress_bar.set_postfix({'status': 'error'})

                if response:
                    logger.error(f"Erro ao registrar aluno {row['Nome']}: {response.status_code} - {response.content}")
                else:
                    logger.error(f"Erro ao registrar aluno {row['Nome']}: Erro de conexão")

            progress_bar.update(1)

        progress_bar.close()

if __name__ == '__main__':
    csv_file_path = './data/students.csv'
    send_requests_from_csv(csv_file_path)
