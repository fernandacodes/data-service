from django.db import models

from unasus_registros.models.especialty import Specialty

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    ubs = models.ForeignKey('Ubs', on_delete=models.CASCADE, related_name='doctors')

    def __str__(self):
        return f"Dr. {self.name} - {self.specialty.name}"