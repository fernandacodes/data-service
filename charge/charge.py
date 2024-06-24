import csv
import requests
import logging
from tqdm import tqdm

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Função para enviar requisições HTTP para registrar alunos
def register_students(data):
    url = 'http://web:8000/api/register/'  # Substitua pela URL correta do seu endpoint
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Lança exceção se houver erro HTTP
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao enviar requisição para {url}: {e}")
        if e.response is not None:
            logger.error(f"Resposta do servidor: {e.response.content}")
        return None

# Função para gerar senha
def generate_password(row):
    if row['Matricula']:
        return row['Matricula']
    else:
        return row['CPF'] + row['Data'].replace('-', '')

# Função para gerar o número de matrícula (Enrollment Number)
def generate_enrollment_number(row):
    if row['Matricula']:
        return row['Matricula']
    else:
        return 'X'

# Função para ler dados de um arquivo CSV e enviar requisições para cada linha
def send_requests_from_csv(csv_file):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        total_rows = sum(1 for row in reader)  # Conta o número total de linhas no CSV

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        progress_bar = tqdm(total=total_rows, desc='Enviando Requisições', unit='req')

        for row in reader:
            password = generate_password(row)
            enrollment_number = generate_enrollment_number(row)
            student_data = {
                'user': {
                    'username': row['CPF'],  # Usando CPF como username
                    'password': password,  # Usando a lógica para gerar senha
                    'email': row['Email'],
                    'cpf': row['CPF'],
                    'first_name': row['Nome'].split()[0],  # Usando o primeiro nome
                    'last_name': " ".join(row['Nome'].split()[1:]),  # Usando o restante como sobrenome
                    'role': 'student'
                },
                'student': {
                    'CPF': row['CPF'],
                    'Name': row['Nome'],
                    'Email': row['Email'],
                    'Phone': row['Telefone'],
                    'Municipality': row['Município'],
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

            # Exemplo de verificação do status da resposta
            if response and response.status_code == 201:  # 201 Created
                progress_bar.set_postfix({'status': 'success'})
            else:
                progress_bar.set_postfix({'status': 'error'})

                # Exibir mais detalhes do erro no log
                if response:
                    logger.error(f"Erro ao registrar aluno {row['Nome']}: {response.status_code} - {response.content}")
                else:
                    logger.error(f"Erro ao registrar aluno {row['Nome']}: Erro de conexão")

            progress_bar.update(1)

        progress_bar.close()

if __name__ == '__main__':
    csv_file_path = '/code/charge/data/students.csv'  # Substitua pelo caminho correto do seu arquivo CSV
    send_requests_from_csv(csv_file_path)
