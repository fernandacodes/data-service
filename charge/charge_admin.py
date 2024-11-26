import csv
import requests
import logging
from tqdm import tqdm
from tratar_dados import TratarCidadesBrasil
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_api_url():
    environment = os.getenv('ENVIRONMENT', 'development')
    if environment == 'production':
        return os.getenv('API_URL_PROD')
    return os.getenv('API_URL_DEV')

tratar_cidades = TratarCidadesBrasil()

def register_user(data):
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
    first_name = row['Nome'].split()[0]
    return row['CPF'] + first_name[:2].lower()

def send_requests_from_csv(csv_file, role):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        total_rows = sum(1 for row in reader)

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        progress_bar = tqdm(total=total_rows, desc='Enviando Requisições', unit='req')

        for row in reader:
            password = generate_password(row)
            

            user_data = {
                'user': {
                    'username': row['CPF'],
                    'password': password,
                    'email': row['Email'],
                    'cpf': row['CPF'],
                    'first_name': row['Nome'].split()[0],
                    'last_name': " ".join(row['Nome'].split()[1:]),
                    'role': role
                }
            }

            logger.info(f"Enviando dados do {role}: {user_data}")
            response = register_user(user_data)

            if response and response.status_code == 201:
                progress_bar.set_postfix({'status': 'success'})
            else:
                progress_bar.set_postfix({'status': 'error'})
                if response:
                    logger.error(f"Erro ao registrar {role} {row['Nome']}: {response.status_code} - {response.content}")
                else:
                    logger.error(f"Erro ao registrar {role} {row['Nome']}: Erro de conexão")

            progress_bar.update(1)

        progress_bar.close()

if __name__ == '__main__':
    admin_csv_path = 'charge/data/admin.csv'
    send_requests_from_csv(admin_csv_path, role='admin')
