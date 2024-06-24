# management/commands/create_users.py
import csv
from django.core.management.base import BaseCommand
from ...models.user_model import CustomUser, Admin
from ...models.student_model import Student
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Load initial student and admin data from CSV'

    def handle(self, *args, **kwargs):
        # Cria ou obtém o grupo de alunos
        student_group, created = Group.objects.get_or_create(name='Students')
        
        # Cria ou obtém o grupo de administradores
        admin_group, created = Group.objects.get_or_create(name='Admins')

        # with open('/code/unasus_registros/data/students.csv', newline='') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for row in reader:
        #         user = CustomUser.objects.create_user(
        #             username=row['CPF'],
        #             password='',  # Usando a matrícula como senha
        #             cpf=row['CPF'],
        #             first_name=row['Nome'].split()[0],  # Usando o primeiro nome
        #             last_name=" ".join(row['Nome'].split()[1:]),  # Usando o restante como sobrenome
        #             email=row['Email'],
        #             role='student'
        #         )
        #         student = Student.objects.create(
        #             CPF=row['CPF'],
        #             Name=row['Nome'],
        #             Email=row['Email'],
        #             Phone=row['Telefone'],
        #             Municipality=row['Município'],
        #             State=row['UF'],
        #             Status=row['Situação'],
        #             Cycle=row['Ciclo'],
        #             List=row['Lista'],
        #             DSEI=row['DSEI'].lower() in ['true', '1', 't', 'yes', 'y', 'sim', 's'],
        #             EnrollmentNumber=row['Matricula'],
        #             TutorClass=row['TurmaTutor'],
        #             Date=row['Data'],
        #             Condition=row['Condição'],
        #             RequestChangeDate=row.get('RequestChangeDate')  # Pode ser None
        #         )
        #         user.groups.add(student_group)
        #         user.save()

        # with open('/code/unasus_registros/data/admins.csv', newline='') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for row in reader:
        #         user = CustomUser.objects.create_user(
        #             username=row['CPF'],
        #             password='adminpassword',  # ou qualquer outra lógica para a senha
        #             cpf=row['CPF'],
        #             first_name=row['Nome'].split()[0],  # Usando o primeiro nome
        #             last_name=" ".join(row['Nome'].split()[1:]),  # Usando o restante como sobrenome
        #             email=row['Email'],
        #             role='admin'
        #         )
        #         admin = Admin.objects.create(
        #             user=user,
        #             department=row['Departamento'],
        #             phone_number=row['Telefone']
        #         )
        #         user.groups.add(admin_group)
        #         user.save()

        # self.stdout.write(self.style.SUCCESS('Usuários importados com sucesso'))