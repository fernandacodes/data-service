from django.db import models

class Ubs(models.Model):
    city = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default="UBS Padrão")
    state = models.CharField(max_length=255)
    ibge_code = models.CharField(max_length=255)
    city_profile = models.CharField(max_length=255)
    vulnerability_profile = models.CharField(max_length=255)
    ine = models.CharField(max_length=255)
    cnes_code = models.CharField(max_length=255)
    ubs_type = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    offering = models.CharField(max_length=255)
    action_date = models.DateField()
    total_students = models.IntegerField(default=0)


    def __str__(self):
        return f"UBS {self.cnes_code} - {self.city}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
