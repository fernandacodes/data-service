from django.db import models
from django.utils import timezone

from unasus_registros.models.doctor import Doctor
from unasus_registros.models.ubs import Ubs

class Teleconsultation(models.Model):
    ubs = models.ForeignKey(Ubs, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    patient_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Consulta de {self.patient_name} com {self.doctor.name} em {self.date}"
