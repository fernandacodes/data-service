# Generated by Django 5.0.6 on 2024-06-21 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unasus_registros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=11, unique=True)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Phone', models.CharField(max_length=15)),
                ('Municipality', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=2)),
                ('Status', models.CharField(max_length=20)),
                ('Cycle', models.CharField(max_length=10)),
                ('List', models.CharField(max_length=50)),
                ('DSEI', models.BooleanField(default=False)),
                ('EnrollmentNumber', models.IntegerField(unique=True)),
                ('TutorClass', models.CharField(max_length=50)),
                ('Date', models.DateField()),
                ('Condition', models.CharField(max_length=50)),
                ('RequestChangeDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_accepted', models.BooleanField(default=False)),
                ('guardian_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=11)),
                ('rg_number', models.CharField(max_length=20)),
                ('rg_issuer', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('university', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('total_score', models.CharField(max_length=10)),
                ('partial_score', models.CharField(blank=True, max_length=10, null=True)),
                ('document', models.FileField(upload_to='documents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unasus_registros.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Aluno',
        ),
    ]