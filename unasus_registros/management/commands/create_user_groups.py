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

        # with open('students.csv', newline='') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for row in reader:
        #         user = CustomUser.objects.create_user(
        #             username=row['CPF'],
        #             password=row['EnrollmentNumber'],
        #             cpf=row['CPF'],
        #             first_name=row['Name'].split()[0],  # Usando o primeiro nome
        #             last_name=" ".join(row['Name'].split()[1:]),  # Usando o restante como sobrenome
        #             email=row['Email'],
        #             role='student'
        #         )
        #         student = Student.objects.create(
        #             user=user,
        #             CPF=row['CPF'],
        #             Name=row['Name'],
        #             Email=row['Email'],
        #             Phone=row['Phone'],
        #             Municipality=row['Municipality'],
        #             State=row['State'],
        #             Status=row['Status'],
        #             Cycle=row['Cycle'],
        #             List=row['List'],
        #             DSEI=row['DSEI'].lower() in ['true', '1', 't', 'yes', 'y'],
        #             EnrollmentNumber=row['EnrollmentNumber'],
        #             TutorClass=row['TutorClass'],
        #             Date=row['Date'],
        #             Condition=row['Condition'],
        #             RequestChangeDate=row.get('RequestChangeDate')  # Pode ser None
        #         )
        #         user.groups.add(student_group)
        #         user.save()

        # with open('admins.csv', newline='') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for row in reader:
        #         user = CustomUser.objects.create_user(
        #             username=row['CPF'],
        #             password='adminpassword',  # ou qualquer outra lógica para a senha
        #             cpf=row['CPF'],
        #             first_name=row['Name'].split()[0],  # Usando o primeiro nome
        #             last_name=" ".join(row['Name'].split()[1:]),  # Usando o restante como sobrenome
        #             email=row['Email'],
        #             role='admin'
        #         )
        #         admin = Admin.objects.create(
        #             user=user,
        #             department=row['Department'],
        #             phone_number=row['Phone']
        #         )
        #         user.groups.add(admin_group)
        #         user.save()

        self.stdout.write(self.style.SUCCESS('Usuários importados com sucesso'))