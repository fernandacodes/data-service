# Generated by Django 5.0.6 on 2024-06-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unasus_registros', '0006_alter_student_enrollmentnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Phone',
            field=models.CharField(max_length=255),
        ),
    ]
