from django.core.exceptions import ValidationError
from django.db import models
from ..models.student_model import Student

class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    term_accepted = models.BooleanField(default=False)
    birthplace = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    birth_date = models.DateField()
    marital_status = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=255)
    rh_factor = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255, null=True, blank=True)
    physical_disability = models.BooleanField(default=False)
    disability_details = models.CharField(max_length=255, null=True, blank=True)
    disability_degree = models.CharField(max_length=255, null=True, blank=True)
    psychological_disorder = models.CharField(max_length=255, null=True, blank=True)
    street_address = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    complement = models.CharField(max_length=255, null=True, blank=True)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    rg = models.CharField(max_length=255)
    birth_city = models.CharField(max_length=255)
    birth_state = models.CharField(max_length=255)
    high_school_graduation_year = models.CharField(max_length=255)
    university_name = models.CharField(max_length=255)
    graduation_year = models.CharField(max_length=255)
    graduation_course = models.CharField(max_length=255)
    current_ubs_name = models.CharField(max_length=255)
    ubs_type = models.CharField(max_length=255)
    
    rg_cpf_copy = models.FileField(upload_to='documents/rg_cpf/', null=True, blank=True)
    reservista_cert_copy = models.FileField(upload_to='documents/reservista_cert/', null=True, blank=True)
    diploma_copy = models.FileField(upload_to='documents/diploma/', null=True, blank=True)
    marriage_certificate_copy = models.FileField(upload_to='documents/marriage_certificate/', null=True, blank=True)
    address_proof_copy = models.FileField(upload_to='documents/address_proof/', null=True, blank=True)
    residence_internet_copy = models.FileField(upload_to='documents/residence_internet/', null=True, blank=True)
    ubs_internet_copy = models.FileField(upload_to='documents/ubs_internet/', null=True, blank=True)
    
    internet_speed = models.CharField(max_length=10, null=True, blank=True)
    internet_availability = models.CharField(max_length=50, null=True, blank=True)
    energy_availability = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Submission by {self.student.full_name}"

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
