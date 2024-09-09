# Generated by Django 4.2.16 on 2024-09-08 23:54

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
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
                ('role', models.CharField(choices=[('admin', 'Admin'), ('student', 'Student')], max_length=255)),
                ('cpf', models.CharField(max_length=255, unique=True)),
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
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=11, unique=True)),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255, unique=True)),
                ('Phone', models.CharField(max_length=255)),
                ('Municipality', models.CharField(max_length=255)),
                ('State', models.CharField(max_length=255)),
                ('Status', models.CharField(max_length=255)),
                ('Cycle', models.CharField(max_length=255)),
                ('List', models.CharField(max_length=255)),
                ('DSEI', models.BooleanField(default=False)),
                ('EnrollmentNumber', models.CharField(max_length=255)),
                ('TutorClass', models.CharField(max_length=255)),
                ('Date', models.CharField(max_length=255)),
                ('Condition', models.CharField(max_length=255)),
                ('RequestChangeDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('term_accepted', models.BooleanField(default=False)),
                ('birthplace', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('marital_status', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('blood_type', models.CharField(max_length=255)),
                ('rh_factor', models.CharField(max_length=255)),
                ('ethnicity', models.CharField(blank=True, max_length=255, null=True)),
                ('physical_disability', models.BooleanField(default=False)),
                ('disability_details', models.CharField(blank=True, max_length=255, null=True)),
                ('disability_degree', models.CharField(blank=True, max_length=255, null=True)),
                ('psychological_disorder', models.CharField(blank=True, max_length=255, null=True)),
                ('street_address', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('complement', models.CharField(blank=True, max_length=255, null=True)),
                ('neighborhood', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('rg', models.CharField(max_length=255)),
                ('birth_city', models.CharField(max_length=255)),
                ('birth_state', models.CharField(max_length=255)),
                ('high_school_graduation_year', models.CharField(max_length=255)),
                ('university_name', models.CharField(max_length=255)),
                ('graduation_year', models.CharField(max_length=255)),
                ('graduation_course', models.CharField(max_length=255)),
                ('current_ubs_name', models.CharField(max_length=255)),
                ('ubs_type', models.CharField(max_length=255)),
                ('rg_cpf_copy', models.FileField(blank=True, null=True, upload_to='documents/rg_cpf/')),
                ('reservista_cert_copy', models.FileField(blank=True, null=True, upload_to='documents/reservista_cert/')),
                ('diploma_copy', models.FileField(blank=True, null=True, upload_to='documents/diploma/')),
                ('marriage_certificate_copy', models.FileField(blank=True, null=True, upload_to='documents/marriage_certificate/')),
                ('address_proof_copy', models.FileField(blank=True, null=True, upload_to='documents/address_proof/')),
                ('residence_internet_copy', models.FileField(blank=True, null=True, upload_to='documents/residence_internet/')),
                ('ubs_internet_copy', models.FileField(blank=True, null=True, upload_to='documents/ubs_internet/')),
                ('internet_speed', models.CharField(blank=True, max_length=10, null=True)),
                ('internet_availability', models.CharField(blank=True, max_length=50, null=True)),
                ('energy_availability', models.CharField(blank=True, max_length=50, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unasus_registros.student')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
