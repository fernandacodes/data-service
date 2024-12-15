import csv
import logging
import psycopg2
from tqdm import tqdm
from dotenv import load_dotenv
import os
from datetime import datetime
import pytz
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from unasus_registros.models.user_model import CustomUser

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_db_credentials():
    environment = os.getenv('ENVIRONMENT')
    
    if environment == 'PRODUCTION':
        return {
            'host': os.getenv('POSTGRES_HOST_PROD'),
            'port': os.getenv('POSTGRES_PORT_PROD'),
            'dbname': os.getenv('POSTGRES_DB_PROD'),
            'user': os.getenv('POSTGRES_USER_PROD'),
            'password': os.getenv('POSTGRES_PASSWORD_PROD')
        }
    else:
        return {
            'host': os.getenv('POSTGRES_HOST'),
            'port': os.getenv('POSTGRES_PORT'),
            'dbname': os.getenv('POSTGRES_DB'),
            'user': os.getenv('POSTGRES_USER'),
            'password': os.getenv('POSTGRES_PASSWORD')
        }

# Função para conectar ao banco de dados PostgreSQL
def connect_db():
    credentials = get_db_credentials()
    try:
        connection = psycopg2.connect(
            host=credentials['host'],
            port=credentials['port'],
            dbname=credentials['dbname'],
            user=credentials['user'],
            password=credentials['password']
        )
        return connection
    except Exception as e:
        logger.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para limpar valores vazios do CSV
def clean_row_values(row):
    cleaned_row = {}
    for key, value in row.items():
        if value == "" or value == "Não":
            if key == "DSEI":
                cleaned_row[key] = False
            elif key == "Matricula":
                cleaned_row[key] = "X"
            elif key == "Situação":
                cleaned_row[key] = "INATIVO"
            elif key == "Telefone":
                cleaned_row[key] = "00000000000"
            elif key == "Data":
                cleaned_row[key] = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S')
            else:
                cleaned_row[key] = None
        else:
            # Verificar DSEI e tratar valores diferentes de "sim" ou "não"
            if key == "DSEI" and value not in ["sim", "não", "Sim", "Não"]:
                cleaned_row[key] = False
            else:
                cleaned_row[key] = value
    return cleaned_row

# Função para inserir os dados do aluno na tabela 'customuser' com role 'student'
def insert_student_customuser_data(cursor, row):
    # Limpar valores vazios
    row = clean_row_values(row)

    # Cria a query para inserir os dados do aluno no 'customuser'
    insert_query = """
        INSERT INTO unasus_registros_customuser 
        (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, role, cpf)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Gerar a senha para o aluno
    password = generate_password(row)
    hashed_password = hash_password(password)  # Hasheia a senha
    
    # Gerar a data e hora atual com o fuso horário correto (-03:00)
    timezone = pytz.timezone("America/Sao_Paulo")
    now = datetime.now(timezone)
    date_joined = now.strftime("%Y-%m-%d %H:%M:%S.%f %z")  # Formato: YYYY-MM-DD HH:MM:SS.MMM ±TZ
    
    # Preparar os dados para inserção
    data = (
        hashed_password,                  # senha hasheada
        None,                             # last_login (NULL por padrão)
        False,                            # is_superuser (não é superuser)
        row['CPF'],                       # username (CPF do aluno)
        row['Nome'].split()[0],           # first_name (primeiro nome)
        " ".join(row['Nome'].split()[1:]),  # last_name (restante do nome)
        row['Email'],                     # email
        False,                            # is_staff (não é staff)
        True,                             # is_active (aluno está ativo)
        date_joined,                      # date_joined (data atual)
        'student',                        # role (definir como student)
        row['CPF']                        # cpf
    )
    
    # Executar a query no banco
    cursor.execute(insert_query, data)

# Função para inserir os dados do aluno na tabela 'student'
def insert_student_data(cursor, row):
    # Limpar valores vazios
    row = clean_row_values(row)

    # Cria a query para inserir os dados do aluno na tabela 'student'
    insert_query = """
        INSERT INTO unasus_registros_student ("CPF", "Name", "Email", "Phone", "Municipality", "State", "Status", "Cycle", "List", "DSEI", "EnrollmentNumber", "TutorClass", "Date", "Condition", "RequestChangeDate", "ubs_id")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Obter a data atual formatada
    current_date = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S')

    data = (
        row['CPF'],                        # CPF
        row['Nome'],                       # Name
        row['Email'],                      # Email
        row['Telefone'],                   # Phone
        row['Município'],                  # Municipality
        row['UF'],                         # State
        row['Situação'],                   # Status
        row['Ciclo'],                      # Cycle
        row['Lista'],                      # List
        row['DSEI'],                       # DSEI
        row['Matricula'],                  # EnrollmentNumber
        row['TurmaTutor'],                 # TutorClass
        row['Data'],                       # Date
        row['Condição'],                   # Condition
        current_date,                      # RequestChangeDate
        None                               # ubs_id (assumindo como None por padrão)
    )

    # Executar a query no banco
    cursor.execute(insert_query, data)

# Função para gerar a senha do aluno
def generate_password(row):
    first_name = row['Nome'].split()[0]
    return row['CPF'] + first_name[:2].lower()  # Exemplo: CPF + 2 primeiros caracteres do nome

# Função para hashear a senha com o Django
def hash_password(password):
    user = CustomUser(username="tempuser")  # Criar um usuário temporário
    user.set_password(password)  # Usa o método set_password para gerar o hash
    return user.password  # Retorna a senha hasheada

# Função para processar o CSV e inserir os dados no banco
def process_csv_and_insert(csv_file):
    # Conectar ao banco de dados
    connection = connect_db()
    if not connection:
        logger.error("Não foi possível conectar ao banco de dados.")
        return

    cursor = connection.cursor()

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        total_rows = sum(1 for row in reader)

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        progress_bar = tqdm(total=total_rows, desc='Inserindo alunos', unit='registro')

        for row in reader:
            try:
                # Inserir dados na tabela 'customuser' (com role 'student')
                insert_student_customuser_data(cursor, row)

                # Inserir dados na tabela 'student'
                insert_student_data(cursor, row)

                progress_bar.set_postfix({'status': 'success'})
            except Exception as e:
                logger.error(f"Erro ao inserir dados do aluno {row['Nome']}: {e}")
                progress_bar.set_postfix({'status': 'error'})
            progress_bar.update(1)

        progress_bar.close()

    # Commitar as alterações e fechar a conexão
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    students_csv_path = 'charge/data/students.csv'
    process_csv_and_insert(students_csv_path)
