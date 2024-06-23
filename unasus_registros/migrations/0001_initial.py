# Generated by Django 5.0.6 on 2024-06-23 00:03

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('student', 'Student')], max_length=10)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL)),
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
    ]
